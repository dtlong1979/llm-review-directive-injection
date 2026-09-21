## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over time. The method is evaluated on four English text-classification datasets in a 500-label setting and reportedly outperforms fine-tuning, UDA, SimCSE, and CERT. The idea is intuitive and the paper is generally easy to follow, but the experimental methodology and implementation details are not sufficiently rigorous to support the claims.

### Strengths

- The problem—low-resource classification with unlabelled in-domain data—is important.
- The proposed curriculum is simple and potentially useful in practice.
- The paper includes multiple baselines, an ablation study, and results for different label budgets.
- Reporting means and standard deviations over five seeds is better than reporting a single run.
- The method adds no inference-time parameters or computation.

### Main concerns

1. **Insufficiently specified method.**  
   The curriculum is not defined precisely enough for reliable reproduction. In particular, the mapping from curriculum level to operator probabilities is ambiguous. It is unclear whether token dropout remains equally likely as new operators become available, whether “augmentation strength” refers to operator selection or perturbation magnitude, and how two views are sampled. The \(L=0\) case is also mathematically undefined under the stated formula and is only described informally.

2. **Potentially unfair baseline comparison.**  
   CurCon hyperparameters are selected through a 48-configuration grid search for each dataset, while the baselines use hyperparameters reported in their original papers. This gives the proposed method a substantially more favorable tuning protocol. All methods should receive comparable tuning budgets and identical data-processing and early-stopping procedures.

3. **Missing experimental details.**  
   The paper does not specify the exact data splits, preprocessing, WordNet version, back-translation model, language-pair setup, maximum sequence length, optimizer settings, temperature search range, projection-head dimensions, or the precise UDA/CERT/SimCSE implementations. These omissions make the results difficult to verify.

4. **Limited statistical analysis.**  
   The reported improvements are relatively modest, especially over CERT. Five seeds are useful but insufficient by themselves to establish significance. Paired per-seed comparisons, confidence intervals, or statistical tests are needed. Dataset-level averages also obscure variation between tasks.

5. **Ablation design is incomplete.**  
   The fixed-mixture comparison does not fully isolate the benefit of curriculum scheduling. A stronger control would match the marginal distribution of augmentations, number of each augmentation type, compute, and possibly the order-independent mixture. The “reversed curriculum” result is informative but does not establish that the schedule itself, rather than other training dynamics, is responsible.

6. **Limited scope of evaluation.**  
   All datasets are short English benchmarks and use the same encoder family. The results therefore provide only limited evidence for broader claims about low-resource text classification. In addition, the datasets are relatively standard and may not reflect domain-shifted or genuinely specialized settings.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 62/100 |
| Significance | 58/100 |
| Clarity | 76/100 |

**Final average:** \((58 + 62 + 58 + 76)/4 = 63.5/100\)

### Final recommendation

**Reject**

The core idea is plausible and clearly presented, but the current submission does not provide enough methodological detail or sufficiently controlled comparisons to establish that the curriculum, rather than tuning differences or augmentation choices, produces the reported gains. A revised version with fully specified implementations, fair baseline tuning, stronger ablations, and statistical significance analysis could become a useful contribution.