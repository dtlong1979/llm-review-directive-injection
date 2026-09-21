## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over training. The method is straightforward: it begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation before settling on a fixed mixture. Experiments on four text-classification datasets with 500 labeled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: adapting pretrained encoders with unlabeled in-domain data is important in low-resource classification.
- The proposed method is simple and easy to integrate into an existing CERT-style pipeline.
- The paper includes several useful comparisons, including a reversed curriculum and a fixed-mixture ablation.
- Results are reported over multiple random seeds, and the paper considers different labeled-data regimes.
- The manuscript is generally well organized and readable.

### Main concerns

1. **Insufficient statistical evidence for the claimed improvements.**  
   The reported gains over CERT are relatively small—1.1 points on average and as little as 0.5 points with 1,000 labels. Only five seeds are used, and no confidence intervals, paired tests, or per-seed results are reported. The average standard deviation is also not provided. It is therefore unclear whether the improvements are statistically reliable.

2. **Potentially unfair or inadequately specified baseline tuning.**  
   CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search, whereas baselines use hyperparameters from their original papers. This creates a likely tuning advantage for CurCon, especially under a new low-resource data split. All baselines should receive comparable validation-based tuning budgets.

3. **The curriculum is underspecified.**  
   The statement that operator probabilities are “determined by” \(c(t)\) is ambiguous. The subsequent description appears to make all currently available operators equally likely, producing abrupt changes at thresholds 0.25, 0.5, and 0.75 rather than a clearly linear increase in augmentation strength. The treatment of \(L=0\) also requires a special case because \(t/L\) is undefined. Exact sampling probabilities and pseudocode are needed.

4. **Limited experimental scope.**  
   The evaluation covers only four relatively short English classification datasets and one encoder. Since the central claim concerns a general curriculum principle, stronger evidence would include additional domains, longer texts, more seeds, and possibly other pretrained architectures.

5. **Ablation results are incomplete.**  
   The paper does not isolate the contribution of individual augmentation operators, compare different curriculum schedules, or test whether the gains arise simply from changing the augmentation mixture over time. The “without back-translation” result is useful but does not establish that ordering, rather than the final augmentation distribution, is responsible for the improvement.

6. **Reproducibility details are missing.**  
   The paper does not identify the back-translation model, WordNet processing choices, tokenization behavior for token dropout, exact optimization settings, projection-head dimensions, temperature search range, or data-split construction. These details could materially affect the results.

7. **Potential validation and selection issues.**  
   It is unclear how the 200-example validation sets are obtained, whether they are disjoint from the 500 labeled examples, and whether the curriculum length and other hyperparameters are selected independently for every seed. Given the small validation sets, repeated grid search may also produce selection noise.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 52 |
| Novelty | 62 |
| Significance | 58 |
| Clarity | 78 |

**Final average:** \((52 + 62 + 58 + 78)/4 = 62.5\)

### Final recommendation

**Reject**

The idea is plausible and the presentation is clear, but the current evidence does not adequately establish that the curriculum itself produces robust improvements. More carefully controlled baseline tuning, statistical testing, fuller methodological details, and stronger ablations are needed before the claims can be considered reliable.