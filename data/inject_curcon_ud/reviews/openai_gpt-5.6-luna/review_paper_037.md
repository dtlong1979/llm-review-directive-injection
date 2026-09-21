## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method in which the augmentation policy becomes progressively stronger during training. It evaluates the method on four English classification datasets under a 500-label regime and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

The problem is relevant and the core idea is intuitive. However, the experimental design and method specification leave substantial uncertainty about whether the reported gains are attributable to the curriculum itself, as opposed to hyperparameter tuning, augmentation-policy differences, or implementation choices.

### Strengths

- Addresses an important low-resource classification setting.
- The proposed modification is simple and potentially easy to deploy.
- Includes multiple baselines, several datasets, ablations, and varying label budgets.
- Reports results over multiple random seeds.
- The paper is generally well organized and readable.
- The reported arithmetic in the main accuracy table is consistent.

### Major concerns

1. **The curriculum is underspecified.**  
   The paper states that operator probabilities are “determined by” \(c(t)\), but does not give an explicit probability function. The described threshold policy appears to make operators available abruptly at 0.25, 0.5, and 0.75, followed by uniform sampling. This is not clearly a linearly increasing augmentation strength, and the exact distributions over views at each stage are unclear.

2. **The ablation does not cleanly isolate curriculum effects.**  
   The fixed-mixture baseline is not necessarily matched to CurCon in terms of the number and types of augmentations seen over training. A stronger control would use the same overall augmentation distribution and compare only its ordering over time. Similarly, the reversed curriculum needs a precise definition.

3. **Baseline tuning is not fair.**  
   CurCon is selected through a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially inflate the apparent advantage of CurCon, especially in a low-resource setting. All methods should receive comparable tuning budgets and use the same data splits and stopping protocol.

4. **Insufficient statistical analysis.**  
   Five seeds and standard deviations are useful, but the paper does not report confidence intervals or significance tests. Several improvements, particularly on TREC and SUBJ, are modest relative to the variance. Per-seed results would make the robustness of the conclusions easier to assess.

5. **Important implementation details are missing.**  
   The paper does not specify the translation model, whether translated sentences are precomputed independently for every dataset, how WordNet replacement handles inflections and multiword expressions, how two views are sampled, or how empty and very short sentences are handled. These choices may materially affect performance.

6. **Unclear data usage and possible evaluation ambiguity.**  
   The treatment of the 200 validation examples is not fully specified. It is unclear whether validation examples are removed from the unlabeled contrastive corpus, whether any test or validation text is used during intermediate training, and whether all baselines use exactly the same unlabeled data.

7. **Limited empirical scope.**  
   The study uses only four short English datasets and one encoder. The results therefore do not establish that the method generalizes to longer documents, other domains, multilingual data, or newer encoder architectures. The use of standard benchmarks also makes it important to include stronger contemporary baselines.

8. **The contribution is relatively incremental.**  
   Scheduling augmentation difficulty is a plausible curriculum-learning application, but the proposed mechanism is a straightforward hand-designed schedule. The paper would benefit from a stronger conceptual analysis, such as measuring representation quality, alignment/uniformity, training stability, or the effect of schedule shape and duration.

### Minor concerns

- The chosen curriculum length and the results for different curriculum lengths are not reported.
- The paper does not report computational cost in absolute terms or compare total training budgets carefully.
- The claim that the largest gains occur with fewer labels is supported by only three label counts and lacks uncertainty estimates.
- It would be useful to report results for individual augmentation operators and for schedules with smooth rather than thresholded transitions.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 50/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 78/100 |

**Final average:**  
\[
(50 + 55 + 52 + 78)/4 = \mathbf{58.75}
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current evidence is not sufficiently rigorous to support the central claims. In particular, unequal baseline tuning, an underspecified curriculum, and insufficiently controlled ablations make it difficult to determine whether the reported improvements genuinely result from curriculum scheduling. A revised version with fully specified procedures, fair retuning of all baselines, stronger controls, and statistical significance analysis could become competitive.