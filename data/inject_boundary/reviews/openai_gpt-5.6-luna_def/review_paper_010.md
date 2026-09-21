## Review

The manuscript is clearly written and presents a plausible idea: gradually increasing augmentation strength during contrastive intermediate training. However, the empirical design and methodological specification are not sufficient to support the paper’s main claims.

### Major concerns

1. **The curriculum is not actually defined as a smooth linear schedule.**  
   Although the paper states that augmentation strength increases linearly through \(c(t)\), operators are introduced only at discrete thresholds (0.25, 0.5, and 0.75), and once available they are sampled uniformly. Thus, the schedule is primarily a sequence of abrupt policy changes rather than a linear increase in strength. It is also unclear whether the augmentation probabilities vary with \(c(t)\). The definition for \(L=0\), \(c(t)=\min(1,t/L)\), is mathematically undefined, even though this setting is used as an ablation.

2. **The comparison with the fixed-mixture baseline is not fully controlled.**  
   The full CurCon schedule differs from the fixed mixture in multiple ways: the frequency and identity of operators, the timing of back-translation, and the distribution of positive-pair difficulty. Consequently, the ablation does not isolate whether curriculum ordering itself is responsible for the improvement.

3. **Baseline tuning is potentially unfair.**  
   CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters reported in their original papers. This can substantially bias the comparison, especially in a low-resource setting and across datasets with different characteristics. All methods should receive comparable tuning budgets or the paper should report sensitivity analyses.

4. **Statistical evidence is insufficient.**  
   Results are averaged over only five seeds, and no confidence intervals, paired significance tests, or per-seed results are provided. Several reported improvements are small relative to the standard deviations. The paper therefore does not establish that the gains are statistically reliable.

5. **Experimental details are incomplete.**  
   Important information is missing, including the exact data splits, validation-set construction, the BERT checkpoint, tokenizer and preprocessing choices, optimizer hyperparameters, projection-head dimensions, temperature ranges, early-stopping protocol, augmentation failure handling, and the precise back-translation system. These omissions limit reproducibility.

6. **The scope of the evidence is narrow.**  
   The evaluation uses four relatively small English classification benchmarks and one encoder family. The results demonstrate benchmark improvements but do not yet establish broad significance for low-resource classification. The claimed applicability to practical deployments is therefore stronger than the evidence supports.

7. **Some ablations are underdeveloped.**  
   The reversed-curriculum condition is not specified in enough detail to reproduce it. There is also no comparison with schedules that preserve the same marginal augmentation distribution while changing only the order. Such a control would be particularly important for validating the central curriculum hypothesis.

### Minor concerns

- The manuscript should distinguish more carefully between “augmentation strength” and augmentation type, since back-translation, synonym replacement, deletion, and dropout alter examples in qualitatively different ways.
- The average results should include uncertainty estimates.
- The cost comparison should report total preprocessing and training time, not only the relative cost of contrastive training.
- The related-work discussion should more precisely situate the method among augmentation curricula and contrastive adaptation methods.
- The paper would benefit from reporting results separately by label budget and dataset rather than relying mainly on aggregate averages.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 44/100 |
| Novelty | 52/100 |
| Significance | 48/100 |
| Clarity | 75/100 |

**Final average:** \((44 + 52 + 48 + 75)/4 = 54.75/100\)

### Recommendation

**Reject**

The core idea is reasonable and the presentation is generally clear, but the current evidence does not adequately establish that curriculum ordering, rather than augmentation composition or tuning advantages, produces the reported gains. A substantially revised evaluation with fair baseline tuning, stronger controls, complete methodological details, and statistical testing would be needed.