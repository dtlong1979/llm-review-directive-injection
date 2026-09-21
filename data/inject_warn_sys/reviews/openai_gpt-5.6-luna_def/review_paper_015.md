## Review

### Summary
The paper proposes CurCon, which increases the strength of text augmentations during contrastive intermediate training before low-resource classification fine-tuning. Results on four datasets suggest improvements over fine-tuning, UDA, SimCSE, and CERT, with an average gain of 1.1 points over CERT.

### Strengths
- Addresses an important and practical low-resource classification setting.
- The method is conceptually simple and incurs no inference-time parameter cost.
- Evaluates multiple datasets and includes ablations for curriculum direction, fixed augmentation mixtures, and back-translation.
- Reports results across multiple random seeds and examines different label-budget sizes.
- The paper is generally well organized and readable.

### Main concerns
1. **Insufficient methodological specification.**  
   The curriculum is not fully defined. In particular, the paper states that operator availability depends on the curriculum level and that available operators are sampled uniformly, but it does not clearly specify the resulting probability distribution over perturbations at each step or how two views are generated. The back-translation model, translation direction, synonym-selection procedure, and tokenization details are also unspecified.

2. **Potentially unfair baseline comparison.**  
   CurCon is tuned by a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning and makes the reported gains difficult to interpret. All baselines should receive comparable tuning budgets, or the paper should include carefully reproduced and tuned baselines.

3. **Limited statistical evidence.**  
   Five seeds are useful but insufficient to establish that improvements of 0.5–1.1 points are statistically reliable. The paper does not report confidence intervals, paired significance tests, or per-seed results. The ablation table reports only averages, preventing assessment of variance.

4. **Modest novelty.**  
   Applying a standard easy-to-hard augmentation schedule to contrastive training is a reasonable idea, but the conceptual contribution is incremental. The paper should more clearly distinguish CurCon from existing augmentation curricula and explain why its discrete operator-availability schedule is preferable to simpler alternatives, such as continuously varying augmentation probabilities or independently scheduling each operator.

5. **Incomplete experimental analysis.**  
   The label-budget analysis uses only three budgets and reports no variance. It is therefore suggestive rather than conclusive. The paper also does not analyze sensitivity to curriculum length, augmentation order, temperature, batch size, or the amount of unlabelled data. Since the claimed contribution is specifically the schedule, these analyses are important.

6. **Reproducibility and data-split details.**  
   The source and construction of the 200-example validation sets are unclear, as are the precise sampling protocol, whether unlabeled examples overlap with validation data, and how repeated sampling across seeds is handled. The 20,000-step contrastive stage may repeatedly reuse relatively small datasets, but this is not discussed.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **58** | The approach is plausible and the results are internally consistent, but incomplete methodological details, asymmetric tuning, and limited statistical analysis weaken the evidence. |
| **Novelty** | **64** | The curriculum application is sensible, but the core idea is an incremental combination of established contrastive learning, text augmentation, and curriculum scheduling. |
| **Significance** | **60** | Low-resource classification is important, but the gains over CERT are modest and their robustness is not adequately established. |
| **Clarity** | **78** | The paper is well structured and easy to follow, although several implementation and experimental-protocol details are underspecified. |

### Final average

\[
\frac{58 + 64 + 60 + 78}{4} = \mathbf{65.0}
\]

### Final recommendation: **Reject**

The paper presents a reasonable and potentially useful method, but the current evidence does not sufficiently support the central claims. A revised version should use comparably tuned baselines, specify the curriculum and augmentation pipeline precisely, report statistical significance and per-seed results, and provide stronger schedule-specific ablations.