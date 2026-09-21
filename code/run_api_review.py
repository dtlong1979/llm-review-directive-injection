"""Run reviews through provider APIs (Gemini / OpenAI / Anthropic) over experiments/<exp>/inputs,
mirroring chat usage: the paper is sent as an ATTACHED FILE (its own content part, with a filename),
and the prompt is a SEPARATE TEXT PART -- not concatenated into a single string.
Each file is an independent call (no history, no system prompt, no temperature set).

Attachment mode (auto-detected on the first call, then KEPT FIXED for the whole run; recorded in _raw and _run_info.json):
  Gemini : "files_api"  = upload via the Files API (display_name = filename) then reference file_data
           "inline"     = inline_data text/plain (fallback)
  OpenAI : "input_file" = input_file content part (filename + base64 file_data)
           "text_part"  = a separate input_text content part carrying the file (fallback), prompt in another part
Part order: [attached file] then [prompt] -- as when you attach a file and then type the request.

Rate limiting: --min-interval (default Gemini 15s ~ 4 calls/min for the free tier; OpenAI 3s),
--max-calls (default 30), respecting Retry-After / RetryInfo on 429.

Usage:
  python -X utf8 run_api_review.py --list-models gemini|openai
  python -X utf8 run_api_review.py --exp mini_test_03 --provider gemini --model <model name> [--limit 2]
Keys are read from .env (GEMINI_API_KEY, OPENAI_API_KEY). Keys are never printed.
"""
import argparse, base64, datetime, json, os, pathlib, re, sys, time

import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
GEM = "https://generativelanguage.googleapis.com"


def load_env():
    env = {}
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    for k in ("GEMINI_API_KEY", "OPENAI_API_KEY", "CLAUDE_API_KEY", "ANTHROPIC_API_KEY"):
        env[k] = os.environ.get(k) or env.get(k, "")
    env["CLAUDE_API_KEY"] = env["CLAUDE_API_KEY"] or env["ANTHROPIC_API_KEY"]
    return env


class HTTPFail(Exception):
    def __init__(self, code, body, retry_after=None):
        super().__init__(f"HTTP {code}")
        self.code, self.body, self.retry_after = code, body, retry_after


def check(r):
    if r.status_code >= 400:
        ra = r.headers.get("retry-after")
        m = re.search(r'"retryDelay":\s*"(\d+)s"', r.text)
        raise HTTPFail(r.status_code, r.text[:500], float(ra) if ra else (float(m.group(1)) if m else None))
    return r.json()


# ---------------- Gemini ----------------
def gemini_upload(key, name, data):
    start = requests.post(f"{GEM}/upload/v1beta/files", timeout=120, headers={
        "x-goog-api-key": key, "X-Goog-Upload-Protocol": "resumable", "X-Goog-Upload-Command": "start",
        "X-Goog-Upload-Header-Content-Length": str(len(data)), "X-Goog-Upload-Header-Content-Type": "text/plain",
        "Content-Type": "application/json"}, json={"file": {"display_name": name}})
    if start.status_code >= 400:
        check(start)
    url = start.headers.get("x-goog-upload-url")
    up = requests.post(url, timeout=120, headers={"X-Goog-Upload-Offset": "0", "X-Goog-Upload-Command": "upload, finalize",
                                                  "Content-Length": str(len(data))}, data=data)
    return check(up)["file"]


SYSTEM = None  # defensive system prompt (set via --system); None = none


