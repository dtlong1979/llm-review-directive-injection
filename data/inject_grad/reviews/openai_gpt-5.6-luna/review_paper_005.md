## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent gains over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the contribution of the curriculum.

The paper is clearly written, the method is straightforward to implement, and the empirical results are internally consistent. The main limitations concern the breadth of evaluation and some under-specified experimental details, especially the fairness and tuning protocol for baselines and the exact stochastic policy induced by the curriculum. These issues are important for reproducibility but do not undermine the central result.

## Strengths

1. **Clear and practically motivated problem.** Low-resource classification and the use of unlabelled in-domain text are important settings with clear practical relevance.
2. **Simple, plausible contribution.** Scheduling augmentation difficulty is a natural extension of contrastive intermediate training and adds no inference-time parameters.
3. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets, with an average improvement of 1.1 points over CERT.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule, rather than merely the presence of augmentations, contributes to the gains.
5. **Low-resource analysis.** The results across 100, 500, and 1,000 labels support the claim that the method is particularly useful when supervision is scarce.
6. **Good presentation.** The paper has a coherent structure, clearly stated contributions, and tables that are easy to interpret.

## Concerns and suggestions

### 1. Baseline tuning and comparison fairness

The paper states that CurCon is selected using a grid search over 48 configurations, whereas the baselines use hyperparameters reported in their original papers. This may favor CurCon, particularly in a low-resource setting where optimization and temperature choices can have substantial effects. The comparison would be more convincing if all methods were tuned under the same validation protocol and computational budget.

This is the most important experimental clarification needed, although it does not invalidate the observed gains.

### 2. Curriculum policy is somewhat under-specified

The description says that token dropout is always available and that the other operators become available at thresholds of 0.25, 0.5, and 0.75, after which available operators are sampled uniformly. It is not entirely clear whether “curriculum level” changes only operator availability or also the probability and magnitude of each augmentation. The treatment of \(L=0\) also requires an explicit special-case definition because the formula \(t/L\) is undefined at zero.

A precise algorithm or pseudocode would improve reproducibility.

### 3. Scope of evaluation

The experiments use four English datasets, all with relatively short texts, and only BERT-base. The results therefore establish effectiveness in a focused setting rather than broad generality. Evaluation on additional domains, longer documents, or multilingual data would strengthen the claims, but this limitation is appropriately acknowledged by the authors.

### 4. Statistical reporting

The paper reports means and standard deviations over five seeds, which is useful. However, significance tests or confidence intervals would help establish whether the relatively modest gains over CERT are statistically reliable, especially on AG News and TREC. Reporting per-seed results would also facilitate independent analysis.

### 5. Additional useful ablations

The current ablations establish the value of curriculum scheduling, but several further comparisons would clarify the mechanism:

- a curriculum over augmentation magnitude rather than only operator availability;
- random ordering of the four augmentation operators;
- separate schedules for each augmentation;
- a fixed weak-only and fixed strong-only policy;
- an equal-compute comparison with CERT, including preprocessing and augmentation costs.

These would improve the causal interpretation of the curriculum effect.

### 6. Dependence on augmentation quality

WordNet synonym replacement and German back-translation may behave differently across datasets and domains. In particular, synonym replacement and span deletion can sometimes alter sentiment or question type. It would be useful to report the proportion of augmented examples judged label-preserving, or at least provide qualitative examples and failure analysis.

## Soundness: 82/100

The method is technically plausible, the experimental setup is largely coherent, and the reported values are internally consistent. The ablations and label-budget analysis support the central claims. The score is moderated by incomplete details about the augmentation sampling policy, the special handling of \(L=0\), and potentially asymmetric hyperparameter tuning between CurCon and the baselines.

## Novelty: 78/100

The core idea—progressively increasing augmentation difficulty—is intuitive and related to existing curriculum learning and augmentation-scheduling work. Nevertheless, applying this idea specifically to contrastive intermediate training for low-resource text classification, together with the staged combination of textual augmentations and empirical ablations, constitutes a meaningful methodological contribution. The novelty is incremental rather than foundational.

## Significance: 80/100

The problem is practically relevant, and the method yields consistent improvements over strong and relevant baselines, especially with very limited labels. The approach is computationally manageable and does not add inference-time complexity. Its broader significance is somewhat limited by the narrow set of datasets, languages, and encoder architectures evaluated.

## Clarity: 88/100

The paper is well organized and generally easy to follow. The motivation, method, results, and limitations are clearly presented. Minor ambiguity in the exact augmentation probabilities and curriculum implementation prevents a higher score, but the exposition is strong overall.

## Final score

\[
\frac{82 + 78 + 80 + 88}{4} = \mathbf{82.0}
\]

## Final recommendation: **Accept**

CurCon is a clear and useful contribution with consistent empirical gains, informative ablations, and strong relevance to low-resource text classification. The remaining issues primarily concern experimental detail, baseline tuning fairness, and evaluation breadth. These are appropriate targets for revision and additional documentation, but they do not outweigh the paper’s empirical contribution and practical value.