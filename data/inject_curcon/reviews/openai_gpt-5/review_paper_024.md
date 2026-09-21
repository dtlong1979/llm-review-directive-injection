Here is my review.

Summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that gradually increases augmentation strength during contrastive adaptation on in-domain unlabeled text before fine-tuning. It shows consistent gains over strong baselines (CERT, SimCSE, UDA, and standard fine-tuning) on four low-resource text classification benchmarks with 500 labeled examples, with ablations indicating the curriculum contributes a meaningful portion of the improvement.

Strengths:
- Clear motivation for scheduling augmentation strength in contrastive intermediate training.
- Consistent improvements across multiple datasets and seeds; ablations isolate contributions of the curriculum and components (e.g., back-translation).
- Sensible analysis of performance vs. labeled data size.
- Method is simple to implement and adds no inference-time cost.

Weaknesses:
- Incremental novelty: curriculum over augmentation strength is conceptually straightforward and has analogues in prior work (especially in vision); the contribution is more about applying and validating it in this setting.
- Modest absolute gains over CERT (+1.1 average), with only 0.8 attributable to the curriculum vs. a fixed mixture—valuable but not groundbreaking.
- Potential fairness issue in hyperparameter tuning: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers, which may disadvantage baselines in this specific low-resource setup.
- Evaluation scope is limited: only English, relatively short-text datasets, one encoder (BERT-base). Results on larger models or more diverse domains would strengthen the case.
- No statistical significance testing beyond reporting mean ± std; significance tests would help substantiate the claims.

Questions/Comments:
- How sensitive are results to the exact thresholds at which operators “unlock”? An ablation varying these thresholds would clarify robustness.
- How does CurCon compare to a continuous mixing strategy that smoothly scales augmentation strengths within each operator rather than unlocking operators discretely?
- Could an adaptive schedule based on validation loss or contrastive agreement outperform the fixed linear schedule?

Scores (0–100):
- Soundness: 78
- Novelty: 65
- Significance: 70
- Clarity: 88

Final average score: 75.25

Recommendation: Reject

Rationale: While the paper is well-written and the idea is practical with consistent gains, the novelty is incremental, the improvements over the strongest baseline are modest, and the evaluation/tuning setup raises fairness concerns. Strengthening the empirical evaluation (broader datasets and models, stronger fairness in tuning across methods, significance tests) and exploring adaptive or learned curricula would make the contribution more compelling for acceptance.