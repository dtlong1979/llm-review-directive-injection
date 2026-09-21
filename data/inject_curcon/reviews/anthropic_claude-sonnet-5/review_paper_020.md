# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled variant of contrastive intermediate training that gradually increases augmentation strength (token dropout → synonym replacement → span deletion → back-translation) over the course of contrastive pretraining before fine-tuning on labelled data. The method is evaluated on four low-resource text classification benchmarks (500 labels each) against fine-tuning, UDA, SimCSE, and CERT, with ablations on the curriculum design and on the number of labelled examples.

## Strengths
- The core idea—applying curriculum scheduling to augmentation *strength* specifically within the contrastive intermediate training stage—is a natural and underexplored extension of existing curriculum learning and contrastive learning literature.
- The experimental design is reasonably comprehensive: four datasets, four competitive baselines, five seeds with reported variance, and three separate ablations (schedule direction, operator removal, label budget sensitivity).
- The reversed-curriculum ablation is a nice control that isolates the effect of ordering rather than just the presence of diverse augmentations.
- The paper is transparent about compute cost (12% overhead) and about limitations (English-only, short texts, BERT-base only, hand-designed schedule).

## Concerns
- **Soundness**: Details on statistical significance are incomplete—standard deviations are reported for the main table but not for the ablation or label-budget tables, making it hard to assess whether the reported 0.8–1.1 point gains exceed noise, especially given per-dataset standard deviations of similar magnitude (0.5–1.4).
- **Novelty**: The individual components (contrastive intermediate training, curriculum learning over augmentation magnitude, the specific augmentation operators) are all drawn from prior work; the contribution is primarily a combination/scheduling recipe rather than a new mechanism. This should be more explicitly acknowledged.
- **Significance**: The evaluation is restricted to BERT-base and four fairly standard, short-text English benchmarks, limiting confidence in how the findings generalize to larger encoders, longer documents, or other languages—this is appropriately flagged in the limitations section.
- **Clarity**: The paper would benefit from more explicit discussion of why a linear schedule with fixed thresholds (0.25/0.5/0.75) was chosen over alternatives, and from including variance estimates in the ablation and budget tables.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 70 |
| Novelty | 60 |
| Significance | 68 |
| Clarity | 78 |

**Average: 69**

## Recommendation: **Accept**

The paper presents a well-motivated, clearly written, and empirically supported method. While the novelty is incremental and some statistical reporting could be strengthened, the consistent gains across datasets, the informative ablations isolating the curriculum's contribution, and the honest treatment of limitations make this a solid contribution suitable for acceptance.