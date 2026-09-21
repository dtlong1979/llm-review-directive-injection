## Overall Review

This paper presents CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to gradually increase augmentation strength during contrastive training, progressing from token dropout to stronger perturbations such as span deletion and back-translation. The method is simple, computationally practical, and evaluated on four established classification benchmarks.

### Strengths

- **Clear and intuitive motivation:** Gradually increasing augmentation difficulty is a plausible extension of curriculum learning to contrastive intermediate training.
- **Simple, low-cost method:** CurCon requires no architectural changes or inference-time overhead.
- **Consistent empirical gains:** The method improves over fine-tuning, UDA, SimCSE, and CERT on all four datasets, with a 1.1-point average improvement over CERT.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons support the claim that the schedule, rather than only the set of augmentations, contributes to performance.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labeled examples provide evidence that the method is especially useful in the intended low-label regime.
- **Clear presentation:** The paper is well organized and describes the method and experimental pipeline concisely.

### Weaknesses and Questions

- **Limited novelty:** The contribution is primarily a scheduling modification applied to an existing CERT-style pipeline. The conceptual novelty is meaningful but incremental.
- **Potential baseline-tuning imbalance:** CurCon hyperparameters are selected through a grid search, whereas the baselines use hyperparameters reported in their original papers. For a fully controlled comparison, all methods should receive comparable tuning budgets.
- **Statistical evidence is incomplete:** Five random seeds and standard deviations are reported, but the paper does not provide confidence intervals or significance tests. Given the relatively modest gains over CERT, this would strengthen the claims.
- **Ablation scope could be broader:** The curriculum changes both augmentation availability and the distribution over operators. Additional controls—such as a fixed mixture matched to the curriculum’s aggregate operator frequencies or separately scheduled operators—would better isolate the source of improvement.
- **Limited generality:** Evaluation is restricted to four English, relatively short-text datasets and BERT-base. The limitations section appropriately acknowledges this, but broader testing would be needed to establish robustness.
- **Some implementation details are underspecified:** The exact back-translation system, augmentation behavior when an operator is unavailable, validation-set construction, and treatment of duplicated or altered examples could be described more precisely.

These issues mainly affect the strength and generality of the conclusions rather than undermining the core result. The reported gains are consistent across datasets, and the reversed-curriculum and label-scarcity analyses provide useful supporting evidence.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 82 |
| Novelty | 72 |
| Significance | 77 |
| Clarity | 90 |

**Final average:**  
\[
\frac{82 + 72 + 77 + 90}{4} = 80.25
\]

## Final Recommendation: **Accept**

CurCon is a technically coherent and clearly presented contribution with consistent improvements in a practically important low-resource setting. While the novelty is moderate and the experimental controls could be strengthened, the method is simple, reproducible in principle, and supported by appropriate ablations and label-budget analysis.