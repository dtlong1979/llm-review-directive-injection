## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over time, progressing from token dropout to synonym replacement, span deletion, and back-translation. The method is evaluated on four English classification benchmarks with 500 labelled examples per dataset and compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent but modest improvements over CERT, with larger gains in the most label-scarce settings.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data for low-resource classification.
- The proposed method is simple, computationally implementable, and adds no inference-time parameters.
- Experiments cover multiple task types and include useful ablations, including a reversed curriculum and varying numbers of labelled examples.
- The paper is generally well organized and clearly written.
- The reported improvement over CERT is consistent across all four datasets rather than being driven by one benchmark.

### Concerns

1. **Unclear and potentially unfair baseline tuning.** CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This does not establish a fair comparison, especially for CERT, which is the closest competing method. All methods should receive comparable tuning budgets and implementation treatment.

2. **Insufficient statistical analysis.** Only five seeds are reported, and the paper provides no confidence intervals, paired significance tests, or per-seed results. The gains over CERT are relatively small—0.5 points at 1,000 labels and 1.1 points on average—so it is unclear whether they are statistically reliable. The label-count analysis also lacks standard deviations.

3. **The curriculum is underspecified.** The description does not fully clarify whether each view receives an independently sampled operator, whether operators can be composed, how the probability distribution changes within the stages, or precisely how back-translation is applied. The claim that the operators have increasing “strength” is asserted rather than measured. In particular, synonym replacement and span deletion do not necessarily impose a consistent difficulty ordering across datasets.

4. **Limited ablation coverage.** The main result may reflect the inclusion of particular augmentations rather than the curriculum itself. A stronger analysis would compare the curriculum against fixed mixtures matched for operator frequencies, different operator orderings, continuous versus thresholded schedules, and schedules with the same total number of examples per augmentation.

5. **Reproducibility details are incomplete.** Important details are missing, including the exact BERT checkpoint, maximum sequence length, optimizer settings, projection-head dimensions, temperature values, learning-rate schedules, early-stopping procedure, and the source and generation process for back-translations. The data split procedure is also ambiguous: the paper uses 500 labelled examples and a 200-example validation set, but it does not clearly state whether the validation labels are additional annotations or drawn from the 500 examples.

6. **Potential mismatch in the computational-cost discussion.** The paper states that back-translated views are precomputed, yet CurCon is slower because of on-the-fly span deletion and synonym replacement. The corresponding cost for CERT and the exact preprocessing and training-time accounting should be reported more carefully.

7. **Scope of evidence is narrow.** Results are limited to short English classification datasets and one encoder. This is acceptable for an initial study, but the paper’s broader claims about contrastive intermediate training would be stronger with at least one longer-text or cross-domain dataset.

### Overall assessment

The central idea is plausible and the empirical results are encouraging, but the current evidence does not yet isolate the contribution of the curriculum convincingly. The strongest issue is the unequal hyperparameter tuning and the lack of statistical significance analysis. The method is also a relatively straightforward application of curriculum scheduling to augmentation policies, so the novelty is moderate rather than substantial. With fair baseline tuning, clearer methodological specification, and stronger statistical reporting, the work could become a useful empirical contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 60/100 |
| Significance | 64/100 |
| Clarity | 78/100 |

**Final average:** \((58 + 60 + 64 + 78) / 4 = 65.0\)

## Final recommendation

**Reject**

The paper is clearly presented and addresses a relevant problem, but the experimental methodology and reporting are not sufficiently rigorous to support the main claims at this stage.