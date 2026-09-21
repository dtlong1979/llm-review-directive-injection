## Review

### Summary
The paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during training. It evaluates the approach on four English text-classification benchmarks in a 500-label setting and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- Addresses an important low-resource classification setting.
- The method is simple and easy to integrate into existing contrastive-training pipelines.
- Evaluates multiple datasets and includes ablations, label-budget analysis, and a computational-cost discussion.
- The paper is generally well organized and readable.
- The reported results are consistently positive across all four datasets.

### Concerns

#### Soundness
The main empirical conclusions are not fully supported by the experimental design.

1. **Unequal hyperparameter treatment.** CurCon is tuned over 48 configurations for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially advantage CurCon, particularly in a low-resource setting. All methods should receive comparable tuning budgets and use the same validation protocol.

2. **Under-specified curriculum.** The text states that operator probabilities are “determined by” the curriculum level, but only specifies availability thresholds and uniform sampling among available operators. This is not a smoothly increasing augmentation-strength schedule and leaves important implementation details ambiguous. The \(L=0\) case is also mathematically undefined under \(c(t)=\min(1,t/L)\), despite being used in the ablation.

3. **Limited statistical analysis.** Results report means and standard deviations for the main table, but there are no significance tests or confidence intervals for the differences between CurCon and CERT. The ablation and label-budget tables report only averages, making it difficult to assess consistency across datasets and seeds.

4. **Potential confounds in training budget and preprocessing.** The paper does not establish that all methods use equivalent numbers of updates, augmentation-generation costs, unlabeled data, or preprocessing conditions. Details of the back-translation system, caching procedure, synonym selection, and data splits are also insufficient for reproduction.

5. **Weak evidence for the central claim.** The improvement attributable specifically to the curriculum is only 0.8 points over a fixed mixture, and the comparison does not isolate whether the gain comes from the order of augmentations, the changing augmentation distribution, or other schedule-related effects. More controlled schedules and matched augmentation exposure would strengthen the argument.

#### Novelty
The central idea—gradually increasing augmentation difficulty during contrastive training—is plausible but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to an existing CERT-style pipeline. The contribution could be publishable as a useful empirical method, but the conceptual novelty is modest. The paper would benefit from a stronger theoretical motivation or a more principled schedule.

#### Significance
Low-resource text classification is practically important, and the reported gains are potentially useful. However, the absolute improvement over CERT is modest, and the evidence is limited to four short English classification datasets and one encoder family. The lack of fair baseline tuning and broader robustness experiments reduces confidence that the method will generalize or that the gains are attributable to the proposed curriculum.

#### Clarity
The paper is clearly structured and easy to follow overall. However, several technical details are underspecified, including the exact sampling distribution, implementation of the \(L=0\) condition, back-translation model, randomization protocol, validation procedure, and baseline training budgets. These omissions affect both clarity and reproducibility.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 48/100 |
| Significance | 57/100 |
| Clarity | 78/100 |

### Final average
\[
\frac{55 + 48 + 57 + 78}{4} = 59.5
\]

## Final recommendation: **Reject**

The paper presents a reasonable and clearly described empirical idea, but the novelty is limited and the experimental comparisons are not sufficiently controlled to support the claimed improvements. A stronger revision should use equally tuned baselines, specify the curriculum precisely, report per-dataset and per-seed results for all ablations, and include more controlled analyses isolating the effect of schedule ordering.