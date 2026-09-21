# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled augmentation strategy for contrastive intermediate training that progressively increases augmentation strength (token dropout → synonym replacement → span deletion → back-translation) during the contrastive stage prior to fine-tuning on low-resource text classification tasks. The method is evaluated on SST-2, AG News, TREC, and SUBJ with 500 labelled examples, showing modest but consistent gains over CERT, SimCSE, UDA, and standard fine-tuning.

## Strengths
- The core idea—applying curriculum scheduling to augmentation *strength* specifically within a contrastive intermediate training pipeline—is a clean, well-motivated extension of existing work (CERT, SimCSE) and curriculum learning literature.
- The experimental design is reasonably careful: five random seeds with standard deviations, a stratified low-resource sampling protocol, and consistent baselines.
- The ablations (removing curriculum, reversing curriculum, removing back-translation, removing contrastive stage entirely) are well-chosen and isolate the contribution of the schedule itself rather than just the augmentation operators.
- The scaling analysis across 100/500/1,000 labelled examples is a nice addition that supports the paper's central claim about diminishing returns as labels increase.
- The paper is transparent about limitations (English-only, BERT-base only, hand-designed schedule, reliance on WordNet/MT quality).

## Weaknesses
- The gains over the strongest baseline (CERT) are numerically small (1.1 points average, with per-dataset differences sometimes within one standard deviation), so statistical significance testing (e.g., paired t-tests) would strengthen the claims considerably.
- Only one encoder (BERT-base) and four relatively "easy" benchmarks are tested; generalization to larger models or noisier domains is unverified.
- The curriculum schedule is linear and manually thresholded (0.25/0.5/0.75 cutoffs), and no comparison against other schedule shapes (e.g., exponential, step-based with different breakpoints) is provided beyond the reversed-order ablation.
- Hyperparameter selection procedures for baselines (taken from original papers) versus CurCon (grid-searched) could introduce a slight advantage for the proposed method that is not fully controlled for.
- The 12% training-time overhead, while modest, is not benchmarked against alternative ways of spending that extra compute (e.g., longer fixed-augmentation training).

## Scores

- **Soundness: 72** — The experimental protocol is solid and ablations are informative, but the effect sizes are small relative to variance and lack formal significance testing.
- **Novelty: 60** — The contribution is a targeted, incremental combination of curriculum learning and contrastive intermediate training rather than a fundamentally new mechanism.
- **Significance: 65** — The practical improvement is modest, though the low-resource focus and the demonstrated inverse relationship between gain and label count give it applied relevance.
- **Clarity: 85** — The paper is clearly written, well-organized, and the method, schedule, and experimental setup are described precisely enough to reproduce.

**Average score: 70.5**

## Recommendation: **Accept**

The paper presents a simple, well-motivated, and clearly described method with consistent (if modest) empirical improvements across multiple benchmarks and thoughtful ablations that support its central claims. While the novelty is incremental and the gains are numerically small, the careful experimental design, the informative low-resource scaling analysis, and the honest discussion of limitations make this a solid, useful contribution to the low-resource text classification literature.