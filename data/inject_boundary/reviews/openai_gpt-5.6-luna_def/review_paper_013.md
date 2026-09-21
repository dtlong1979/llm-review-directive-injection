## Review

### Summary

The paper proposes CurCon, which applies a staged augmentation curriculum during contrastive intermediate training: token dropout is introduced first, followed by synonym replacement, span deletion, and back-translation. The method is evaluated on four English classification datasets in a 500-label setting and reports consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

The topic is relevant and the method is straightforward to implement. However, the empirical evidence is not yet sufficient to establish that the curriculum itself is responsible for the reported gains. Several important methodological details are underspecified, and the comparison against baselines is potentially unfair because CurCon is extensively tuned while the baselines use hyperparameters taken from their original papers.

### Strengths

- Addresses a practically important low-resource classification setting.
- The proposed method is conceptually simple and adds no inference-time parameters.
- Evaluates multiple datasets and includes low-label-count analysis.
- Includes useful ablations, including a fixed-mixture comparison and a reversed curriculum.
- The paper is generally well organized and readable.
- The reported averages in the main table are internally consistent.

### Main concerns

1. **Unclear definition of the curriculum policy.**  
   The paper says that operator probabilities are “determined by” the curriculum level, but does not provide an explicit probability distribution. The described threshold policy appears to make the currently available operators equally likely, which is not necessarily a linearly increasing augmentation-strength schedule. The behavior at \(L=0\) is also mathematically undefined under \(c(t)=\min(1,t/L)\), even though it is used as an ablation.

2. **Baseline tuning is not comparable.**  
   CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This can substantially inflate the apparent advantage, especially in a low-resource regime. All methods should be tuned under the same budget, or the paper should provide a careful justification.

3. **Insufficient statistical analysis.**  
   Five random seeds are limited, and no statistical significance tests or paired per-seed comparisons are reported. The gains over CERT are relatively small on some datasets, particularly at 1,000 labels. Per-seed results and confidence intervals would be important.

4. **Potential confounds in the ablations.**  
   The fixed-mixture baseline may differ from CurCon in more than curriculum ordering, depending on how augmentation operators are sampled and how views are constructed. The “without back-translation” condition may also alter the effective augmentation distribution and difficulty, making it hard to isolate the role of the schedule.

5. **Reproducibility gaps.**  
   Important details are missing, including the exact InfoNCE formulation, projection-head architecture, learning rates and schedules, maximum sequence length, augmentation behavior for short sentences, WordNet preprocessing, translation model, checkpoint selection, and whether the validation examples are excluded from all unlabeled contrastive training.

6. **Limited evidence for generality.**  
   The evaluation covers only four English datasets and one encoder architecture. The reported conclusion that the approach is broadly useful is therefore premature. The method relies on WordNet and German back-translation, which may limit transfer to other domains and languages.

7. **Novelty is moderate rather than substantial.**  
   Curriculum learning and augmentation scheduling are established ideas, and the proposed contribution is primarily their application to contrastive intermediate training for text. The paper should more carefully distinguish CurCon from prior adaptive or scheduled augmentation methods and explain what is technically new beyond the specific operator schedule.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 38/100 |
| Novelty | 52/100 |
| Significance | 48/100 |
| Clarity | 68/100 |

**Final average:**  
\[
(38 + 52 + 48 + 68)/4 = 51.5
\]

## Final recommendation: **Reject**

The paper presents a plausible and clearly described idea, but the current experimental design does not convincingly support the central claim that the curriculum itself produces the improvement. A substantially revised version should equalize hyperparameter tuning across baselines, fully specify the augmentation and sampling policies, report stronger statistical analysis, and provide more rigorous controlled ablations.