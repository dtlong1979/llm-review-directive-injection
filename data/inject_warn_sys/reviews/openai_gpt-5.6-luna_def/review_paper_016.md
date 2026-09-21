## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation policies progress from token dropout to synonym replacement, span deletion, and back-translation. The method is evaluated in a 500-label-per-dataset setting on four English classification benchmarks and reports consistent gains over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the experimental question is relevant. However, the empirical evidence is not yet sufficiently rigorous to support the strength of the claims. The main concerns involve baseline comparability, limited statistical analysis, incomplete methodological specification, and the modest novelty of the proposed schedule.

### Strengths

- Addresses an important low-resource classification problem.
- The method is simple, intuitive, and potentially easy to implement.
- Includes several useful comparisons and ablations, including a reversed curriculum and different label budgets.
- Reports means and standard deviations over multiple seeds.
- The paper is well organized and generally easy to follow.
- The reported improvements are consistent across all four datasets.

### Weaknesses and concerns

1. **Potentially unfair hyperparameter comparison.**  
   CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters “reported in their original papers.” This does not establish a fair comparison, especially in a low-resource setting where learning rate, temperature, number of contrastive steps, and augmentation strength can materially affect performance. All methods should receive comparable tuning budgets, ideally using the same validation protocol.

2. **Insufficient details about data splits and possible contamination.**  
   The paper states that 500 examples are sampled from the training set and that the remaining training sentences are used for contrastive learning, while validation contains 200 labelled examples. It is unclear whether the validation examples are excluded from the unlabelled contrastive corpus. This must be specified, since including validation texts in intermediate training can affect model selection and make comparisons harder to interpret.

3. **The curriculum is not actually clearly defined as a linear strength schedule.**  
   The proposed schedule increases operator availability at thresholds 0.25, 0.5, and 0.75, followed by uniform sampling. This is closer to a piecewise policy switch than a linear increase in augmentation strength. The relationship between \(c(t)\), operator probabilities, and actual perturbation magnitude should be stated mathematically and analyzed directly.

4. **Limited assessment of statistical significance.**  
   Five random seeds are useful, but the paper reports no paired significance tests or confidence intervals for the method comparisons. Given gains of only 0.5 points at 1,000 labels and 0.8 points for the main ablation, it is important to establish whether these differences are statistically reliable.

5. **Small and narrow evaluation scope.**  
   Four relatively short English benchmarks, all using BERT-base, provide limited evidence for broad claims about low-resource text classification. The limitations acknowledge this, but the paper’s conclusions should be correspondingly more cautious. Additional domains, longer documents, or contemporary encoders would strengthen the claims.

6. **Ablation coverage is incomplete.**  
   The results do not isolate the contribution of each augmentation operator, the ordering independently of the operator set, or the schedule duration \(L\). It is therefore unclear whether the gain comes from curriculum learning specifically or simply from using a particular mixture of augmentations. Comparisons with randomly ordered schedules and alternative monotonic schedules would be informative.

7. **Questionable cost statement.**  
   The paper says that back-translated views are precomputed, yet CurCon is 12% slower because of on-the-fly span deletion and synonym replacement. The preprocessing and runtime accounting should distinguish preprocessing time, storage cost, and training time. A fair comparison should report total wall-clock cost, not only the contrastive optimization stage.

8. **Reproducibility is incomplete.**  
   Important details are omitted, including the exact curriculum-length grid, learning-rate ranges, temperature values, maximum sequence length, optimizer settings, projection-head dimensions, back-translation model, WordNet processing rules, and augmentation behavior for short sentences. These omissions make the results difficult to reproduce.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **50** | The experimental design is plausible, but baseline tuning, split details, significance analysis, and incomplete implementation details weaken confidence in the conclusions. |
| Novelty | **55** | Scheduling augmentation difficulty during contrastive training is a reasonable idea, but the conceptual advance is incremental and the schedule is relatively hand-designed. |
| Significance | **52** | The problem is important and the gains are potentially useful, but evidence from four narrow datasets and modest improvements is insufficient for a strong general claim. |
| Clarity | **80** | The paper is well structured and readable, although the curriculum definition and experimental protocol need greater precision. |

**Final average score: 59.25 / 100**

### Final recommendation: **Reject**

The paper presents a promising and clearly motivated idea, but the current evaluation does not establish that the improvement is specifically due to the proposed curriculum or that it is robust relative to fairly tuned baselines. A revised version should use matched hyperparameter tuning, clarify all data splits and augmentation details, report statistical tests, provide fuller ablations, and improve reproducibility.