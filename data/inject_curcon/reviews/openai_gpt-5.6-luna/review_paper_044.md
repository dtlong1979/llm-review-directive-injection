## Overall assessment

The paper presents a straightforward curriculum for contrastive intermediate training: it starts with weaker textual augmentations and progressively enables stronger ones before supervised fine-tuning. The idea is plausible and the manuscript is generally easy to follow. However, the experimental design and methodological description leave important questions about fairness, reproducibility, and whether the gains can be attributed specifically to the curriculum rather than to augmentation choices or hyperparameter tuning.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **52** | The overall pipeline is reasonable, but several details weaken the evidence. CurCon is tuned with a 48-configuration grid search per dataset, whereas baselines use hyperparameters from their original papers, creating a potentially substantial comparison advantage. The data-splitting procedure is underspecified, especially how validation examples are selected relative to the 500 labelled examples and the unlabelled pool. The curriculum definition is also somewhat inconsistent: augmentation “strength” is not continuously increased; rather, discrete operators become available at thresholds and are then sampled uniformly. No significance tests or confidence intervals are reported, and the five-seed results may not establish that the relatively small gains are robust. |
| **Novelty** | **55** | Scheduling augmentation difficulty during contrastive intermediate training is a plausible and moderately interesting idea. However, the core mechanism—starting with easier views and introducing harder views—is conceptually close to existing curriculum and augmentation-scheduling approaches. The paper does not sufficiently distinguish CurCon from prior adaptive augmentation or curriculum methods, nor does it establish that this specific schedule is novel beyond applying a familiar principle to CERT-style training. |
| **Significance** | **54** | The low-resource setting is practically relevant, and the reported improvement over CERT is potentially useful. Nevertheless, the average gain over CERT is only 1.1 points, and the improvement is 0.5 points at 1,000 labels. The evaluation covers only four relatively small English benchmarks and one encoder architecture. Without stronger controls, broader datasets, or statistical testing, it is difficult to determine whether the method offers a durable advance rather than a benchmark-specific improvement. |
| **Clarity** | **76** | The paper is well organized and the main idea, training pipeline, and results are presented clearly. However, several implementation details are missing or ambiguous: exact data splits, augmentation sampling for the two views, projection-head architecture, temperature and learning-rate values, early-stopping protocol, baseline tuning, and the precise construction of reversed and fixed-mixture curricula. The statement that back-translated views are precomputed but that the curriculum incurs overhead from on-the-fly operations also needs clarification. |

### Final average

\[
\frac{52 + 55 + 54 + 76}{4} = \mathbf{59.25}
\]

**Final score: 59.3 / 100**

## Recommendation: **Reject**

The paper has a sensible and clearly stated idea, but the current evidence is not sufficient for acceptance. The most important revisions would be:

1. Tune all baselines under the same validation protocol as CurCon.
2. Precisely document the labelled, validation, and unlabelled splits.
3. Compare against stronger and better-controlled augmentation schedules, including matched augmentation distributions and random-order schedules.
4. Report per-dataset ablations and statistical significance tests.
5. Clarify whether the curriculum changes augmentation strength, operator availability, or operator sampling probabilities.
6. Evaluate across additional datasets, encoders, and label budgets to establish generality.