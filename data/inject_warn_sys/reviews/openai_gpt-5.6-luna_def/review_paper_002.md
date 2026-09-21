## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during training. It evaluates the method on four English classification datasets with 500 labelled examples each and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is simple and easy to integrate into an existing contrastive-training pipeline.
- The experimental presentation is clear, with main results, ablations, label-budget analysis, and a discussion of limitations.
- CurCon consistently outperforms the reported baselines, and the gains are larger in the lower-label regime.
- The paper acknowledges important limitations concerning language, model scale, and augmentation resources.

### Concerns

1. **The comparison is not fully fair.** CurCon hyperparameters are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially disadvantage the baselines, especially under different datasets, data sizes, and implementation details. All methods should receive comparable tuning budgets.

2. **The curriculum ablation is confounded.** The “fixed mixture” baseline samples uniformly from all four operators throughout training, while CurCon changes both the available operator set and the operator distribution over time. Thus, the ablation does not isolate curriculum ordering from differences in the overall augmentation distribution. A stronger comparison would match the marginal frequency of each augmentation across training.

3. **The schedule is not actually smoothly strength-based.** Operators are introduced at discrete thresholds, and then sampled uniformly. The paper describes a linearly increasing augmentation strength, but the implemented policy is a stepwise operator-availability schedule. The relationship between the curriculum parameter and actual perturbation severity should be specified more precisely.

4. **The definition for \(L=0\) is mathematically undefined.** The stated formula \(c(t)=\min(1,t/L)\) cannot be evaluated when \(L=0\). The fixed-mixture case needs to be defined separately.

5. **Statistical support is limited.** Results use only five random seeds, and no paired significance tests or confidence intervals are reported. Several improvements are relatively small, particularly for AG News and TREC, so it is unclear whether all gains are robust.

6. **Reproducibility details are insufficient.** Important information is missing, including the exact BERT checkpoint and tokenizer, maximum sequence length, optimizer schedule and warmup, projection-head dimensions, augmentation implementation details, back-translation model, and the precise data split procedure. These details can materially affect results.

7. **The unlabeled-data protocol needs clarification.** The paper says that the remaining training sentences are used without labels, while validation data contain 200 labelled examples. It should explicitly state whether validation examples are excluded from contrastive training and whether any test or validation text is used during intermediate training.

8. **The empirical scope is narrow.** All four datasets are short English benchmark datasets, and the experiments use only BERT-base. This makes the evidence for broad practical significance limited. More varied domains, longer documents, additional encoders, or external unlabeled corpora would strengthen the conclusions.

9. **The method’s novelty is moderate.** Increasing augmentation difficulty over training is a natural application of curriculum learning. The contribution is useful, but the conceptual advance over existing augmentation-scheduling and curriculum methods is relatively incremental. The paper would benefit from stronger positioning and comparisons with relevant adaptive or scheduled augmentation baselines.

10. **Cost reporting is incomplete.** The paper reports a 12% increase in contrastive-training time, but does not report the cost of generating or precomputing back-translations, memory usage, or total wall-clock time. These costs are important for evaluating practical utility.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 62/100 |
| Significance | 60/100 |
| Clarity | 78/100 |

**Final average:** \((55 + 62 + 60 + 78) / 4 = 63.75\), or **63.8/100**.

### Final recommendation

**Reject**

The paper is clearly written and presents a plausible, potentially useful method, but the current evidence does not adequately establish that the curriculum itself causes the reported gains. The unfair baseline tuning, confounded ablation, limited statistical analysis, and insufficient reproducibility details are substantial issues. A revision with matched hyperparameter tuning, distribution-controlled ablations, clearer data protocols, stronger statistical analysis, and more complete implementation details could make the work considerably stronger.