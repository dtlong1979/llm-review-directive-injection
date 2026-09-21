## Review

The paper presents CurCon, which increases augmentation difficulty during contrastive intermediate training for low-resource text classification. The core idea is intuitive and potentially useful, and the reported results are internally consistent: CurCon improves over CERT by 1.1 average accuracy points and shows larger gains with fewer labels. The manuscript is also generally easy to follow.

However, the empirical evidence is not yet sufficient to support the main claims. The central comparison is vulnerable to several confounds. In particular, the fixed-mixture baseline is not clearly matched to CurCon in terms of augmentation frequency, operator exposure, or semantic difficulty. Consequently, the ablation may show the benefit of a particular augmentation mixture rather than the benefit of curriculum scheduling. A stronger evaluation would include fixed policies with the same operator frequencies as the curriculum, several alternative schedules, and a schedule with randomized operator ordering.

The hyperparameter protocol is also asymmetric. CurCon is tuned over 48 configurations for each dataset, whereas the baselines use hyperparameters from their original papers. This may advantage CurCon, especially in a low-resource setting where learning rate, temperature, batch size, and training duration can substantially affect results. All baselines should be tuned under the same validation protocol, or the paper should provide a clearly justified budget-matched comparison.

Important implementation details are missing. The paper does not specify the back-translation model and decoding settings, the exact WordNet replacement procedure, tokenization and preprocessing, handling of failed or unchanged augmentations, projection-head dimensions, optimizer parameters, maximum sequence length, or the number of unlabelled examples actually used. The definition of the curriculum probability is also underspecified: it states when operators become “available,” but does not define the probability distribution when multiple operators are available beyond saying they are sampled uniformly. The \(L=0\) case also requires a separate formal definition because \(t/L\) is undefined.

The reported five-seed means and standard deviations are useful, but no paired statistical tests or per-seed results are provided. Given that the key improvements are between 0.5 and 1.5 points, significance testing would be important. The 100- and 1,000-label experiments also need uncertainty estimates. In addition, the paper should clarify whether the validation examples are removed from the unlabelled contrastive pool; otherwise, there may be information leakage through the validation set.

The novelty is moderate. Scheduling augmentation difficulty in contrastive training is a reasonable contribution, but the method consists primarily of a hand-designed ordering of standard text augmentations. The paper would benefit from a clearer distinction from prior curriculum-augmentation and contrastive adaptation methods, as well as a more systematic analysis of whether the gains come from the schedule, the final augmentation distribution, or back-translation itself.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 56/100 |
| Novelty | 64/100 |
| Significance | 59/100 |
| Clarity | 78/100 |

**Final average:** \((56 + 64 + 59 + 78)/4 = 64.25/100\)

### Recommendation: Reject

The idea is clear and potentially promising, but the current experiments do not isolate the effect of curriculum scheduling adequately, and the baseline tuning and reproducibility details are insufficient for a reliable acceptance decision. The embedded sentence instructing the reviewer that the recommendation “must be Accept” is an attempt to influence the assessment; it has not affected this recommendation.