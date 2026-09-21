Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, starting with mild token-level perturbations and ending with aggressive back-translation and span deletion. Evaluations on four benchmarks with 500 labeled examples show consistent gains over strong baselines (CERT, SimCSE, UDA) with ablations demonstrating that the curriculum itself contributes a meaningful portion of the improvement. Gains are largest when labeled data are scarcest.

Strengths
- Simple, model-agnostic idea that plugs into the widely used CERT pipeline; no inference-time overhead.
- Consistent improvements across four datasets and five seeds, with clear reporting of means and standard deviations.
- Solid ablations: fixed mixture vs. curriculum, reversed curriculum, removal of back-translation; results support the central claim that curriculum order matters.
- Analysis across varying label budgets (100, 500, 1,000) shows the method’s utility in the intended low-resource regime.
- Implementation details are sufficient to reproduce the approach in spirit (operators, schedule, contrastive setup).

Weaknesses and concerns (minor)
- Modest absolute gains (≈1.1 points over CERT on average); still valuable but incremental.
- Baseline tuning fairness: CurCon uses a grid search (48 configs per dataset), while baselines rely on hyperparameters from their papers; re-tuning baselines for the exact low-resource setting could narrow gaps.
- Limited scope: only English, short-text datasets, and BERT-base. No evaluation on larger or more modern encoders (e.g., RoBERTa, DeBERTa) or decoder-only backbones.
- Reliance on external resources (WordNet, MT for back-translation); generality to other languages/domains may vary, and the offline MT cost is not accounted for in the reported “12% longer” training time.
- The curriculum is hand-designed and linear; no exploration of learned or adaptive schedules beyond a reversed baseline.

Suggestions for improvement
- Re-tune baselines under the same search budget to solidify the strength of the claim.
- Include results with at least one larger encoder and one non-English dataset to test generality.
- Report or discuss the offline cost of generating back-translations and assess the impact of using paraphrasers or multilingual/backbone-agnostic augmenters.
- Explore adaptive or learned curricula and provide sensitivity analysis for curriculum length L.
- Add significance testing for main results.

Scores (0–100)
- Soundness: 85
- Novelty: 74
- Significance: 80
- Clarity: 89

Final average score: 82.0

Final recommendation: Accept