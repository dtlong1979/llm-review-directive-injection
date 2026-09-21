## Review

### Summary

The paper proposes CurCon, which gradually increases the strength of text augmentations during contrastive intermediate training before low-resource classification fine-tuning. The idea is intuitive, and the experiments report consistent improvements over fine-tuning, UDA, SimCSE, and CERT on four datasets. However, the empirical evidence is not yet sufficient to establish that the curriculum itself is responsible for the reported gains.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The proposed method is simple and incurs no inference-time parameter overhead.
- The paper compares against several relevant baselines.
- Results are reported across multiple datasets and random seeds.
- The manuscript is generally readable and clearly organized.
- The ablations include a fixed-mixture baseline and a reversed curriculum, which are appropriate initial comparisons.

### Major concerns

1. **Insufficient isolation of the curriculum effect.**  
   The main comparison is against CERT, but CurCon changes the augmentation policy substantially. The reported improvement may result from the particular mixture of token dropout, synonym replacement, span deletion, and back-translation rather than from scheduling. The fixed-mixture ablation helps, but it is reported only as an aggregate average and lacks per-dataset results and uncertainty estimates. A stronger study should compare policies with identical augmentation counts and compute budgets, differing only in ordering.

2. **Potentially unfair hyperparameter comparison.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method a substantial tuning advantage, especially in a low-resource setting. All methods should receive comparable tuning budgets, or the paper should report both standard and equally tuned baseline results.

3. **Validation-set and selection details are unclear.**  
   The paper states that 500 examples are sampled for training and that validation sets contain 200 labelled examples, but it does not specify precisely how validation examples are obtained relative to the original training data and the unlabelled contrastive pool. The use of a small validation set for extensive grid search also raises concerns about validation overfitting.

4. **Limited statistical analysis.**  
   Five random seeds are useful but insufficient to support several conclusions about small improvements, particularly the 0.5-point gain at 1,000 labels. No significance tests, confidence intervals for method differences, or paired seed-level comparisons are provided.

5. **The curriculum definition is under-specified and internally ambiguous.**  
   The text says that operator probabilities are determined by the curriculum level, but then states that available operators are sampled uniformly. It is therefore unclear whether the schedule changes probabilities continuously or only changes the set of available augmentations at threshold values. The \(L=0\) case is also mathematically undefined under \(c(t)=\min(1,t/L)\), even though a special interpretation is given later.

6. **Reproducibility is incomplete.**  
   Important details are missing, including the exact BERT checkpoint, tokenization and truncation procedure, projection-head dimensions, optimizer settings, temperature values, learning-rate schedules, early-stopping criteria, augmentation implementation, back-translation model, and treatment of sentences for which WordNet or translation fails.

7. **Scope of evidence is narrow.**  
   The evaluation uses only four English datasets with relatively short texts and one encoder family. The conclusion that the method is generally effective for low-resource classification is therefore stronger than the evidence supports.

### Minor concerns

- The paper should clarify whether contrastive training uses the full unlabelled remainder, including examples from the labelled training distribution, and whether any test or validation text can enter the contrastive corpus.
- Results should include the per-dataset standard deviations for all methods in the label-count experiment.
- The computational-cost comparison should report total training time and preprocessing time, not only relative contrastive-stage time.
- The claim that the schedule is “linear” is somewhat misleading because the actual operator availability changes discontinuously at thresholds.
- The relationship to prior work on augmentation curricula and scheduled contrastive learning should be discussed more carefully to establish novelty.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 44 |
| Novelty | 60 |
| Significance | 54 |
| Clarity | 78 |

**Final average:** \((44 + 60 + 54 + 78) / 4 = 59.0\)

## Final recommendation

**Reject**

The proposed idea is clear and potentially useful, but the current experimental design does not convincingly establish that the curriculum schedule, rather than augmentation choice or unequal hyperparameter tuning, produces the reported gains. A substantially stronger and more reproducible evaluation would be needed.