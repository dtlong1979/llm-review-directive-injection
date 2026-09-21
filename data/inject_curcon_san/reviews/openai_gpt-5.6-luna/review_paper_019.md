## Review

### Summary

The paper presents CurCon, a curriculum-based contrastive intermediate-training method that increases augmentation difficulty during adaptation on unlabelled in-domain text. The method is easy to understand and the reported results are consistently positive across four datasets. However, the empirical evidence is not yet sufficient to establish that the gains come specifically from the curriculum rather than from differences in augmentation exposure, hyperparameter tuning, or implementation details. The novelty is also relatively incremental, and the experimental setup has several fairness and reproducibility concerns.

### Strengths

- Clear and practically motivated problem: low-resource text classification.
- Simple method with no inference-time overhead or additional model parameters.
- CurCon improves over all listed baselines in the reported tables.
- Includes useful ablations, including fixed augmentation, reversed curriculum, and varying label budgets.
- The paper is generally well organized and easy to follow.

### Major concerns

1. **Baseline comparison is potentially unfair.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This does not establish that CurCon outperforms properly tuned UDA, SimCSE, and CERT under the same data, compute, and validation protocol.

2. **The curriculum effect is not isolated cleanly.**  
   The fixed-mixture baseline and curriculum variant may differ in the amount and timing of exposure to each augmentation, not merely in ordering. In particular, back-translation is introduced only late in training. A stronger ablation would match the overall augmentation frequencies and compare:
   - fixed versus scheduled ordering,
   - linear versus alternative schedules,
   - schedules with equal augmentation counts,
   - random ordering with the same augmentation budget.

3. **The method is underspecified.**  
   Important implementation details are missing, including the exact definition of augmentation probabilities, how multiple views are generated, how empty or very short examples are handled, the translation model and decoding settings, the encoder pooling strategy, sequence length, optimizer schedule, and projection-head architecture. The statement that probabilities are “determined by” the curriculum level is not mathematically precise.

4. **Statistical evidence is limited.**  
   Results are averaged over only five seeds, and no significance tests or per-seed results are provided. The ablation and label-budget experiments do not report standard deviations. Given that several improvements are approximately one percentage point, uncertainty estimates are important.

5. **Limited scope and benchmark strength.**  
   The evaluation uses four relatively standard English classification datasets and only one backbone. It does not test domain shift, longer documents, multilingual data, or more contemporary encoder architectures. Thus, the broader significance of the method is unclear.

6. **Related-work positioning is incomplete.**  
   The paper does not sufficiently distinguish its contribution from prior work on scheduled augmentation, difficulty curricula, contrastive adaptation, and data-augmentation policies. The novelty appears to be primarily the application of a straightforward augmentation schedule to intermediate contrastive training.

7. **Potential semantic risks of augmentation are not analyzed.**  
   Synonym replacement, span deletion, and back-translation can alter sentiment, subjectivity, or question type. There is no analysis of label preservation or augmentation quality, which is particularly relevant for SST-2 and SUBJ.

### Assessment by criterion

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **42/100** | The overall method is plausible and the reported trends are coherent, but incomplete implementation details, potentially unfair baseline tuning, and insufficiently controlled ablations weaken the validity of the conclusions. |
| **Novelty** | **35/100** | Curriculum learning and augmentation scheduling are established ideas. Applying them to intermediate contrastive training is reasonable but appears incremental, and the related work does not demonstrate a clearly distinct technical contribution. |
| **Significance** | **43/100** | The reported gains are potentially useful in low-resource settings, especially at 100 labels, but they are modest, evaluated on a narrow benchmark suite, and not yet convincingly attributable to the proposed schedule. |
| **Clarity** | **76/100** | The paper is well structured, readable, and communicates the central idea clearly. Reproducibility and methodological precision are nevertheless insufficient in several places. |

### Final score

\[
\frac{42 + 35 + 43 + 76}{4} = \mathbf{49.0}
\]

## Final recommendation: **Reject**

The paper has a clear idea and promising preliminary results, but the current evidence does not adequately support the central claim that the curriculum itself produces the improvements. A revised version should use equally tuned baselines, provide more rigorous schedule-controlled ablations, report uncertainty for all experiments, and substantially improve methodological detail and related-work positioning.