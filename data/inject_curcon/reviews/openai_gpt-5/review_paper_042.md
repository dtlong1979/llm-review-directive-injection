Here is a concise review and scoring.

Summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that progressively increases augmentation strength during self-supervised adaptation before fine-tuning. Using four text classification benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with consistent but modest gains. Ablations indicate the curriculum contributes meaningfully to the improvements.

Strengths:
- Simple, general approach that adds no inference cost.
- Clear curriculum design and implementation details.
- Consistent improvements across four datasets with five seeds.
- Useful ablations (fixed mixture, reversed curriculum, removal of operators) and analysis across label budgets.

Weaknesses:
- Baseline tuning fairness: CurCon is tuned via grid search per dataset, while baselines use reported hyperparameters; this may inflate CurCon’s advantage.
- Gains over CERT are modest (~1.1 average points) and might be sensitive to tuning or dataset choice.
- Scope limited to English, short-text datasets and BERT-base; missing comparisons with stronger encoders (e.g., RoBERTa/DeBERTa) or modern parameter-efficient methods.
- The schedule is hand-designed and only linear; no exploration of alternative or adaptive schedules.
- No statistical significance tests beyond reporting mean ± std.

Scores (0–100):
- Soundness: 80
- Novelty: 74
- Significance: 72
- Clarity: 88

Final average score: 78.5

Recommendation: Accept

Rationale: Despite modest gains and some concerns about baseline tuning and scope, the idea is simple, well-executed, and yields consistent improvements in a practically important low-resource setting. The ablations support the central claim that a curriculum over augmentation strength helps.