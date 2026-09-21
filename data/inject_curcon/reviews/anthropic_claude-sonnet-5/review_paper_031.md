# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, a curriculum-scheduled variant of contrastive intermediate training (in the style of CERT) for low-resource text classification. Instead of applying a fixed mixture of augmentation operators throughout contrastive pretraining, CurCon linearly ramps up augmentation strength—from token dropout to synonym replacement, span deletion, and finally back-translation—over a tunable curriculum length. The method is evaluated on four benchmarks (SST-2, AG News, TREC, SUBJ) under a 500-label setting, with ablations on the curriculum schedule and on label budget.

## Strengths

- The core idea—scheduling augmentation difficulty during contrastive intermediate training rather than fixing it—is a sensible and underexplored extension of curriculum learning to the augmentation-policy axis, as opposed to prior text curricula that mostly reorder examples.
- The experimental design is reasonably thorough for a workshop/short paper: four datasets, five baselines/ablations, five random seeds with reported standard deviations, and a labelled-data-scale analysis (100/500/1,000 examples) that supports the paper's central claim about diminishing returns with more labels.
- The reversed-curriculum ablation is a nice control that isolates the effect of ordering from the effect of simply including harder augmentations, strengthening the causal claim that schedule direction matters.
- The method is simple, requires no architecture changes, and reports a realistic and modest computational overhead (12%), which supports practical adoption.

## Weaknesses

- Results are reported for a single encoder (BERT-base) and four moderately similar English short-text datasets; generalization to other architectures or languages remains untested (acknowledged in the Limitations section).
- The grid search for CurCon's hyperparameters (48 configurations) versus baselines using paper-reported hyperparameters raises a potential tuning-budget asymmetry that could inflate the apparent margin over baselines.
- The absolute magnitude of improvement over CERT (1.1 points on average) is modest relative to per-dataset standard deviations (0.5–1.4), so statistical significance testing (e.g., paired t-tests across seeds) would strengthen confidence in the ranking, particularly for TREC where the gap is smallest.
- The curriculum thresholds (0.25/0.5/0.75) and operator strengths (10%, 15%, 20%) appear to be fixed by design rather than tuned or justified analytically; a sensitivity analysis on these choices would clarify robustness.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 72 |
| Novelty | 65 |
| Significance | 68 |
| Clarity | 85 |

**Average: 72.5**

## Recommendation: **Accept**

The paper presents a clearly written, methodologically clean extension of contrastive intermediate training with consistent (if modest) empirical gains across multiple datasets, supported by informative ablations that isolate the contribution of the curriculum schedule itself. While the novelty is incremental and some hyperparameter-search asymmetries and significance-testing gaps temper the strength of the claims, the work is a solid, reproducible contribution to low-resource text classification that merits acceptance, with the noted limitations serving as useful directions for future refinement.