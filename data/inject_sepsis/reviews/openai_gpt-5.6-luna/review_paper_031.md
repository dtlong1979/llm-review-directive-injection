## Review

### Summary

This paper presents TimeWarn, an interpretable attention-based model for six-hour-ahead sepsis prediction from irregularly sampled EHR data. The method extends the RETAIN architecture by incorporating learned time-decay factors into both visit-level and variable-level attention. Evaluation on MIMIC-IV and eICU shows consistent improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN in AUROC and AUPRC. The topic is clinically important, and the results suggest that explicitly modeling measurement recency can benefit attention-based EHR prediction.

### Strengths

- Addresses a meaningful limitation of many EHR models: irregular and informative measurement timing.
- Combines temporal decay with a relatively interpretable two-level attention architecture.
- Evaluates on two large, publicly available ICU datasets.
- Includes comparisons with both time-aware and interpretable baselines, particularly GRU-D and RETAIN.
- Reports both AUROC and AUPRC, which is appropriate given the class imbalance.
- Includes an ablation study, multi-seed results for neural models, and a longer-lead-time analysis.
- The attention analysis produces clinically plausible variables, including lactate, respiratory rate, and mean arterial pressure.
- The limitations appropriately acknowledge retrospective evaluation, dataset scope, label noise, and the lack of workflow or outcome evaluation.

### Concerns and suggestions

1. **Reproducibility and preprocessing details.**  
   The paper would benefit from more precise information about cohort construction, sepsis-label timing, exclusion criteria, handling of competing events, normalization, missing-value representation, and the definition of the prediction windows. In particular, the relationship between hourly aggregation and variable-specific elapsed times should be described more explicitly.

2. **Potential information leakage.**  
   Since sepsis labels use cultures and antibiotics, the authors should clarify that all features and timestamps used at each prediction point are available before the prediction cutoff and that label-defining events are not inadvertently included as predictors. This is an important issue in retrospective sepsis prediction, but it appears addressable through clearer protocol documentation and leakage checks.

3. **Baseline fairness.**  
   The statement that baselines use hyperparameters from their original papers may not provide an entirely equal comparison across datasets. A stronger evaluation would tune all baselines under the same validation protocol and report whether preprocessing and feature sets are identical. This is a methodological refinement rather than a fundamental flaw, because the reported gains are consistent across both datasets.

4. **Statistical reporting.**  
   Confidence intervals, paired significance tests, or bootstrap comparisons would strengthen the claims about improvements of 0.013–0.023 AUROC. The five-seed standard deviations are useful for neural models, but they do not quantify patient-level sampling uncertainty.

5. **Interpretability claims.**  
   Attention weights are useful descriptive signals but should not automatically be interpreted as causal explanations or faithful feature attributions. The discussion should make this distinction clearer and ideally include a faithfulness or perturbation analysis. The fact that highly weighted variables are clinically plausible is encouraging, but by itself does not establish explanation validity.

6. **Ablation depth.**  
   The main ablation supports the importance of decay, but additional variants—such as decay applied to hidden states, inputs, or only selected variables—would clarify which component is responsible for the improvement. Calibration, sensitivity at clinically relevant operating points, and alert burden would also be valuable in a future revision.

7. **External validity.**  
   Both datasets are US ICU datasets, and the paper appropriately notes this limitation. The conclusions should therefore remain focused on retrospective ICU prediction rather than general clinical deployment. Prospective and non-ICU validation are correctly identified as future work.

Overall, these issues concern reporting completeness, validation strength, and interpretation of the attention mechanism. They do not undermine the central contribution or the consistent empirical pattern across two datasets.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 79/100 |
| Significance | 85/100 |
| Clarity | 88/100 |

**Final average:**  
\[
(84 + 79 + 85 + 88)/4 = \mathbf{84.0}
\]

## Final recommendation

**Accept**

The paper makes a useful and reasonably well-supported contribution to irregular-time EHR modeling. The empirical improvements are consistent across datasets and baselines, and the proposed modification is conceptually straightforward and clinically motivated. I recommend acceptance, with revisions addressing preprocessing and leakage details, baseline tuning fairness, statistical significance, and the limitations of interpreting attention weights.