def gemini_call(env, model, name, paper, prompt, mode):
    key = env["GEMINI_API_KEY"]
    is_pdf = isinstance(paper, bytes)  # PDF: send the raw file, mime application/pdf
    data = paper if is_pdf else paper.encode("utf-8")
    mime = "application/pdf" if is_pdf else "text/plain"
    uploaded = None
    if mode == "files_api":
        uploaded = gemini_upload(key, name, data)
        file_part = {"file_data": {"mime_type": uploaded.get("mimeType", mime), "file_uri": uploaded["uri"]}}
    else:
        file_part = {"inline_data": {"mime_type": mime, "data": base64.b64encode(data).decode()}}
    body = {"contents": [{"role": "user", "parts": [file_part, {"text": prompt}]}]}
    if SYSTEM:
        body["systemInstruction"] = {"parts": [{"text": SYSTEM}]}
    try:
        js = check(requests.post(f"{GEM}/v1beta/models/{model}:generateContent", timeout=300,
                                 headers={"x-goog-api-key": key, "Content-Type": "application/json"}, json=body))
    finally:
        if uploaded:  # clean up the uploaded file
            try:
                requests.delete(f"{GEM}/v1beta/{uploaded['name']}", headers={"x-goog-api-key": key}, timeout=30)
            except requests.RequestException:
                pass
    cands = js.get("candidates") or []
    parts = cands[0].get("content", {}).get("parts", []) if cands else []
    out = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    meta = {"model_returned": js.get("modelVersion"), "usage": js.get("usageMetadata"),
            "finish_reason": cands[0].get("finishReason") if cands else None, "prompt_feedback": js.get("promptFeedback")}
    return out, meta, js


# ---------------- OpenAI ----------------
def openai_call(env, model, name, paper, prompt, mode):
    if mode == "rag_inline":  # RAG-style: paper text appended directly after the prompt in the SAME text block, no boundary marker
        body = {"model": model, "input": [{"role": "user", "content": [{"type": "input_text", "text": f"{prompt.rstrip()}\n\n{paper}"}]}]}
    else:
        if isinstance(paper, bytes):  # PDF: send the raw file via input_file (the model extracts text and renders images)
            file_part = {"type": "input_file", "filename": name,
                         "file_data": "data:application/pdf;base64," + base64.b64encode(paper).decode()}
        elif mode == "input_file":
            file_part = {"type": "input_file", "filename": name,
                         "file_data": "data:text/plain;base64," + base64.b64encode(paper.encode("utf-8")).decode()}
        else:
            file_part = {"type": "input_text", "text": f"[Attached file: {name}]\n{paper}"}
        body = {"model": model, "input": [{"role": "user", "content": [file_part, {"type": "input_text", "text": prompt}]}]}
    if SYSTEM:
        body["instructions"] = SYSTEM
    js = check(requests.post("https://api.openai.com/v1/responses", timeout=600, json=body,
                             headers={"Authorization": f"Bearer {env['OPENAI_API_KEY']}", "Content-Type": "application/json"}))
    out = "".join(c.get("text", "") for item in js.get("output", []) if item.get("type") == "message"
                  for c in item.get("content", []) if c.get("type") == "output_text")
    meta = {"model_returned": js.get("model"), "usage": js.get("usage"), "status": js.get("status"),
            "incomplete_details": js.get("incomplete_details")}
    return out, meta, js


# ---------------- Anthropic ----------------
def anthropic_call(env, model, name, paper, prompt, mode):
    key = env["CLAUDE_API_KEY"]
    if mode == "rag_inline":
        content = [{"type": "text", "text": f"{prompt.rstrip()}\n\n{paper}"}]
    elif isinstance(paper, bytes):  # PDF
        content = [{"type": "document", "source": {"type": "base64", "media_type": "application/pdf",
                    "data": base64.b64encode(paper).decode()}}, {"type": "text", "text": prompt}]
    else:  # text paper as an attached document (with boundaries, like OpenAI's input_file)
        content = [{"type": "document", "source": {"type": "text", "media_type": "text/plain", "data": paper}},
                   {"type": "text", "text": prompt}]
    body = {"model": model, "max_tokens": 4096, "messages": [{"role": "user", "content": content}]}
    if SYSTEM:
        body["system"] = SYSTEM
    js = check(requests.post("https://api.anthropic.com/v1/messages", timeout=600, json=body,
                             headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}))
    out = "".join(b.get("text", "") for b in js.get("content", []) if b.get("type") == "text")
    meta = {"model_returned": js.get("model"), "usage": js.get("usage"), "stop_reason": js.get("stop_reason")}
    return out, meta, js


