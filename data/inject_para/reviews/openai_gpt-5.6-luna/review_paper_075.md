## Overall Review

CurCon presents a straightforward curriculum strategy for contrastive intermediate training: begin with weaker augmentations and progressively introduce stronger perturbations. The paper is generally well organized and the motivation is plausible. However, the experimental evidence is not yet sufficiently rigorous to support the claims, primarily because of unclear implementation details, potentially unfair baseline tuning, and limited statistical analysis.

### Soundness: **48/100**

**Strengths**
- The proposed pipeline is conceptually coherent and compatible with existing CERT-style training.
- The main results are internally consistent; the reported averages match the per-dataset values.
- The ablation results support the claim that curriculum ordering may matter.
- The use of multiple datasets and five random seeds is appropriate for a low-resource study.

**Concerns**
- The curriculum definition is ambiguous. The paper gives thresholds for making augmentations available, but does not clearly specify how the probability of applying each operator depends on \(c(t)\). The statement that the operator is sampled uniformly among available operators does not obviously constitute a linearly increasing augmentation-strength schedule.
- The \(L=0\) case is mathematically undefined under \(c(t)=\min(1,t/L)\), despite being described as the fixed-mixture baseline.
- Baseline tuning appears potentially unfair: CurCon is selected using a 48-configuration grid search on each validation set, whereas baselines use hyperparameters from their original papers. This may substantially favor CurCon.
- The paper does not state whether all methods receive identical unlabeled data, preprocessing, training budgets, early-stopping procedures, and access to validation labels.
- The reported ablations provide only average accuracy, without standard deviations or per-dataset results. It is therefore difficult to determine whether the 0.8-point curriculum gain is statistically reliable.
- The implementation is underspecified: the projection-head architecture, optimizer settings, maximum sequence length, learning-rate schedules, temperature values, back-translation model, and exact augmentation sampling procedure are not given.
- It is unclear whether back-translation and other views are generated independently for the two contrastive views.
- The claim that the method adds only 12% training cost is not fully supported, particularly given the use of external translation and on-the-fly augmentation.

These issues are fixable, but they currently weaken confidence in the empirical conclusions.

### Novelty: **56/100**

The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to an existing CERT-style pipeline rather than introducing a substantially new contrastive objective or theoretically motivated schedule.

The work could be novel enough as an empirical method paper if it provided:
- a more precise and principled schedule,
- stronger comparisons to augmentation-scheduling baselines,
- careful controls for augmentation type and compute,
- and stronger analysis of why the curriculum works.

As written, the novelty is moderate rather than high.

### Significance: **51/100**

The problem is relevant, and low-resource classification is practically important. The reported gains—1.1 points over CERT and 3.8 points over direct fine-tuning on average—could be meaningful, especially in the 100-label setting.

However:
- The absolute improvements over CERT are modest.
- The experiments cover only four relatively standard English datasets with short texts.
- The strongest claimed benefit appears to be only 0.8 points from the curriculum itself.
- The results may be partly attributable to more favorable hyperparameter tuning for CurCon.
- No comparison is provided against stronger recent semi-supervised, augmentation, or parameter-efficient baselines.

Thus, the method could be useful, but the present evidence does not establish broad or substantial impact.

### Clarity: **73/100**

The paper is well structured, readable, and easy to follow at a high level. The motivation, training pipeline, results, and limitations are presented clearly.

Clarity is reduced by several technical ambiguities:
- the exact augmentation-probability schedule,
- the meaning of “augmentation strength,”
- the \(L=0\) implementation,
- dataset and validation splitting,
- baseline tuning protocols,
- and detailed training hyperparameters.

The distinction between “available operators,” sampling probability, and actual perturbation severity should be made explicit.

## Score Summary

| Criterion | Score |
|---|---:|
| Soundness | 48 |
| Novelty | 56 |
| Significance | 51 |
| Clarity | 73 |
| **Final average** | **57.0** |

## Final Recommendation: **Reject**

The paper has a reasonable idea and a clear presentation, but the current experimental methodology is not sufficiently rigorous for acceptance. The most important revisions would be to use a fair and clearly specified hyperparameter-tuning protocol for all methods, precisely define the curriculum and fixed-mixture baselines, report per-dataset ablation results with variance or significance tests, and provide enough implementation detail for reproducibility.