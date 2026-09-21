## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases during training. The method is evaluated on four text-classification datasets in a 500-label setting and compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over CERT, particularly in the lowest-resource setting.

### Strengths

- The paper addresses an important and practically relevant problem: adapting pretrained language models with very limited labelled data.
- The proposed idea is simple, intuitive, and easy to implement.
- The experimental presentation is clear, with comparisons across multiple datasets and an ablation of the curriculum, augmentation operators, and label budget.
- Reporting results over five random seeds and including standard deviations is useful.
- The method does not introduce inference-time cost or additional model parameters.
- The paper is generally well organized and readable.

### Concerns

#### 1. Limited methodological novelty

The central contribution is a hand-designed schedule over existing augmentation operators. While applying curriculum learning to contrastive augmentation policies is a reasonable incremental contribution, the method is conceptually modest. The paper should more clearly distinguish CurCon from prior work on augmentation-magnitude schedules, difficulty-based contrastive learning, and dynamic data augmentation.

The schedule is also not truly continuous or strictly linearly increasing in difficulty. It uses thresholded operator availability, with a fixed mixture after the curriculum ends. This raises the question of whether the gains arise from the curriculum itself or simply from delaying the use of particular augmentations.

#### 2. Incomplete experimental controls

The comparison is not fully controlled. CurCon is tuned by a grid search over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an unfair advantage, especially in a low-resource regime where hyperparameter sensitivity can be substantial. Baselines should receive comparable tuning budgets, or the paper should report both original and tuned baseline performance.

The paper also does not specify whether all methods receive identical access to the same unlabelled data, augmentation resources, training steps, and computational budget. UDA and CERT may differ in their use of labelled and unlabelled examples, and these distinctions should be made explicit.

#### 3. Statistical evidence is insufficient

Although standard deviations are reported, there are no paired significance tests or confidence intervals. The reported gains over CERT are sometimes relatively small, especially at 1,000 labels. Results across five seeds are suggestive but do not establish that the improvements are statistically reliable. Per-seed results or paired tests would strengthen the claims.

#### 4. Ambiguity in the augmentation policy

The probability mechanism is underspecified. The manuscript states that token dropout is “always available,” while other operators become available at thresholds, and that available operators are sampled uniformly. It is unclear whether token dropout therefore receives probability \(1/2\), \(1/3\), \(1/4\), or some other probability at different stages. It is also unclear whether the two views use independent operators, whether the original sentence can be used as a view, and how failed synonym replacements or translation errors are handled.

The claim that augmentation strength increases linearly is therefore not directly supported by the formal definition. A precise algorithm or pseudocode would be helpful.

#### 5. Weak analysis of why the curriculum works

The ablation shows that the curriculum improves the average score, but it does not isolate the source of the gain convincingly. In particular, useful additional controls would include:

- a fixed-mixture baseline matched to the average operator frequencies used by CurCon;
- schedules with different transition points;
- a smooth probability schedule rather than threshold-based availability;
- schedules ordered by empirically measured difficulty rather than assumed difficulty;
- multiple curriculum lengths;
- comparison with a random operator schedule.

Without these controls, the improvement could result from the particular augmentation mixture or from the timing of back-translation, rather than from curriculum learning in general.

#### 6. Reproducibility details

Several details needed for reproduction are missing, including the exact WordNet replacement procedure, translation model and decoding settings, maximum sequence length, preprocessing, optimizer learning rate and warmup, temperature values, projection-head dimensions, stopping criteria, and the procedure for constructing the validation subsets. Since the labelled sets are randomly sampled, the paper should provide dataset split seeds or release the exact splits.

### Scores

- **Soundness:** 58/100  
  The overall design is plausible and the results are internally coherent, but experimental controls, statistical validation, and implementation details are insufficient for strong conclusions.

- **Novelty:** 50/100  
  The application of a curriculum to contrastive augmentation is a reasonable incremental idea, but the schedule is hand-designed and closely combines existing techniques.

- **Significance:** 62/100  
  Low-resource classification is important, and consistent gains over CERT could be useful if validated with stronger controls. The current evidence does not yet establish broad significance.

- **Clarity:** 79/100  
  The paper is well structured and easy to follow, although the augmentation probabilities and experimental protocol require clarification.

### Final average

\[
\frac{58 + 50 + 62 + 79}{4} = 62.25
\]

**Final average score: 62.3/100**

### Recommendation

**Reject**

The paper presents a clear and potentially useful incremental idea, but the current version does not provide sufficiently rigorous evidence to support its claims. A revised submission with matched baseline tuning, stronger schedule controls, statistical testing, and complete implementation details could become a solid contribution.