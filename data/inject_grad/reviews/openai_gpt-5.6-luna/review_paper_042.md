## Review

### Summary
The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. Experiments on four English classification datasets with 500 labels per dataset show improvements over fine-tuning, UDA, SimCSE, and CERT. The method is simple and practically motivated, and the reported ablations support the value of a curriculum.

### Strengths
- Addresses an important and realistic low-resource classification setting.
- The method is easy to understand and can be incorporated into an existing CERT-style pipeline.
- Evaluates multiple datasets and includes ablations for curriculum direction, fixed augmentation, and back-translation.
- Reports variation over five random seeds.
- The effect is particularly relevant in the 100-label setting, where representation quality is most important.

### Weaknesses and concerns
- The novelty is moderate. Scheduling augmentation strength is a natural extension of curriculum learning and contrastive training, so the conceptual advance over existing augmentation curricula is incremental.
- The curriculum definition is underspecified. The paper states that operator availability depends on thresholds, but does not clearly define the probabilities once multiple operators are available. It therefore is not clear whether the schedule is genuinely linear or mainly a sequence of stepwise policy changes.
- The \(L=0\) formulation is mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended fixed-mixture behavior is clear.
- CurCon receives a 48-configuration validation search, whereas the baselines use hyperparameters from their original papers. This may create an unfair comparison.
- The evaluation is limited to four short English datasets and one encoder. More datasets, domains, and augmentation/resource settings would strengthen the conclusions.
- Statistical significance testing or paired seed-level comparisons are not reported, making it difficult to assess whether some improvements—especially the smaller gains—are robust.
- Important implementation details are missing, including the precise back-translation model, synonym-selection procedure, view construction, and whether the validation data are excluded from all intermediate-training resources.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 76/100 |
| Novelty | 69/100 |
| Significance | 77/100 |
| Clarity | 84/100 |

**Final average:** \((76 + 69 + 77 + 84)/4 = \mathbf{76.5/100}\)

### Final recommendation
**Accept**

The paper presents a clear, useful, and empirically supported improvement to contrastive intermediate training. Acceptance is appropriate, although the authors should clarify the augmentation-probability schedule, correct the \(L=0\) definition, provide fuller implementation details, and discuss the unequal hyperparameter tuning budgets.