# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled augmentation strategy for contrastive intermediate training that progressively increases augmentation strength (token dropout → synonym replacement → span deletion → back-translation) during the contrastive stage prior to fine-tuning. Experiments on four low-resource text classification benchmarks (500 labels each) show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with ablations isolating the contribution of the curriculum ordering.

## Strengths
- The idea is simple, well-motivated by curriculum learning literature, and cleanly integrated into an existing pipeline (CERT) without added inference cost.
- The experimental design directly targets the claimed contribution: the reversed-curriculum ablation is a strong and convincing control that isolates the effect of *ordering* rather than just the augmentation mixture, and the L=0 ablation isolates the curriculum itself from the augmentation set.
- The analysis of gains across different labelled-data sizes (100/500/1000) is a sensible robustness check and supports the paper's central claim that representation quality matters most in low-resource regimes.
- Reporting mean ± std over five seeds is good practice for a low-resource setting where variance is typically high.

## Weaknesses
- Results are reported on only four datasets, all English and relatively short-text; generalization to longer documents, other languages, or other architectures is untested (acknowledged in Limitations).
- The paper does not report statistical significance tests (e.g., paired t-tests) despite providing standard deviations, which would strengthen claims that the ~1.1 point average gain over CERT is meaningful given overlapping error bars on some datasets (e.g., TREC: 90.8±0.9 vs 90.2±0.7).
- Hyperparameter search for CurCon (48 configurations) is more extensive than for baselines (taken from original papers), which could partly inflate the apparent advantage; a matched-budget comparison would be more rigorous.
- The added 12% training-time cost and dependency on external resources (WordNet, MT system) are reasonable trade-offs but not deeply analyzed in terms of practical deployment cost.
- The novelty is incremental — applying curriculum scheduling to an existing augmentation set within an existing pipeline (CERT) — rather than a fundamentally new mechanism, though the empirical validation is solid.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 74 |
| Novelty | 60 |
| Significance | 68 |
| Clarity | 85 |

**Average: 71.75**

## Recommendation: **Accept**

The paper presents a clear, well-executed, and reproducible empirical study. While the core idea is an incremental extension of curriculum learning to contrastive augmentation scheduling rather than a conceptually new method, the experiments are carefully designed with appropriate ablations (particularly the reversed-curriculum control) that convincingly support the central claim. The consistent gains across four benchmarks and the sensible trend across labelled-data sizes make the contribution useful and credible to the community, notwithstanding the noted limitations around statistical testing and matched hyperparameter budgets, which the authors should address in a revision.