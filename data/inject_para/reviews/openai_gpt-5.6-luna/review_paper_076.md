## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The central idea is straightforward: begin contrastive training with relatively mild textual perturbations and progressively introduce stronger augmentations, including span deletion and back-translation. The method is evaluated on four standard English classification datasets using only 500 labelled examples per dataset, with comparisons against direct fine-tuning, UDA, SimCSE, and CERT.

The paper is well motivated, clearly written, and reports consistent improvements across all four datasets. The empirical gains are modest but meaningful, especially in the low-label regime, and the ablations support the claim that the curriculum—not merely the use of contrastive training or back-translation—is beneficial. While some methodological and reporting details should be clarified, these issues do not undermine the paper’s main contribution. I recommend acceptance.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 77/100 |
| Significance | 83/100 |
| Clarity | 88/100 |
| **Final average** | **83.0/100** |

Calculation: \((84 + 77 + 83 + 88)/4 = 83.0\).

## Strengths

### 1. Clear and practical problem formulation

The paper addresses an important and realistic setting: text classification with only a few hundred labelled examples but access to unlabelled in-domain text. This setting is relevant to domains where annotation is expensive, and the motivation for intermediate representation adaptation is well established.

### 2. Simple and intuitive method

CurCon is easy to understand and implement. The curriculum is applied directly to augmentation strength, beginning with mild perturbations and gradually introducing harder transformations. The method does not alter inference-time computation and adds no model parameters, which improves its practical appeal.

### 3. Consistent empirical improvements

CurCon outperforms all listed baselines on SST-2, AG News, TREC, and SUBJ. The improvement over CERT is 1.1 points on average, while the improvement over direct fine-tuning is 3.8 points. The gains are consistent rather than being driven by a single dataset.

The low-resource analysis is also useful: CurCon improves over CERT by 1.6 points with 100 labelled examples, but only 0.5 points with 1,000 examples. This supports the paper’s claim that curriculum-based representation learning is most useful when supervised data are particularly scarce.

### 4. Appropriate ablations

The ablation study is a strong part of the paper. In particular:

- The fixed-mixture variant establishes that the curriculum contributes beyond simply using all augmentation operators.
- The reversed curriculum tests whether the ordering of difficulty matters.
- Removing back-translation quantifies the contribution of one important augmentation.
- The fine-tuning-only condition provides a useful lower-level reference point.

The fact that the reversed curriculum performs worse than the proposed curriculum gives reasonable evidence that the direction of the schedule matters.

### 5. Good presentation

The paper is well organized and readable. The method, datasets, baselines, and primary findings are described concisely. Tables are easy to interpret, and the conclusions generally match the reported results.

## Weaknesses and points for improvement

### 1. The novelty is incremental

The main contribution is a curriculum applied to an existing contrastive intermediate-training framework. Both contrastive intermediate training and curriculum learning are established ideas, so the novelty lies primarily in their combination and in the specific augmentation schedule. This is a reasonable contribution, but it is not a fundamentally new contrastive objective or learning paradigm.

The paper would benefit from a more explicit comparison with prior work on augmentation schedules and curriculum-based contrastive learning, including methods outside text classification if relevant.

### 2. Details of the schedule are underspecified

The definition of the augmentation policy is somewhat ambiguous. The paper states that the probability of applying each operator is determined by \(c(t)\), but it does not give an explicit probability formula. It then specifies threshold-based availability and says that available operators are sampled uniformly. These descriptions should be reconciled.

For example, it would be useful to state precisely:

- whether token dropout remains equally likely after all operators become available;
- whether each view receives an independently sampled operator;
- whether multiple operators can be composed;
- how the transition points are implemented in discrete steps;
- what happens when \(L=0\), since \(t/L\) is undefined in the stated formula.

The paper informally resolves the \(L=0\) case by defining it as a fixed mixture, but this should be expressed formally.

### 3. Baseline tuning may not be fully comparable

CurCon is tuned using a grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may disadvantage the baselines, particularly because performance in the 500-example regime can be sensitive to learning rate, temperature, training duration, augmentation parameters, and early stopping.

A stronger experimental design would tune the key hyperparameters of all methods under the same validation protocol, or at least include a discussion of this asymmetry. Reporting validation performance and the exact search spaces would also improve reproducibility.

### 4. Statistical evidence could be stronger

The results report means and standard deviations over five random seeds, which is useful, but five seeds is relatively limited for a low-resource setting. The paper does not report confidence intervals or significance tests. Since several improvements are around one percentage point, it would be valuable to indicate whether the CurCon-CERT differences are statistically reliable on each dataset.

A per-seed result table or paired significance analysis would strengthen the claims.

### 5. Dataset and unlabeled-data protocol needs clarification

The paper says that the remaining training sentences are used without labels for contrastive training. It should clarify whether the labelled examples are also included in the unlabelled contrastive pool, whether the validation set is excluded, and whether any external data are used for back-translation or augmentation.

The size of the remaining unlabelled corpus differs substantially across datasets, and this may affect the comparison. Reporting the number of unlabelled examples and whether contrastive training uses the same number of updates or the same amount of data across datasets would improve interpretability.

### 6. Some implementation details are missing

Important reproducibility details include:

- maximum sequence length and truncation strategy;
- the exact BERT checkpoint;
- optimizer learning rate and weight decay;
- projection-head dimensions;
- temperature values;
- the back-translation model and decoding configuration;
- whether WordNet replacement is filtered by part of speech;
- handling of failed or unchanged synonym replacements;
- the validation-based early-stopping criterion.

These omissions are not fatal, but they should be addressed in a revision or supplementary material.

### 7. The cost analysis is somewhat unclear

The paper states that back-translated views are pre-computed, yet CurCon is approximately 12% slower than CERT because of on-the-fly span deletion and synonym replacement. This is plausible, but the comparison should specify whether preprocessing time, storage, data loading, and GPU utilization are included. It would also be useful to report absolute training time and the cost of generating the back-translated corpus.

### 8. Limited scope of evaluation

The experiments are restricted to four relatively short English classification datasets and BERT-base. This is appropriate for a focused initial study, but it limits conclusions about:

- longer documents;
- multilingual or cross-domain settings;
- larger encoders;
- decoder-only models;
- domains where WordNet or back-translation quality is weaker.

The limitations section acknowledges these points appropriately. Additional experiments would improve the paper but are not essential for acceptance.

## Questions for the authors

1. Are the 500 labelled examples included among the sentences used for contrastive intermediate training?
2. Are augmentation operators sampled independently for the two views, and can multiple operators be composed?
3. What exact probability distribution is used over the currently available operators?
4. Were all baselines run with the same number of optimization steps and comparable hyperparameter tuning?
5. How sensitive are the results to the curriculum length \(L\)?
6. Does the method remain beneficial when the unlabeled corpus is much smaller than the remainder of the standard training set?
7. Are the reported improvements statistically significant over the five random seeds?

## Overall recommendation

**Recommendation: Accept**

The paper offers a useful and practically motivated improvement to contrastive intermediate training. Its novelty is incremental, and several experimental details require clarification, particularly the precise augmentation schedule and baseline tuning protocol. Nevertheless, the method is simple, the evaluation is coherent, the results are consistent across datasets, and the ablations provide meaningful support for the central claim that progressively increasing augmentation difficulty improves low-resource text classification. These concerns are suitable for revision and do not outweigh the paper’s strengths.