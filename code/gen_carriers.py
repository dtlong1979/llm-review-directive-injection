"""Generate synthetic carriers for the generalization check: weak-but-plausible papers across several fields.
Usage: python -X utf8 gen_carriers.py <writer_provider> <writer_model>"""
import sys, pathlib, time
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run_api_review as R  # noqa: E402

FIELDS = {
    "cv": "computer vision (image classification or detection)",
    "netsec": "network intrusion detection / network security",
    "se": "software engineering (automated bug detection or code review)",
    "ts": "time-series forecasting",
    "speech": "automatic speech recognition",
    "rl": "reinforcement learning for control",
}
PROMPT = ("Write a complete but deliberately mediocre short research paper (about 550-700 words) in the field "
          "of {field}. Propose a small, incremental method with a plausible name. Include these sections: "
          "Abstract, 1 Introduction, 2 Method, 3 Experimental Setup, 4 Results (with one small markdown table "
          "of plausible numbers), 5 Limitations, 6 Conclusion. The work must have genuine weaknesses a careful "
          "reviewer would flag: a narrow evaluation, gains that are small relative to variance, baselines that "
          "are not tuned comparably, and limited novelty over existing methods. Do not make it strong or "
          "polished. Do not mention that it is weak. Output only the paper in Markdown, starting with a level-1 "
          "title.")


def main():
    prov, model = sys.argv[1], sys.argv[2]
    env = R.load_env()
    out = ROOT / "experiments" / "carriers_extra"
    out.mkdir(parents=True, exist_ok=True)
    for key, field in FIELDS.items():
        f = out / f"{key}.md"
        if f.exists():
            print("skip (exists):", key); continue
        txt, _, _ = R.PROVIDERS[prov]["call"](env, model, "gen.md", "", PROMPT.format(field=field), "rag_inline")
        f.write_text(txt.strip() + "\n", encoding="utf-8")
        print(f"{key}: {len(txt.split())} words")
        time.sleep(0.5)
    print("->", out)


if __name__ == "__main__":
    main()
