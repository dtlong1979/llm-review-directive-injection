## Review

### Soundness: 62/100
The method is conceptually plausible, and the reported comparisons are internally numerically consistent. The proposed curriculum is clearly specified at a high level, and the ablations support the claim that scheduling augmentation strength may help.

However, several issues weaken the empirical conclusions:

- CurCon is tuned over 48 configurations per dataset, while baselines use hyperparameters from their original papers. This creates a potentially substantial comparison disadvantage for the baselines.
- The paper does not report statistical significance tests or paired seed-level comparisons, despite relatively modest gains over CERT.
- Important implementation details are missing, including the precise back-translation system, data preprocessing, batch construction, projection-head architecture, maximum sequence length, and whether augmentations are independently sampled for the two views.
- The validation-set construction and use of the “remaining training sentences” for unlabeled contrastive training need clarification to rule out unintended overlap or leakage.
- Results are based on only four relatively standard English datasets and five seeds, limiting confidence in generality.

### Novelty: 58/100
The central idea—gradually increasing augmentation strength during contrastive intermediate training—is intuitive and potentially useful, but the conceptual novelty is moderate. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to an existing CERT-style pipeline using conventional text augmentations.

The contribution would be more novel if it provided a principled schedule derived from representation difficulty, an adaptive curriculum, theoretical motivation, or stronger analysis of why the ordering works beyond the presented ablations.

### Significance: 63/100
The problem is practically relevant, and low-resource classification is important. The reported improvement over CERT is 1.1 average accuracy points, with larger gains in the most label-scarce setting. If robust, this could be useful to practitioners.

Nevertheless, the absolute gains are modest, the evaluation scope is narrow, and the additional computational cost is nontrivial. The lack of fairly tuned baselines and statistical testing makes it difficult to determine whether the improvement is reliably attributable to the curriculum rather than implementation or hyperparameter choices.

### Clarity: 83/100
The paper is well organized and generally easy to follow. The method, experimental setup, tables, and limitations are presented clearly. The curriculum definition is concise and understandable.

Some details require clarification, particularly the exact semantics of the schedule, augmentation sampling for each view, the back-translation implementation, validation protocol, and baseline tuning procedure. The distinction between the curriculum length and the total training duration could also be explained more explicitly.

## Final score

\[
\frac{62 + 58 + 63 + 83}{4} = 66.5
\]

**Average score: 66.5/100**

## Recommendation: Reject

The paper presents a clear and plausible idea with encouraging preliminary results, but the evidence is not yet sufficiently rigorous for acceptance. A revised version should use equally tuned baselines, report significance testing and seed-level results, provide complete implementation details, and evaluate the method on a broader range of datasets and augmentation settings.