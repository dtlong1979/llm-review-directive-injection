# Artifact: a legitimate-sounding directive in LLM peer review

This artifact reproduces the experiments in the paper. It contains the code that
built and ran every study, the verbatim payloads and prompts, and the model outputs
behind every reported table and figure. No real submission was scored at any point;
all manuscripts are synthetic carriers written to be weak.

> WARNING. `PAYLOADS.md`, the builder scripts, and the `key.csv` files contain live
> injection strings that instruct a reviewing model to accept a paper. Do not feed
> this artifact, or any manuscript built from it, to a reviewing pipeline or an
> assistant you rely on. The strings exist only to reproduce the study.

## Layout

- `PROMPTS.md` - every prompt used, verbatim (review request, defences, sanitiser
  detector, two-pass extractor and scorer).
- `PAYLOADS.md` - the injected sentences, verbatim, with a warning.
- `carriers/` - the synthetic weak papers used as manuscripts: the three main
  carriers (text classification, clinical, recommender) and the six confirmation
  fields. The builders read these automatically (via `styles.py`) and append a
  payload to make each input.
- `code/` - the runner and the builders and pipelines:
  - `run_api_review.py` - sends one review per input across the three provider APIs
    (attached-document or inline delivery, optional system prompt, PDF support).
  - `carriers.py`, `gen_carriers.py` - the synthetic weak-paper carriers.
  - `make_inject_multi.py` - builds the cross-vendor map inputs (clean, crude,
    directive) for a carrier.
  - `make_inject_lead.py` - inline positions and the directive vs a crude control.
  - `make_inject_pdf.py` - the PDF hiding inputs (visible vs invisible text).
  - `make_inject_para.py` - the matched-paraphrase ablation.
  - `make_inject_warn.py` - the identical warning placed in the user vs system role.
  - `sanitize_build.py` - detect-and-delete sanitiser (a detector call lists
    reviewer-directed sentences; code deletes them by exact match).
  - `build_twopass.py` - two-pass bottleneck (extract a neutral digest, then score
    only the digest).
- `data/<experiment>/` - for each reported experiment:
  - `key.csv` - maps each input file to its condition and payload.
  - `prompt_review.txt` - the review request used (when not embedded in the input).
  - `reviews/<model>/` - the model's review for every input (raw text output).
  - `results.csv` - automated Accept/Reject/empty/no-decision counts per condition.

Each experiment folder names the table or figure it supports; see the mapping in
`data/INDEX.md`.

## Outcome extraction

`results.csv` is produced by an automated parser that reads the final
recommendation. For most vendors this agrees with a manual read. For one vendor the
free-form reviews quote the injected sentence, which defeats keyword extraction, so
the corresponding cells in the paper were read by hand; the raw reviews are included
so any count can be re-checked. Empty or decision-free outputs are reported as such
and are counted as neither Accept nor Reject.

## Reproducing

1. Python 3.10+ with `requests`.
2. Provide API keys in a `.env` file at the repository root:
   `OPENAI_API_KEY=...`, `GEMINI_API_KEY=...`, `CLAUDE_API_KEY=...`.
3. From the repository root, build a study's inputs, for example the
   matched-paraphrase ablation (writes to `experiments/inject_para/`, which is
   git-ignored):
   `python -X utf8 code/make_inject_para.py 8 7`
4. Run a model over it:
   `python -X utf8 code/run_api_review.py --exp inject_para --provider openai --model <id> --max-calls 90`
   Each builder script states its own arguments in its module docstring.

Model identifiers, sampling settings, and run dates are listed in the paper's
supplementary material. Sampling uses each provider's defaults; outputs are
therefore stochastic and exact counts may vary run to run.
