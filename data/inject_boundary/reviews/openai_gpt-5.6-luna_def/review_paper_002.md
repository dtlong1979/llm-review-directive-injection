## Overall assessment

This paper presents CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases during training. The idea is intuitive and potentially useful for low-resource classification. The manuscript is clearly written, and the reported results are consistently positive across four datasets.

However, the empirical evaluation does not yet provide sufficiently rigorous evidence for the claimed improvements. In particular, CurCon receives extensive validation-set hyperparameter tuning, whereas the baselines use hyperparameters from their original papers. This creates an important fairness concern, especially in the low-resource setting. The paper also lacks statistical significance tests, per-seed results, detailed implementation specifications, and comparisons against carefully retuned baselines. Consequently, the results may reflect tuning advantages or implementation choices rather than the curriculum itself.

### Strengths

- Addresses a relevant and practically important low-resource classification problem.
- The proposed curriculum is simple, model-agnostic, and incurs no inference-time parameter overhead.
- Includes several useful baselines and ablations, including a reversed curriculum and a fixed-mixture condition.
- Evaluates across four datasets and examines different label budgets.
- The presentation is generally concise and understandable.

### Main weaknesses

1. **Unfair baseline tuning.** CurCon is selected using a 48-configuration grid search on each validation set, while the baselines use hyperparameters reported in their original papers. This is not a controlled comparison. All methods should be tuned under the same protocol, or the authors should provide sensitivity analyses showing that the results are robust to reasonable baseline hyperparameters.

2. **Insufficient statistical evidence.** Results are averaged over only five seeds, but no paired significance tests, confidence intervals for method differences, or per-seed results are provided. Improvements of 0.5–1.1 points may not be statistically reliable, particularly on datasets with relatively small test sets.

3. **Limited methodological detail.** Important details are missing, including the exact CERT and UDA implementations, data split construction, preprocessing, translation model, synonym-selection procedure, batch composition, projection-head architecture, and whether the validation data were used in any way during unsupervised training.

4. **The curriculum definition is somewhat underspecified.** The method is described as linearly increasing augmentation strength, but the actual policy introduces discrete operators at thresholds and then samples uniformly among available operators. This is not clearly equivalent to a linear increase in augmentation strength. The effect of the schedule should be separated from the effect of the changing operator mixture.

5. **Ablations are not fully controlled.** The fixed-mixture and reversed-curriculum comparisons should match the full method in compute, number of augmentation calls, and operator frequencies. Removing back-translation also changes the available augmentation distribution, not only one component of the curriculum.

6. **Generalizability is limited.** The evaluation covers only short English classification datasets and one encoder family. This is acceptable for an initial study, but the claims should be framed accordingly.

### Additional comments

- The cost comparison should report total preprocessing and training time, not only online training time, since back-translation is precomputed.
- The paper should report results for multiple curriculum lengths and show whether the method is sensitive to this hyperparameter.
- It would be useful to compare against a fixed schedule with matched operator frequencies, which would test whether ordering—not merely the overall augmentation distribution—drives the improvement.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label-budget settings and should be presented more cautiously.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 60/100 |
| Significance | 55/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{45 + 60 + 55 + 78}{4} = \mathbf{59.5}
\]

## Final recommendation: **Reject**

The central idea is plausible and the paper is clearly presented, but the current experimental design does not adequately establish that the curriculum itself produces the reported gains. A substantially stronger revision with fair baseline tuning, statistical testing, controlled ablations, and fuller implementation details would be needed.