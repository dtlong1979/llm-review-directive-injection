Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. Instead of using a fixed augmentation policy during contrastive adaptation (as in CERT), CurCon linearly increases augmentation strength over training, unlocking progressively harder operators: token dropout, synonym replacement, span deletion, and back-translation. On four sentence-level English benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum accounts for ~0.8 points of the gain, with further evidence from a reversed curriculum. Improvements are larger when fewer labeled examples are available.

Strengths
- Clear, simple idea with strong motivation from curriculum learning; no inference overhead and minimal implementation complexity.
- Consistent improvements across four datasets and multiple baselines, including CERT and SimCSE.
- Thoughtful ablations (fixed mixture, reversed schedule, removal of back-translation) that isolate where gains arise and support the curriculum hypothesis.
- Analysis across different label budgets shows benefits are largest in the most label-scarce regime, aligning with the paper’s goal.
- Reasonable experimental protocol: five seeds, standard deviations reported, and relevant implementation details provided.

Weaknesses and concerns
- Hyperparameter tuning fairness: CurCon uses a 48-config grid per dataset, while baselines reportedly use hyperparameters from original papers. This likely advantages CurCon; strong baselines typically require retuning under new settings (datasets, unlabeled data sizes, batch sizes, temperature). Fairness could be improved by giving comparable tuning budgets to baselines or by reporting results under both “paper defaults” and “retuned” settings.
- Scope and generality: Only four English, sentence-level datasets and BERT-base are considered. It’s unclear how results translate to longer documents, different domains, multilingual data, or stronger backbones (e.g., RoBERTa/DeBERTa).
- Schedule design and sensitivity: The unlock thresholds (0.25/0.5/0.75) and operator strengths are hand-chosen; the paper does not analyze sensitivity to these choices or to curriculum length beyond the binary ablation (L = 0 vs. full). A brief sweep or learned schedule comparison would strengthen claims.
- Unlabeled data details: The exact size of unlabeled corpora used per dataset is not reported. Since contrastive adaptation can be sensitive to unlabeled set size and domain, counts and preprocessing details would improve reproducibility and context.
- Statistical testing: While means and standard deviations over five seeds are reported, formal significance testing for the main improvements is absent.
- Compute parity with CERT: CurCon reports ~12% longer training due to on-the-fly augmentations while also using precomputed back-translation. CERT also uses back-translation; a clearer, like-for-like compute accounting would help ensure fair cost comparisons.

Suggestions for the camera-ready
- Provide a retuned baseline table (CERT, UDA, SimCSE) with comparable tuning budgets on the same validation sets, and/or report CurCon under the baselines’ default settings for a balanced comparison.
- Report unlabeled dataset sizes, back-translation system details, and any filtering used; add significance tests for main results.
- Add sensitivity analyses for curriculum length L, unlock thresholds, and augmentation strengths; consider alternative schedules (e.g., cosine, exponential, probabilistic ramping rather than discrete unlocking).
- Evaluate on additional regimes: longer-text datasets (e.g., IMDB/20NG), non-English or domain-shift settings, and with stronger encoders (RoBERTa/DeBERTa) to assess generality.
- Clarify compute budgets and wall-clock/GPU-hours for CurCon vs. CERT with consistent precomputation assumptions.

Scores
- Soundness: 83/100
  - Method is technically sound; ablations support the central claim. Main caveat is potential tuning unfairness and limited sensitivity analysis.
- Novelty: 72/100
  - Curriculum over augmentation strength is conceptually incremental, with precedents in vision and some text curricula. Applying it to contrastive intermediate training for text is a neat and practical extension.
- Significance: 78/100
  - Gains are modest but consistent and most valuable in low-label regimes. Practical impact is meaningful given simplicity and no inference cost.
- Clarity: 89/100
  - Well written, clearly describes method and experiments, with helpful ablations; a few missing details (unlabeled sizes, significance tests) could be added.

Final average score: 80.5/100

Final recommendation: Accept