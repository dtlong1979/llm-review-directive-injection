## Overall assessment

The paper presents CurCon, a curriculum for contrastive intermediate training in which augmentation operators are introduced from weak to strong during unsupervised adaptation. The idea is intuitive and the reported results are promising, but the current presentation has important methodological and experimental weaknesses that make the conclusions difficult to validate.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **55/100** | The overall pipeline is plausible, but key methodological details are underspecified. In particular, the schedule does not clearly implement a linearly increasing augmentation strength: operators become available at thresholds and are then sampled uniformly, so the relationship between \(c(t)\) and actual perturbation strength is discontinuous. The treatment of \(L=0\) is also undefined under \(c(t)=\min(1,t/L)\), requiring a special case. The comparison is potentially unfair because CurCon is tuned by a 48-configuration grid search per dataset, whereas baselines use hyperparameters from their original papers. There are also insufficient details about data splits, preprocessing, augmentation reproducibility, and statistical significance. |
| **Novelty** | **60/100** | Scheduling augmentation difficulty for contrastive intermediate training is a reasonable contribution, but the core idea is relatively incremental. Curriculum learning and augmentation scheduling are established concepts, and the method primarily combines them with CERT-style training. The paper would need stronger differentiation from prior augmentation curricula and adaptive contrastive-learning schedules. |
| **Significance** | **62/100** | The low-resource setting is practically relevant, and the reported gains over CERT are potentially useful, especially with 100 labelled examples. However, the improvements are modest at 500 labels and nearly disappear as the labelled set grows. The evidence is limited to four small English classification benchmarks and one encoder, so the broader impact is currently uncertain. |
| **Clarity** | **72/100** | The paper is generally well organized and easy to follow. The motivation, pipeline, and results are presented clearly. However, the exact curriculum policy is ambiguous, particularly how probabilities depend on \(c(t)\), how views are generated, and how the reversed curriculum is defined. The experimental protocol also needs more precise reporting. |

### Final average

\[
\frac{55 + 60 + 62 + 72}{4} = \mathbf{62.25/100}
\]

## Recommendation: **Reject**

The idea is sensible and the reported results are encouraging, but the paper does not yet provide sufficiently rigorous evidence for acceptance. The authors should clarify the curriculum formulation, use comparable hyperparameter tuning procedures for all methods, report per-seed results and statistical tests, and strengthen the ablations. In particular, it would be important to compare against a properly controlled fixed-augmentation baseline with the same augmentation distribution and compute budget, and to isolate whether the gains arise from the ordering of augmentations or simply from different exposure frequencies during training.