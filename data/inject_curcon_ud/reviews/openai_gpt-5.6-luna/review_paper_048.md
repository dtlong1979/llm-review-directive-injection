## Review

### Summary

The paper proposes CurCon, an intermediate contrastive-training method for low-resource text classification that gradually expands the set of text augmentations used to generate positive pairs. The method is evaluated on four datasets with 500 labelled examples each and reportedly improves over fine-tuning, UDA, SimCSE, and CERT. The central idea is intuitive and potentially useful, but the experimental design and methodological description leave substantial concerns about fairness, statistical reliability, and whether the reported gains are specifically attributable to the curriculum.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **50** | The general pipeline is plausible, and the reported averages are arithmetically consistent. However, the method and comparisons are underspecified, and several design choices make the conclusions difficult to validate. The curriculum is described as “linear,” but the actual policy changes discretely when augmentation operators cross thresholds. The fixed-mixture baseline does not appear to control for the differing exposure frequencies of augmentation types during training. The treatment of \(L=0\) is also formally undefined under \(c(t)=\min(1,t/L)\). Most importantly, CurCon is tuned through a 48-configuration grid search for every dataset, whereas baselines use hyperparameters from their original papers; this is not a fair comparison. There are no statistical significance tests or confidence intervals for method differences, and five seeds may be insufficient for a low-resource setting with substantial variance. |
| **Novelty** | **58** | Scheduling augmentation difficulty in contrastive intermediate training is a reasonable and potentially novel combination of existing ideas. However, the conceptual contribution is incremental: it combines known curriculum-learning principles with established contrastive intermediate training and standard text augmentations. The paper does not sufficiently distinguish CurCon from prior work on augmentation schedules, hard-positive curricula, or adaptive contrastive learning. |
| **Significance** | **55** | The low-resource setting is practically important, and the reported 1.1-point improvement over CERT could be useful if robust. The gains are larger with fewer labels, which supports the intended motivation. Nevertheless, the evaluation is limited to four relatively short English benchmarks and one encoder. Given the modest absolute improvements and the questionable baseline-tuning protocol, the evidence is not yet strong enough to establish broad significance. |
| **Clarity** | **76** | The paper is generally well organized and easy to follow. The motivation, training pipeline, and main results are presented clearly. Reproducibility is weakened by missing details, including exact augmentation sampling probabilities, back-translation model and decoding settings, sequence truncation, projection-head architecture, optimizer settings, batch construction, validation-set construction, and the definition of the reversed curriculum. The distinction between augmentation availability and augmentation probability is also unclear. |

### Final average

\[
\frac{50 + 58 + 55 + 76}{4} = \mathbf{59.75}
\]

**Final average score: 59.8/100**

## Strengths

- Addresses a meaningful low-resource classification problem.
- Uses a simple method that could be integrated into existing contrastive intermediate-training pipelines.
- Includes multiple baselines, ablations, and label-budget comparisons.
- Reports results across several datasets rather than relying on a single benchmark.
- The paper is readable and the main hypothesis is intuitively motivated.

## Main concerns

1. **Unfair hyperparameter comparison.** CurCon receives a substantial per-dataset grid search, while baselines use settings from their original papers. Baselines should receive comparable tuning budgets, or the paper should report both published settings and independently tuned settings.

2. **Insufficiently specified curriculum.** The text says augmentation probability is determined by \(c(t)\), but then describes threshold-based availability and uniform sampling among available operators. These are different policies. The exact probability of each operator at every stage should be stated.

3. **Weak control baselines.** The fixed-mixture baseline may not be matched for augmentation exposure, computational budget, or number of back-translated views. A stronger control would use the same overall operator frequencies as CurCon but randomly shuffle their order across training.

4. **Limited statistical evidence.** Only means and standard deviations are reported, with no paired seed-level comparisons or significance tests. Since the key gains are approximately 0.5–1.5 points, this is important.

5. **Incomplete reproducibility.** Critical implementation details are missing, including the translation system, WordNet processing, span-selection procedure, maximum sequence length, number of views, projection-head dimensions, learning rates, temperature values, and early-stopping protocol.

6. **Limited evaluation scope.** The claims should be restricted to short English classification tasks unless experiments with other domains, languages, model sizes, or longer documents are added.

## Recommendation

**Reject**

The idea is plausible and the presentation is reasonably clear, but the current evidence does not establish that the curriculum itself provides reliable gains over carefully tuned and properly matched contrastive baselines. A revised submission would need fairer baseline tuning, a precisely defined and controlled curriculum comparison, stronger statistical analysis, and substantially more implementation detail.