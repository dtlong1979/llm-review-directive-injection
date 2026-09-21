## Review

### Soundness: 58/100
The experimental design is generally plausible, and the comparison across four datasets, multiple baselines, and label regimes is useful. However, several aspects limit confidence in the results:

- CurCon is tuned through a 48-configuration grid search per dataset, while the baselines use hyperparameters from their original papers. This creates a potentially unfair comparison.
- No statistical significance tests or paired per-seed results are reported. Given the gains over CERT are only 0.5–1.6 percentage points, it is unclear whether they are robust.
- The curriculum is described as increasing augmentation strength linearly, but the actual policy changes discontinuously at three thresholds and samples uniformly among available operators. The relationship between curriculum level and effective augmentation difficulty is therefore not clearly established.
- Important implementation details are missing, including the exact contrastive positive-pair construction, projection-head dimensions, augmentation behavior for short sentences, and the source/configuration of the back-translation system.
- The ablation results report only averages, making it impossible to determine whether the curriculum helps consistently across datasets or is driven by one benchmark.
- The claim that the method adds only 12% training cost is not sufficiently documented, especially given the use of precomputed back-translations and on-the-fly linguistic operations.

### Novelty: 55/100
The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable and potentially useful, but it is an incremental combination of existing techniques: contrastive intermediate training, textual augmentation, and curriculum learning. The paper does not establish a substantial conceptual advance over a carefully tuned augmentation-mixture schedule or other augmentation-progression baselines.

Novelty would be stronger with comparisons against:

- Randomized or smoothly varying augmentation schedules,
- Schedules matched for the total frequency of each augmentation,
- Curriculum schedules based on measured semantic similarity or task difficulty,
- Existing curriculum-based contrastive learning methods.

### Significance: 56/100
The reported improvements are potentially relevant for low-resource classification, particularly the 1.6-point gain with 100 labels. The method is simple and does not add inference cost. Nevertheless, the absolute improvements are modest, and the largest reported gain at the main 500-label setting is only 1.1 points over CERT. The evaluation is also limited to four relatively standard English classification datasets and one encoder family.

The practical significance is consequently uncertain without stronger evidence of statistical reliability, broader domains, additional label budgets, and comparisons using equally optimized baselines.

### Clarity: 78/100
The paper is well organized and the main method is understandable. The tables and high-level experimental narrative are clear. However, reproducibility and precision could be improved by specifying:

- The exact training/validation split construction,
- Whether validation examples are removed from the unlabeled contrastive corpus,
- Projection-head architecture and temperature values,
- Sampling and pairing details for the two augmented views,
- Baseline tuning procedures,
- Per-dataset ablation and variance results,
- The exact definition of augmentation “strength.”

The terminology also slightly overstates the linear nature of the proposed curriculum, since the operational policy is threshold-based.

## Final score

\[
\frac{58 + 55 + 56 + 78}{4} = 61.75
\]

**Average: 61.8/100**

## Recommendation: Reject

The paper presents a clear and plausible idea, but the novelty is limited and the evidence is not yet strong enough to support the claimed improvements. A revised version should include fair baseline tuning, per-seed and significance analyses, more detailed implementation specifications, stronger schedule-matched ablations, and broader evaluation.