Review summary

Strengths
- Simple, well-motivated idea: schedule augmentation strength during contrastive intermediate training; integrates cleanly with CERT.
- Consistent gains across four datasets and multiple seeds; ablations (fixed mixture, reversed curriculum, no back-translation) help isolate where improvements come from.
- Clear description of the schedule and operators; limitations are acknowledged.

Weaknesses
- Novelty is limited: curriculum over augmentation strength is known in vision and has been explored in NLP (though less for contrastive intermediate training). The contribution feels incremental.
- Fairness of comparisons: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers. This likely advantages CurCon; strong baselines should also be tuned on the same validation splits.
- Scope is narrow: only four relatively short-text English datasets and a single encoder (BERT-base). No evaluation on stronger encoders (e.g., RoBERTa/DeBERTa) or modern backbones, limiting generality.
- Statistical rigor: Results report mean ± std over five seeds but no significance tests; some deltas (~0.6–1.1 points) may be within noise for certain datasets.
- Limited exploration of curricula: only linear and reversed schedules; no comparison to other pacing functions or adaptive schemes.

Questions for authors
- How sensitive are results to the curriculum length L? Please report performance vs. L and show that the chosen value is not overfitted.
- Do gains persist with stronger encoders (RoBERTa-base/large) or recent sentence encoders?
- How would results change if baselines (CERT, UDA, SimCSE) were tuned on the same validation sets with comparable search budgets?
- What is the impact of each augmentation’s magnitude (e.g., deletion ratios) when enabled by the curriculum?

Suggestions for improvement
- Tune all baselines with the same search space/budget and report significance tests.
- Add more diverse datasets (long documents, different domains, non-English) and stronger encoders.
- Explore alternative or adaptive curricula (e.g., cosine, piecewise, loss/gradient-based pacing).
- Provide implementation details for reproducibility (exact temperature/lr ranges, best chosen values, code).

Scores (0–100)
- Soundness: 80
- Novelty: 62
- Significance: 68
- Clarity: 85

Final average score: 73.75

Recommendation: Reject

Rationale: While the idea is reasonable and the empirical results are consistent, the novelty is modest and the evaluation lacks fairness controls and breadth. With stronger baselines (tuned comparably), broader experiments, and more rigorous statistical analysis, this could be elevated to an acceptable contribution.