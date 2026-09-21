## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four standard text-classification datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and addresses a practically relevant problem. However, several aspects of the experimental design and method specification make it difficult to determine whether the gains arise from the curriculum itself, from the augmentation mixture, or from differences in tuning and computational budget.

### Strengths

- Addresses an important low-resource classification setting.
- The overall pipeline is simple and potentially useful in practice.
- Includes comparisons with relevant baselines, including CERT and SimCSE.
- Reports multiple random seeds for the main results.
- Provides ablations for the fixed mixture, reversed curriculum, and removal of back-translation.
- The paper is generally well organized and easy to follow.
- The reported gains are consistent across all four datasets, which is encouraging.

### Main concerns

1. **The curriculum is not actually specified as a fully defined linear schedule.**  
   The paper states that augmentation strength increases linearly, but the described policy changes at discrete thresholds: operators become available at 0.25, 0.5, and 0.75, after which available operators are sampled uniformly. It is therefore unclear how augmentation strength is mapped to operator probabilities, and the schedule is not linear in the usual sense. The exact probabilities at each step should be provided.

2. **The key comparison does not isolate the curriculum cleanly enough.**  
   CurCon uses a changing operator distribution, whereas the fixed-mixture baseline samples all operators uniformly. The two methods may differ in effective augmentation difficulty, operator frequency, and the number of strong views. A stronger ablation would compare:
   - the curriculum against a fixed mixture with the same marginal operator frequencies;
   - a fixed-strength policy tuned separately;
   - schedules with equal compute and equal numbers of back-translated examples;
   - several curriculum lengths.

3. **Baseline tuning appears potentially asymmetric.**  
   CurCon receives a grid search over 48 configurations on each validation set, while the baselines use hyperparameters from their original papers. This may advantage the proposed method, particularly in a low-resource setting where tuning choices can have a substantial effect. All methods should ideally receive comparable tuning budgets, or the paper should report sensitivity analyses.

4. **Statistical support is incomplete.**  
   Although the main table reports five-seed means and standard deviations, the ablation and label-budget tables report only averages. It is not possible to assess whether the 0.8-point curriculum gain, or the smaller 0.5-point gain at 1,000 labels, is statistically reliable. Confidence intervals or per-seed results would strengthen the conclusions.

5. **Several implementation details are underspecified.**  
   The paper should clarify the exact back-translation system and decoding settings, treatment of sentences for which WordNet has no synonym, whether augmentations are applied independently to both views, maximum sequence length, optimizer learning rate and schedule, projection-head dimensions, and whether unlabelled data include the held-out validation or test sentences. These details matter for reproducibility.

6. **The attribution of improvements is not fully established.**  
   The strong performance may result primarily from the inclusion of back-translation or from the overall augmentation policy rather than from curriculum learning. The reported “without back-translation” result is useful, but additional controls are needed to establish that ordering is the causal source of the improvement.

7. **The scope of the evidence is limited.**  
   All datasets are short English benchmarks and the encoder is BERT-base. The results support the claims for this setting, but the broader claims about low-resource text classification should be stated more cautiously.

### Minor comments

- The term “aggressive back-translation” is somewhat imprecise, since back-translation is an operator rather than a continuously varying strength parameter in the current formulation.
- The paper should state whether the 500 labelled examples are re-sampled for each seed or held fixed across seeds.
- The validation-set construction and its relationship to the standard dataset splits should be described more precisely.
- Reporting task-specific results for the label-budget ablation would help identify whether the gains are concentrated in particular datasets.
- The computational-cost discussion should include total training time and the cost of generating the precomputed translations.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 62/100 |
| Novelty | 65/100 |
| Significance | 64/100 |
| Clarity | 78/100 |

**Final average:** \((62 + 65 + 64 + 78) / 4 = 67.25/100\)

## Recommendation

**Reject**

The idea is plausible and the presentation is clear, but the current evidence does not sufficiently isolate the contribution of the curriculum, and the asymmetric baseline tuning and incomplete experimental details weaken confidence in the reported improvements. A revised version with precisely defined schedules, matched tuning and compute controls, stronger statistical reporting, and more informative ablations could become a competitive submission.