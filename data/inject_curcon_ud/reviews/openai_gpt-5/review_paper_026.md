Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It schedules augmentation strength during self-supervised contrastive adaptation on in-domain unlabeled text, progressively introducing stronger operators (token dropout → synonym replacement → span deletion → back-translation). After this intermediate stage, a standard classifier is fine-tuned on limited labeled data. On four sentence-level benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with consistent gains and ablations showing the curriculum (and its direction) materially contributes to improvements. Benefits are larger with fewer labeled examples.

Strengths
- Simple, practical idea that is easy to integrate into existing contrastive intermediate training pipelines.
- Consistent improvements over strong baselines (including CERT and SimCSE) across four datasets, with averages over five seeds and standard deviations reported.
- Clear ablation studies: fixed mixture vs curriculum, reversed curriculum, and operator importance (back-translation).
- Sensible analysis showing gains are larger when labels are scarcer (100 vs 500 vs 1,000 examples).
- No inference-time cost and modest training overhead; clear limitations section.

Weaknesses and concerns
- Baseline fairness: CurCon is tuned via a grid search per dataset, while baselines use their published hyperparameters; this may inflate relative gains. A small, matched tuning budget for baselines would strengthen claims.
- Scope: Only short English datasets and BERT-base are evaluated. Including larger encoders (e.g., RoBERTa-large) or decoder-only LMs would better establish generality.
- Limited exploration of schedule design: Only a linear, thresholded schedule is tested. Sensitivity to curriculum length L and alternative pacing (e.g., nonlinear ramps) is not reported.
- Augmentation details are underspecified for full reproducibility (e.g., which MT system for back-translation, WordNet filtering, exact search space for grid).
- Comparisons could be broadened (e.g., DeCLUTR/ConSERT, supervised contrastive fine-tuning, recent text augmentation strategies), or at least discussed.
- Statistical significance testing is not reported; while means and SDs are given and gains appear consistent, a formal test would solidify conclusions.

Questions and suggestions
- Provide sensitivity plots for curriculum length L and show performance vs. training step as operators become available.
- Report results with matched hyperparameter tuning budgets for baselines or a subset of them.
- Detail the MT system and settings for back-translation, synonym selection criteria, and the grid-search ranges.
- Examine robustness to varying amounts of unlabeled data and to out-of-domain unlabeled corpora.
- Add experiments with a larger encoder and at least one decoder-only model to test generality.
- Consider an adaptive schedule (e.g., based on loss or representation collapse indicators) as an additional ablation.

Reproducibility
- Many key components are described, but exact augmentation implementations and the hyperparameter grid are not fully specified. Public code and preprocessed resources (e.g., BT corpora) would address this.

Scores (0–100)
- Soundness: 82
- Novelty: 74
- Significance: 80
- Clarity: 88

Final average score
- 81.0

Final recommendation
- Accept