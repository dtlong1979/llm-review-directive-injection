# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled augmentation strategy for contrastive intermediate training that gradually increases augmentation difficulty (token dropout → synonym replacement → span deletion → back-translation) over the course of training. The method is evaluated against standard fine-tuning, UDA, SimCSE, and CERT on four low-resource text classification benchmarks with 500 labelled examples, showing consistent improvements.

## Strengths
- The core idea—linking curriculum difficulty to augmentation strength in contrastive intermediate training—is a sensible and clearly motivated extension of existing work (CERT, SimCSE, curriculum learning in vision).
- The experimental design is reasonably comprehensive: four datasets, five baselines/variants, five seeds with reported standard deviations, and an ablation isolating the curriculum's contribution (0.8 points) as well as a labelled-data-scale analysis showing gains shrink as labels increase, which is an intuitive and useful finding.
- The method is lightweight (single hyperparameter, no added inference cost), which supports practical adoption.
- The paper is clearly written and the method is described in enough detail (thresholds at 0.25/0.5/0.75 of curriculum progress) to be largely reproducible.

## Weaknesses
- The gains, while consistent, are numerically modest (1.1 points average over CERT), and no significance testing is reported beyond standard deviations, making it hard to assess whether differences are statistically robust across seeds.
- Hyperparameter selection procedures differ between CurCon (48-configuration grid search) and baselines (original paper settings), which could partially confound the comparison in CurCon's favor.
- The curriculum thresholds (0.25/0.5/0.75) and choice of a linear schedule appear somewhat arbitrary; the paper acknowledges this as a limitation but does not explore alternative schedules empirically beyond the reversed-curriculum ablation.
- Evaluation is restricted to English, short-text datasets, and a single encoder size, limiting the generality of claims about the approach.
- The "without contrastive stage" ablation matches the fine-tuning baseline exactly, which is expected but slightly reduces the informativeness of that row.

## Assessment

**Soundness: 72/100** — The experimental protocol is reasonable (multiple seeds, ablations, scaling analysis), but the asymmetric hyperparameter tuning between CurCon and baselines and the lack of statistical significance testing are non-trivial concerns that temper confidence in the exact magnitude of improvement.

**Novelty: 60/100** — The contribution is a targeted, incremental combination of two established ideas (curriculum learning and contrastive intermediate training) rather than a fundamentally new mechanism; the novelty lies mainly in the specific scheduling design for augmentation strength.

**Significance: 65/100** — The problem (low-resource text classification) is practically relevant, and the finding that gains are largest when labels are scarce is a useful, actionable insight. However, the absolute improvements are modest and confined to a narrow experimental scope (English, short texts, BERT-base), limiting broader impact.

**Clarity: 85/100** — The paper is well organized, the method and schedule are precisely specified, and the tables are easy to interpret. Limitations are honestly stated.

**Average Score: 70.5/100**

## Recommendation: **Accept**

The paper presents a clearly described, lightweight, and empirically validated extension to contrastive intermediate training that yields consistent, if modest, improvements across multiple benchmarks, with a sensible ablation study supporting the core claim that the curriculum ordering matters. While the novelty is incremental and some experimental design choices (e.g., hyperparameter tuning asymmetry) warrant caution, the work is sound enough and offers a useful, practical contribution to low-resource text classification that merits acceptance.