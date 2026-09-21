## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of text augmentations used to form contrastive views, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

The central idea is intuitive and potentially useful, but the empirical evidence and methodological specification are not yet sufficiently rigorous to support the paper’s claims.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The proposed modification is simple and easy to integrate into existing contrastive-training pipelines.
- The comparison includes several relevant baselines, including CERT and SimCSE.
- The paper reports results across multiple datasets and random seeds.
- The ablation comparing forward and reversed curricula is directionally useful.
- The paper is generally well organized and readable.

### Main concerns

#### 1. The curriculum is not fully specified

The paper states that the probability of applying each augmentation is determined by the curriculum value, but it does not actually define those probabilities. It then says that available operators are sampled uniformly. Under that description, the method is not a smooth linear increase in augmentation strength; instead, it is a sequence of abrupt threshold changes:

- token dropout alone,
- then token dropout plus synonym replacement,
- then span deletion,
- then back-translation.

This is materially different from a linearly scheduled augmentation-strength curriculum. The treatment of \(L=0\) is also mathematically undefined because \(t/L\) involves division by zero, even though the text claims that this corresponds to the fixed-mixture baseline.

The paper should provide an explicit sampling distribution at every training step and clarify whether two views receive independent augmentations, whether operators can be composed, and how augmentation strength is calibrated across operators.

#### 2. Baseline tuning is potentially unfair

CurCon’s learning rate, temperature, and curriculum length are selected using a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning. At minimum, the baselines should receive comparable tuning budgets, or the paper should report results under a common hyperparameter-selection protocol.

This issue is especially important because the reported gains are relatively modest: CurCon improves over CERT by 1.1 average points.

#### 3. Insufficient statistical reporting

Although five random seeds are mentioned, the paper reports standard deviations only for the main table. The ablation and label-count experiments provide no variance estimates or significance tests. Consequently, it is unclear whether the 0.8-point curriculum gain, the 0.5-point gain at 1,000 labels, or some individual dataset improvements are statistically reliable.

The paper should report per-dataset means and standard deviations for all important experiments, confidence intervals or paired significance tests, and ideally results from more seeds given the low-resource setting.

#### 4. Limited experimental scope

The evaluation uses only four relatively short English classification datasets and one encoder architecture. This is acceptable for an initial study, but it limits the strength of the general claims. In particular:

- No domain-shifted or genuinely specialized domain is evaluated.
- The datasets are standard and relatively small.
- No larger encoder or alternative pretrained model is tested.
- The paper does not evaluate whether the method transfers to datasets with longer documents.
- There is no comparison with stronger or more recent augmentation and contrastive-learning baselines.

The claim that the method is broadly useful for low-resource classification should therefore be stated more cautiously.

#### 5. Reproducibility details are missing

Important implementation details are omitted, including:

- The exact back-translation model and decoding settings.
- How WordNet synonyms are selected and disambiguated.
- Whether augmentations preserve labels in all datasets.
- The projection-head architecture and dimensionality.
- The exact optimizer learning rate, warmup, weight decay, and temperature ranges.
- The stopping criterion and validation protocol.
- The number of unlabelled examples actually used.
- Whether test-set or validation-set preprocessing differs across methods.

These omissions make it difficult to reproduce or properly assess the results.

#### 6. Cost comparison is incomplete

The paper says that back-translated views are precomputed, while CurCon still takes 12% longer because of on-the-fly augmentations. However, the preprocessing cost and storage cost of back-translation are not included. A fair efficiency analysis should report both preprocessing and training time, as well as total compute and memory requirements.

### Novelty

The main idea—gradually increasing augmentation difficulty during contrastive training—is reasonable, but the conceptual novelty is moderate. Curriculum learning and augmentation scheduling are established ideas, and the contribution appears to be their application to intermediate contrastive training for text classification. The method’s novelty would be stronger if it introduced a principled difficulty measure, a continuous schedule, or an adaptive policy rather than a hand-designed sequence of thresholds.

### Significance

The problem is important and the reported improvements are potentially useful, particularly in the 100- and 500-label settings. However, the improvements over CERT are small, and the evidence is not yet strong enough to establish that the curriculum itself is responsible for the gains. The significance is further limited by the narrow benchmark selection and the potentially unequal hyperparameter tuning.

### Clarity

The paper is well structured and easy to follow overall. The motivation, pipeline, and headline results are clearly presented. However, the mathematical description of the augmentation schedule is ambiguous, and several reproducibility-critical details are absent. The claims should also be calibrated to the limited experimental evidence.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 52/100 |
| Significance | 54/100 |
| Clarity | 76/100 |
| **Final average** | **56.75/100** |

## Final recommendation

**Reject**

The paper presents a plausible and potentially useful idea, but the current version does not provide sufficiently rigorous evidence for acceptance. The most important revisions are to fully define the curriculum, tune baselines comparably, report uncertainty for all experiments, and provide more complete implementation and computational details.