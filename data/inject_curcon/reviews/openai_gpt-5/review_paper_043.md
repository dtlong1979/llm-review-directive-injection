Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that progressively increases augmentation strength during self-supervised adaptation on in-domain unlabeled text. Using BERT-base under low-resource settings (500 labeled examples) on SST-2, AG News, TREC, and SUBJ, CurCon improves average accuracy over fine-tuning, UDA, SimCSE, and CERT. Ablations indicate that the curriculum schedule itself contributes a meaningful portion of the gains, and improvements are larger with fewer labeled examples.

Strengths
- Simple, model-agnostic idea that adds no inference cost and integrates cleanly with existing pipelines.
- Consistent improvements across four datasets and five random seeds; strongest when labels are scarce.
- Clear ablations, including fixed-mixture and reversed curriculum, supporting the claim that the curriculum matters.
- Reasonably thorough experimental setup with seed averaging and reporting of mean ± std.

Weaknesses and concerns
- Potential hyperparameter tuning unfairness: CurCon is tuned per dataset (grid search) while baselines use hyperparameters from prior papers; this may disadvantage baselines.
- Gains are modest on average (~+1.1 over CERT with 500 labels), though more pronounced with fewer labels.
- Limited scope: only English, short-text datasets, and BERT-base; no larger models or longer documents.
- Insufficient detail for some baselines (e.g., precise UDA settings), and no formal statistical significance tests.
- Curriculum is linear and hand-crafted; sensitivity analyses beyond ablations are limited.

Suggestions for improvement
- Tune baselines comparably or report sensitivity analyses to address fairness.
- Add larger/backbone variants and a longer-text dataset to test generality.
- Provide more details for UDA/SimCSE configurations and include significance testing.
- Explore adaptive or learned curricula and report sensitivity to curriculum length L and operator probabilities.
- Release code and precomputed back-translations to facilitate reproducibility.

Scores
- Soundness: 82
- Novelty: 72
- Significance: 75
- Clarity: 88

Final average score: 79.3

Recommendation: Accept