# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which applies a linear curriculum schedule to augmentation strength during contrastive intermediate training (building on CERT), progressing from token dropout to synonym replacement, span deletion, and back-translation. Evaluated on four low-resource text classification benchmarks (500 labels/dataset), CurCon shows modest but consistent improvements over CERT, UDA, SimCSE, and fine-tuning baselines.

## Strengths
- The core idea—scheduling augmentation difficulty in contrastive intermediate training rather than using a fixed policy—is a reasonable and underexplored extension of curriculum learning to the augmentation dimension.
- The experimental design is appropriately scoped: multiple baselines, multiple datasets, seed averaging, and ablations (reversed curriculum, no curriculum, no back-translation, no contrastive stage) that isolate the claimed contribution.
- The additional experiment varying labelled-example count (100/500/1000) is a nice touch that supports the motivating claim about low-resource benefit.
- The method is simple, requires no architecture changes, and adds no inference-time cost.

## Weaknesses

**Soundness concerns:**
- No confidence intervals or significance testing are reported for the 1.1-point average gain over CERT; given per-dataset standard deviations of ~0.6–0.9, several individual gains (e.g., TREC +0.6) are not clearly distinguishable from noise.
- The claim that "curriculum contributes 0.8 points" rests on a single ablation configuration (L=0) without exploring sensitivity to L, batch composition, or interaction with dataset difficulty.
- Hyperparameters for CurCon are tuned via a 48-config grid search on validation sets, while baselines use published hyperparameters — this asymmetry in tuning effort could inflate CurCon's advantage.
- No details are given on the back-translation quality, WordNet coverage for domain-specific terms, or variance from the MT system itself, despite these being central to the "hardest" augmentation level.

**Novelty concerns:**
- The contribution is an incremental combination of two established ideas (contrastive intermediate training via CERT, and curriculum-by-augmentation-strength from vision literature) rather than a fundamentally new mechanism. The paper itself acknowledges this lineage.
- The curriculum schedule (fixed linear thresholds at 0.25/0.5/0.75) is simple and hand-tuned; no comparison to alternative non-linear schedules (e.g., exponential, cosine) is provided.

**Significance concerns:**
- Absolute gains are modest (1.1 points average over the strongest baseline), and the paper does not discuss whether this justifies the added complexity (curriculum length as an extra hyperparameter, 12% training overhead, back-translation infrastructure).
- Only BERT-base is evaluated; the paper explicitly notes it hasn't tested larger encoders or decoder-only models, which limits confidence that findings generalize to current-generation architectures where intermediate contrastive training may behave differently.
- Datasets are limited to English, short-text classification; the claimed benefit for low-resource settings is not tested outside this narrow scope.

**Clarity issues:**
- The augmentation probability scheme ("when multiple operators are available, one is sampled uniformly") could be stated more precisely with pseudocode, especially regarding token dropout's role after level thresholds are crossed.
- The paper does not report where L is set for the final model, nor its sensitivity — an important missing implementation detail.
- Table 3 lacks per-dataset breakdowns, making it hard to assess whether the label-count effect uniformly holds or is driven by one dataset.

## Scores

| Criterion | Score | Justification |
|---|---|---|
| **Soundness** | 60 | Reasonable experimental protocol but lacks statistical testing, hyperparameter-tuning parity between methods, and sensitivity analysis on the key novel hyperparameter (L). |
| **Novelty** | 45 | Incremental combination of curriculum learning and existing contrastive intermediate training; conceptually plausible but not a substantial methodological advance. |
| **Significance** | 50 | Modest, consistent gains in a narrow (English, short-text, BERT-base) setting; unclear whether benefits persist with larger models or scale of labelled data. |
| **Clarity** | 70 | Generally well-organized and readable, but missing some implementation specifics (final L value, sensitivity, augmentation sampling precision). |

**Average Score: 56.25 / 100**

## Recommendation: **Reject** (borderline/weak reject)

The paper presents a sensible and clearly-described idea with supportive ablations, but the modest effect sizes, lack of statistical rigor, asymmetric hyperparameter tuning between CurCon and baselines, and narrow experimental scope (single encoder, English-only, short texts) limit confidence in the robustness and generality of the claimed improvements. The work would benefit from significance testing, broader model/language coverage, and a more thorough exploration of the curriculum design space before publication at a top venue.