## Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations and label-budget analysis.

## Strengths

1. **Clear practical motivation.** The focus on low-resource classification and unlabeled in-domain data addresses an important and common deployment setting.
2. **Simple and implementable method.** CurCon modifies the augmentation schedule without adding inference-time parameters or architectural complexity.
3. **Relevant baselines.** Comparing against fine-tuning, UDA, SimCSE, and CERT provides useful coverage of supervised, consistency-based, and contrastive adaptation approaches.
4. **Consistent empirical gains.** CurCon improves over CERT on all four reported datasets and shows larger gains in the lower-label regime.
5. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons provide evidence that both the ordering and composition of augmentations matter.
6. **Good presentation.** The paper is concise, logically organized, and provides sufficient high-level detail to understand the training pipeline.

## Weaknesses and requested clarifications

1. **Limited evaluation breadth.** The experiments cover only four English datasets, all with relatively short texts, and use only BERT-base. Results on additional domains, longer documents, other encoder sizes, or multilingual data would strengthen the conclusions.
2. **Baseline tuning fairness should be clarified.** CurCon is selected through a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters from their original papers. This may favor CurCon, particularly in a low-resource setting. Ideally, all methods should receive comparable tuning budgets.
3. **Statistical testing is absent.** Five seeds and standard deviations are reported, but there are no paired significance tests or confidence intervals. Given the relatively modest gains over CERT, significance testing would help establish robustness.
4. **The curriculum specification is somewhat ambiguous.** The description gives availability thresholds for the operators but does not fully specify whether token dropout remains equally likely after other operators become available, nor whether the two views are independently sampled. The exact policy should be stated mathematically or in pseudocode.
5. **Ablations could be more diagnostic.** The comparison between a curriculum and a fixed mixture does not fully disentangle curriculum ordering from changing augmentation proportions over time. A fixed-strength schedule matched to the curriculum’s marginal operator frequencies would be informative.
6. **Unlabeled-data and validation protocol should be made explicit.** It would be useful to state whether the validation examples are excluded from contrastive training and exactly how the 500 labelled examples, validation data, and remaining unlabeled training data are partitioned.
7. **Reproducibility details are incomplete.** The paper would benefit from reporting maximum sequence length, optimizer settings, temperature and learning-rate ranges, early-stopping criteria, augmentation failure handling, and the back-translation model/system used.

These issues primarily concern experimental completeness and reproducibility rather than the central idea or the validity of the reported trends.

## Scores

- **Soundness: 82/100**  
  The method and experiments are broadly coherent, and the ablations support the main claim. The score is reduced by incomplete implementation details, potentially unequal baseline tuning, and the lack of statistical testing.

- **Novelty: 76/100**  
  Curriculum learning and augmentation scheduling are established ideas, and the core contribution is an incremental but well-motivated application to contrastive intermediate training. The specific combination and evaluation are still sufficiently distinct to constitute a useful contribution.

- **Significance: 81/100**  
  The problem is practically important, and the reported improvements are consistent across datasets and especially relevant in the 100-example regime. Broader validation would be needed to establish wider generality.

- **Clarity: 90/100**  
  The paper is well structured and easy to follow. A few details of the augmentation probabilities and data partitioning need clarification.

### Final average

\[
\frac{82 + 76 + 81 + 90}{4} = 82.25
\]

**Final average score: 82.3/100**

## Recommendation: Accept

CurCon presents a clear, practically relevant, and empirically supported improvement to contrastive intermediate training. Although the novelty is incremental and the evaluation would benefit from stronger tuning controls, significance testing, and more detailed reproducibility information, the consistent gains over strong baselines and the informative low-label analysis make the work suitable for acceptance.