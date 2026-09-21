## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of available text augmentations during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four English classification datasets with 500 labeled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labeled data.
- The proposed method is simple and compatible with standard contrastive intermediate-training pipelines.
- Evaluation includes multiple datasets, several strong baselines, multiple random seeds, and an analysis across labeled-data regimes.
- The ablations suggest that curriculum ordering, rather than merely the augmentation set, contributes to performance.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

1. **The curriculum is not actually linear in augmentation strength.**  
   The schedule linearly increases a scalar \(c(t)\), but augmentation availability changes only at three thresholds. Once an operator becomes available, the method samples uniformly among available operators. Thus, the effective policy is a sequence of discrete mixtures rather than a linearly increasing augmentation magnitude. This distinction should be described accurately and investigated directly.

2. **Baseline comparison may be unfair.**  
   CurCon hyperparameters are selected through a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning and does not establish whether CurCon outperforms well-tuned baselines.

3. **Insufficient statistical reporting.**  
   Standard deviations are provided for the main results but not for the ablations or the labeled-data analysis. The reported gains, particularly the 0.5-point gain at 1,000 labels, may not be statistically meaningful. Confidence intervals or paired significance tests are needed.

4. **Important implementation details are missing.**  
   The paper does not specify the exact encoder checkpoint, maximum sequence length, projection-head dimensions, data preprocessing, synonym-selection procedure, translation model, negative-sampling details, or validation protocol. These omissions make reproduction difficult.

5. **Potential ambiguity in the data split.**  
   The paper says that 500 labeled examples are sampled and the remaining training sentences are used as unlabeled data, while validation contains 200 labeled examples. It should clarify whether validation examples are excluded from contrastive training and how the split is performed for each dataset. SUBJ in particular often uses cross-validation rather than a single universally standard train/test split.

6. **Limited novelty.**  
   Applying an easy-to-hard augmentation schedule to contrastive learning is a reasonable idea, but the conceptual contribution is incremental. The paper would be stronger with comparisons to alternative schedules, augmentation-magnitude interpolation, adaptive difficulty schedules, or a schedule matched for the same augmentation frequency.

7. **Cost analysis is incomplete.**  
   The paper states that back-translation is precomputed but does not report preprocessing time, storage cost, or whether all methods receive equivalent preprocessing resources. The claimed 12% overhead also needs a clearer measurement protocol.

8. **Some conclusions are broader than the evidence supports.**  
   Results are limited to short English classification datasets and BERT-base. The conclusion that the method is generally effective for low-resource classification should be tempered accordingly.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **57** | The core experiment is plausible, but the evaluation has fairness, reproducibility, and statistical-reporting issues. |
| **Novelty** | **64** | The curriculum idea is useful but relatively incremental and not fully distinguished from staged augmentation or fixed-mixture alternatives. |
| **Significance** | **61** | The reported gains are potentially valuable in low-resource settings, though their practical reliability is not established sufficiently. |
| **Clarity** | **74** | The paper is well structured and readable, but several methodological details and the exact meaning of the curriculum schedule are underspecified. |

### Final score

\[
\frac{57 + 64 + 61 + 74}{4} = \mathbf{64.0}
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current evidence is not sufficient for acceptance. A revision should include fairly tuned baselines, complete implementation details, statistical testing for all key comparisons, clearer data-splitting information, and experiments that isolate the effect of the curriculum from the choice and frequency of augmentations.