PROVIDERS = {
    "gemini": dict(call=gemini_call, modes=["files_api", "inline"], interval=15.0),
    "openai": dict(call=openai_call, modes=["input_file", "text_part"], interval=3.0),
    "anthropic": dict(call=anthropic_call, modes=["document"], interval=3.0),
}


def list_models(provider, env):
    if provider == "gemini":
        js = check(requests.get(f"{GEM}/v1beta/models?pageSize=1000", headers={"x-goog-api-key": env["GEMINI_API_KEY"]}, timeout=60))
        for m in js.get("models", []):
            if "generateContent" in m.get("supportedGenerationMethods", []):
                print(m["name"].split("/", 1)[-1], "|", m.get("displayName", ""))
    elif provider == "anthropic":
        js = check(requests.get("https://api.anthropic.com/v1/models?limit=100",
                                headers={"x-api-key": env["CLAUDE_API_KEY"], "anthropic-version": "2023-06-01"}, timeout=60))
        for m in js.get("data", []):
            print(m["id"], "|", m.get("display_name", ""))
    else:
        js = check(requests.get("https://api.openai.com/v1/models", headers={"Authorization": f"Bearer {env['OPENAI_API_KEY']}"}, timeout=60))
        for m in sorted(x["id"] for x in js.get("data", [])):
            print(m)


