# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which applies a linear curriculum schedule to augmentation strength during contrastive intermediate training (before fine-tuning on labelled data), progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four text classification benchmarks (500 labels each) show improvements over fine-tuning, UDA, SimCSE, and CERT baselines.

## Strengths
- The core idea—scheduling augmentation difficulty in a contrastive intermediate-training setting—is a reasonable and underexplored combination of two established ideas (curriculum learning + contrastive intermediate training).
- The paper includes ablations isolating the curriculum's contribution (0.8 points), a reversed-curriculum control (which meaningfully underperforms), and a labelled-data-scarcity analysis, which is good experimental hygiene.
- The method is simple, requires no architecture changes, and adds no inference cost, which is appealing for practical adoption.
- Writing is generally clear and the pipeline is described in enough detail to (mostly) reproduce.

## Weaknesses

**Soundness concerns:**
- No confidence intervals or significance testing are reported for the main comparisons despite averaging over five seeds and having standard deviations available; several reported gaps (e.g., 0.5–0.6 points) are within or close to one standard deviation, making claims of consistent superiority questionable.
- Hyperparameters for CurCon were selected via a 48-configuration grid search, whereas baselines used values "reported in their original papers." This is a significant asymmetry that could account for some or all of the improvement, rather than the curriculum itself.
- Only one random split methodology is described (stratified 500 examples), but details on validation set construction and how sensitive results are to the particular 500-example sample are unclear.
- No comparison to a "SimCSE + curriculum" or "CERT + curriculum" style control that isolates whether the benefit is curriculum-specific versus simply from more careful/extended hyperparameter tuning of the schedule length L.

**Novelty concerns:**
- The technical contribution is a fairly straightforward application of curriculum scheduling (well established in vision, e.g., progressively increasing augmentation strength) to an existing pipeline (CERT). The four augmentation operators are all pre-existing (dropout, WordNet synonym replacement, span deletion, back-translation). The novelty is essentially in the scheduling heuristic and its application to a known intermediate-training recipe.
- No comparison to alternative non-linear or adaptive schedules beyond a linear one and its reversal, despite the limitations section itself noting the schedule is "hand-designed."

**Significance concerns:**
- Gains are modest (1.1 points average over the strongest baseline) and shrink further as labelled data increases (0.5 points at 1,000 examples), suggesting limited practical impact outside a narrow low-resource band.
- Evaluated only on BERT-base and four fairly standard, well-worn English benchmarks with short texts; generalization to other encoders, languages, or domains is untested (acknowledged in limitations).
- The added training cost (12%) is modest but non-trivial for what appears to be a relatively small accuracy gain.

**Clarity issues:**
- The exact curriculum thresholds (0.25, 0.5, 0.75) are stated but not justified or ablated—it's unclear if performance is sensitive to these boundaries.
- The paper does not report the selected curriculum length L or how it varies across datasets, which would help readers understand the practical range of this hyperparameter.
- No qualitative or representation-level analysis (e.g., embedding visualization, alignment/uniformity metrics common in contrastive learning literature) is given to support the mechanistic claim that curriculum improves representation quality rather than just providing more effective regularization/tuning.

## Scores

| Criterion | Score |
|---|---|
| Soundness | 55 |
| Novelty | 45 |
| Significance | 50 |
| Clarity | 70 |

**Average: 55**

## Recommendation: **Reject**

While the paper addresses a reasonable and practically motivated question with a clean experimental design and honest limitations section, the core contribution is incremental (curriculum scheduling applied to an existing intermediate-training pipeline), the hyperparameter tuning asymmetry between CurCon and baselines undermines the soundness of the comparison, and the magnitude of improvement is modest and shrinks with more labelled data. Stronger controls (matched tuning budgets across methods, statistical testing, ablation of schedule shape/thresholds, and testing beyond BERT-base) would be needed to support the claims at a level suitable for acceptance.