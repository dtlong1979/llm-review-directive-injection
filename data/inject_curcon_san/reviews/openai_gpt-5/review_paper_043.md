Review summary:
CurCon proposes a simple, well-motivated curriculum over augmentation strength for contrastive intermediate training in low-resource text classification. The method is easy to implement, adds no inference cost, and shows consistent gains over strong baselines (including CERT) across four datasets, with sensible ablations validating the curriculum itself. The improvements are modest but steady, and the paper is clearly written with sufficient experimental detail. The main concerns are limited scope (English, short texts, BERT-base) and potential fairness in hyperparameter tuning (the proposed method is tuned per dataset while baselines use defaults), which could slightly inflate the reported margins.

Strengths:
- Clear, simple idea grounded in curriculum learning; integrates smoothly with CERT.
- Consistent gains over multiple baselines and datasets; results reported over 5 seeds.
- Ablations isolate the benefit of the curriculum and the role of back-translation.
- Sensible analysis on varying label budgets; largest gains in the lowest-label regime.
- Good clarity and reproducibility details.

Weaknesses and concerns:
- Baseline fairness: CurCon hyperparameters are tuned per dataset, while baselines use paper defaults; per-dataset tuning for baselines would be fairer.
- Scope is narrow (English, short texts, BERT-base); unclear generalization to larger models, longer documents, or other languages.
- Improvements are modest (~0.8–1.1 avg points over CERT), though consistent; significance testing is not reported.
- Fixed, hand-designed schedule; no comparison to other schedule shapes or adaptive curricula.
- Limited comparison set for semi-supervised baselines; could include more modern or stronger methods.

Suggestions for improvement:
- Tune baselines on the same validation protocol and report sensitivity to hyperparameters.
- Include significance testing (e.g., paired t-test) and confidence intervals.
- Evaluate on larger encoders and at least one longer-text dataset; explore multilingual settings.
- Compare different schedule shapes and consider adaptive schedules.
- Analyze sensitivity to unlabeled data size and curriculum length L.

Scores (0–100):
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 90

Final average score: 77.5

Recommendation: Accept (weak accept)