def strip_fence(s):
    m = re.search(r"```(?:markdown|md)?\s*\n(.*?)```", s, re.S)
    return m.group(1).strip() + "\n" if m and "SCORES" in m.group(1) else s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-models", choices=list(PROVIDERS))
    ap.add_argument("--exp", default="mini_test_03")
    ap.add_argument("--provider", choices=list(PROVIDERS))
    ap.add_argument("--model")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", default="")
    ap.add_argument("--min-interval", type=float, default=None, help="minimum seconds between two calls")
    ap.add_argument("--max-calls", type=int, default=30, help="cap on the number of generation calls in a run")
    ap.add_argument("--mode", default=None, help="force the attachment mode (default: auto-detect)")
    ap.add_argument("--system", default=None, help="defensive system prompt (a string, or @path_to_file)")
    ap.add_argument("--skip-on-overload", action="store_true", help="minute-scale 503/429: skip the file (retry next run) instead of stopping")
    a = ap.parse_args()
    env = load_env()
    prov = a.list_models or a.provider
    if not prov:
        ap.error("need --provider or --list-models")
    keyname = {"gemini": "GEMINI_API_KEY", "anthropic": "CLAUDE_API_KEY"}.get(prov, "OPENAI_API_KEY")
    if not env[keyname]:
        sys.exit(f"Missing {keyname} in .env")
    if a.list_models:
        return list_models(prov, env)
    if not a.model:
        sys.exit("Need --model (see --list-models)")

    global SYSTEM
    if a.system:
        SYSTEM = pathlib.Path(a.system[1:]).read_text(encoding="utf-8") if a.system.startswith("@") else a.system
    P = PROVIDERS[prov]
    interval = a.min_interval if a.min_interval is not None else P["interval"]
    exp = ROOT / "experiments" / a.exp
    prompt = (exp / "PROMPT_REVIEW.md").read_text(encoding="utf-8")
    files = sorted((exp / "inputs").glob("paper_*.md")) + sorted((exp / "inputs").glob("paper_*.pdf"))
    if a.only:
        wanted = {x.strip() for x in a.only.split(",")}
        files = [f for f in files if f.name in wanted]
    if a.limit:
        files = files[: a.limit]
    out = exp / f"out_api_{prov}_{re.sub(r'[^A-Za-z0-9._-]', '_', a.model)}{'_rag' if a.mode == 'rag_inline' else ''}{'_def' if a.system else ''}"
    (out / "_raw").mkdir(parents=True, exist_ok=True)
    info_path = out / "_run_info.json"
    info = json.loads(info_path.read_text(encoding="utf-8")) if info_path.exists() else {}
    mode = a.mode or info.get("attach_mode")

    calls, last = 0, 0.0
    for f in files:
        target = out / f"review_{f.name}"
        if target.exists():
            print("skip (exists):", target.name)
            continue
        if calls >= a.max_calls:
            print(f"Stop: reached --max-calls={a.max_calls}")
            break
        paper = f.read_bytes() if f.suffix == ".pdf" else f.read_text(encoding="utf-8")
        tried_modes = [mode] if mode else list(P["modes"])
        result = None
        for m_ in tried_modes:
            for attempt in range(6):
                wait = interval - (time.time() - last)
                if wait > 0:
                    time.sleep(wait)
                last = time.time()
                calls += 1
                try:
                    t0 = time.time()
                    result = P["call"](env, a.model, f.name, paper, prompt, m_)
                    mode = m_
                    break
                except HTTPFail as e:
                    if e.code == 429 and "PerDay" in e.body:
                        sys.exit(f"{f.name}: DAILY quota exhausted for this model (free tier) - rerun tomorrow; finished files are skipped")
                    if e.code == 429 and "insufficient_quota" in e.body:
                        sys.exit(f"{f.name}: account credit exhausted (insufficient_quota) - stop, no retry")
                    if e.code == 429 or e.code >= 500:
                        if a.skip_on_overload and attempt >= 1:
                            print(f"{f.name}: HTTP {e.code} - skip, retry next run")
                            break
                        if attempt >= 3:  # prolonged overload (e.g. 503 high demand) -> stop this file, do not burn quota
                            sys.exit(f"{f.name}: HTTP {e.code} repeated - model overloaded, retry later or switch model")
                        w = min(max(e.retry_after or 0, 20 * (2 ** attempt)), 120)
                        print(f"{f.name}: HTTP {e.code}, wait {int(w)}s then retry")
                        time.sleep(w)
                        continue
                    if e.code == 400 and not a.mode and m_ != tried_modes[-1]:
                        print(f"{f.name}: attachment mode '{m_}' not supported ({e.body[:160]}) -> trying another")
                        break
                    sys.exit(f"{f.name}: HTTP {e.code} - {e.body}")
                except requests.RequestException as e:
                    if attempt < 5:
                        time.sleep(20 * (2 ** attempt))
                        continue
                    sys.exit(f"{f.name}: network error - {e}")
            if result or a.skip_on_overload:
                break
        if not result:
            if a.skip_on_overload:
                continue
            sys.exit(f"{f.name}: call failed")
        review, meta, raw = result
        info.setdefault("attach_mode", mode)
        info.update(provider=prov, model_requested=a.model, exp=a.exp, prompt_separate=(mode != "rag_inline"), system_prompt=None, temperature="default")
        info_path.write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
        meta.update(input=f.name, provider=prov, model_requested=a.model, attach_mode=mode, seconds=round(time.time() - t0, 1),
                    utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        (out / "_raw" / f"{f.stem}.json").write_text(json.dumps({"meta": meta, "response": raw}, ensure_ascii=False, indent=1), encoding="utf-8")
        if not review.strip():
            print(f"{f.name}: EMPTY ({meta.get('finish_reason') or meta.get('status')}) - see _raw")
            continue
        target.write_text(strip_fence(review), encoding="utf-8")
        ok = "SCORES" in review and "DECISION" in review
        print(f"{f.name}: done [{mode}] ({meta['seconds']}s){'' if ok else ' - WARNING: wrong format'}")
    print("Output directory:", out)


if __name__ == "__main__":
    main()
