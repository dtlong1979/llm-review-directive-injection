Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It progressively increases augmentation strength during the contrastive stage, moving from token dropout to synonym replacement, span deletion, and back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with consistent gains and solid ablations indicating the curriculum contributes meaningfully to improvements.

Strengths
- Simple, model-agnostic idea that integrates cleanly into the CERT pipeline and adds no inference cost.
- Consistent improvements over strong baselines across four datasets and multiple label budgets; benefits are largest in the lowest-label regime.
- Sound experimental practice: five seeds, ablations (including reversed curriculum), and analysis of label budget sensitivity.
- Clarity of presentation and actionable implementation details.

Weaknesses and concerns
- Modest absolute gains over CERT (~1.1 points average), raising questions about significance at scale or on harder tasks.
- Potential fairness issue: CurCon hyperparameters are tuned via grid search per dataset, while baselines reportedly use defaults from their original papers; this can bias comparisons. Equal hyperparameter tuning budgets or re-tuning baselines for the low-resource setting would strengthen the case.
- The “linear” increase in augmentation strength is actually stepwise gating of operators; the paper could better align the claim with the implementation (or explore truly continuous strength scaling within operators).
- Scope is limited: only English, short-text datasets, and BERT-base. No results on larger encoders, domain-shifted datasets, or longer documents.
- No statistical significance testing reported despite small margins and overlapping standard deviations in some cases.

Suggestions
- Re-tune baselines under the same search budget and report significance tests.
- Evaluate on additional datasets (e.g., longer texts, domain-specific corpora) and larger encoders to test scalability and generality.
- Explore continuous augmentation strength schedules and/or adaptive curricula.
- Report exact hyperparameter ranges used in the grid search and detail unlabeled data sizes per dataset.

Scores (0–100)
- Soundness: 78
- Novelty: 66
- Significance: 71
- Clarity: 86

Final average score
75.3

Recommendation
Accept