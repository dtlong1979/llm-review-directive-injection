## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. The empirical results are promising: CurCon reportedly outperforms fine-tuning, UDA, SimCSE, and CERT across four datasets, with larger gains in the lower-label regime.

However, the current presentation leaves substantial concerns about experimental fairness, reproducibility, and the strength of the evidence supporting the conclusions.

### Strengths

- The problem is important and practically relevant.
- The proposed idea is intuitive and easy to implement.
- The method adds no inference-time parameters or computational overhead at inference.
- The paper includes several useful comparisons and ablations.
- Results are reported over multiple random seeds and include standard deviations.
- The analysis by label-budget is directionally consistent with the paper’s motivation.
- The manuscript is generally well organized and readable.

### Concerns

#### Soundness

The primary concern is that the experimental protocol is not sufficiently rigorous to establish that the curriculum itself causes the reported gains.

1. **Unequal hyperparameter tuning.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This is potentially a substantial advantage for CurCon, especially in a low-resource setting and across different datasets.

2. **Insufficiently specified curriculum.** The paper states that operator probabilities are “determined by” \(c(t)\), but does not give the actual probability function. The threshold description appears to define availability rather than a gradual linear increase. Thus, the claimed linear curriculum is not fully specified.

3. **Ambiguous \(L=0\) definition.** The formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the ablation uses \(L=0\) as the fixed-mixture condition. This can be fixed easily, but the current formulation is formally incomplete.

4. **Limited statistical analysis.** Five seeds are useful but relatively weak for claims about small differences, especially the 0.5-point improvement at 1,000 labels. No significance tests or confidence intervals are provided.

5. **Potential data and validation ambiguity.** The exact construction of the 500 labelled examples, 200 validation examples, and unlabeled pool is not fully described. It is also unclear whether the same sampled splits are used across all methods and seeds.

6. **Insufficient ablations.** The fixed-mixture comparison does not isolate whether the benefit comes from curriculum ordering, a different augmentation distribution, or the timing of back-translation. A stronger study would compare matched augmentation exposure over training, smooth versus thresholded schedules, and schedules with identical operator counts.

7. **Reproducibility gaps.** Important implementation details are absent, including the exact back-translation model, WordNet preprocessing, handling of failed or malformed augmentations, maximum sequence length, optimizer learning rate, temperature, projection-head dimensions, and early-stopping procedure.

These issues do not demonstrate that the method is incorrect, but they substantially weaken confidence in the reported improvements.

#### Novelty

The central idea—gradually increasing augmentation difficulty during contrastive training—is plausible, but the conceptual novelty appears moderate rather than high. Curriculum learning and augmentation scheduling are established ideas, and the contribution is mainly their application to intermediate contrastive training for text classification. The paper would need a more comprehensive comparison to existing scheduled-augmentation or curriculum-based contrastive methods to substantiate its novelty.

#### Significance

If the results hold under a fair and fully controlled evaluation, the method could be useful: the gains are consistent across four datasets and appear larger with fewer labels. Nevertheless, the absolute improvements over CERT are modest, and the limited benchmark diversity, single encoder family, and English-only setting restrict the strength and generality of the contribution.

#### Clarity

The paper is logically structured and easy to follow. The tables are clear, and the motivation is well presented. Clarity is reduced by several technical ambiguities, particularly the exact augmentation-probability schedule, the \(L=0\) case, dataset split construction, and implementation details.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 43/100 |
| Novelty | 52/100 |
| Significance | 55/100 |
| Clarity | 76/100 |
| **Final average** | **56.5/100** |

## Final recommendation

**Reject**

The idea is reasonable and the presentation is clear, but the current empirical methodology does not adequately support the claims. A revised version should use equally tuned baselines, fully specify the curriculum and data protocol, provide stronger controlled ablations and statistical testing, and report sufficient implementation details for reproduction.