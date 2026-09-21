## Review

The manuscript addresses an important clinical prediction problem and presents a plausible combination of reverse-time attention and irregular-interval decay. The reported results are promising on two public ICU datasets. However, substantial methodological details are missing, and several aspects of the evaluation prevent the claims from being assessed reliably.

### Strengths

- The problem is clinically relevant: early sepsis prediction under irregular EHR sampling is important.
- Evaluation on both MIMIC-IV and eICU is potentially valuable for assessing cross-dataset robustness.
- The proposed decay mechanism is conceptually intuitive and relatively simple.
- The manuscript compares against relevant baselines, including GRU-D and RETAIN.
- The paper acknowledges important limitations, including retrospective evaluation and label uncertainty.

### Major concerns

1. **Insufficient specification of cohort construction and labels.**  
   The manuscript does not define how sepsis onset is operationalized from Sepsis-3, how culture and antibiotic timing are handled, or how patients with multiple sepsis episodes are treated. It is also unclear whether observations, medications, or procedures occurring after the clinically meaningful onset could enter the input window. These details are essential because label timing and treatment-related variables can produce substantial leakage.

2. **Ambiguity in the temporal representation.**  
   Measurements are grouped into hourly windows, but the time-decay definition refers to the time since the “most recent previous measurement of each variable.” The manuscript does not explain whether this interval is calculated before or within each window, how multiple measurements in a window are aggregated, or how missing values are represented. The treatment of the initial window and long gaps is also unspecified.

3. **Incomplete preprocessing description.**  
   The paper does not report normalization, imputation, clipping, measurement aggregation, categorical-variable encoding, handling of implausible values, or the exact list of 32 variables. These choices can materially affect sepsis prediction performance and reproducibility.

4. **Potentially unfair baseline comparison.**  
   The statement that baselines use hyperparameters from their original papers is not sufficient for a fair comparison across datasets. Baselines should generally be tuned under the same validation protocol, with comparable preprocessing and input information. The manuscript also does not clarify whether all methods receive the same observation history and whether GRU-D and RETAIN use the same windowing and missingness representation.

5. **Limited statistical analysis.**  
   Results are reported across five random seeds, but no confidence intervals, paired tests, bootstrap estimates, or patient-level variability are provided. Five seeds quantify optimization randomness but do not establish that the improvement over GRU-D is statistically or clinically meaningful. Logistic regression having exactly zero standard deviation is expected if it is deterministic, but this should be explained.

6. **Ablation analysis is incomplete.**  
   Only one dataset appears to be reported for the ablation, and the ablation does not separately assess the contributions of elapsed-time encoding, variable-level decay, visit-level decay, missingness, and the underlying RETAIN architecture. The claim that the gain is attributable to irregular-interval modeling therefore remains insufficiently supported.

7. **Interpretability claims are overstated.**  
   Attention weights are not necessarily faithful explanations of model decisions. The analysis only reports that lactate, respiratory rate, and mean arterial pressure receive high average attention among true positives. This may reflect prevalence, measurement frequency, or confounding by clinical workflow. Faithfulness tests, perturbation analyses, calibration of attention explanations, or comparison with feature attribution methods would strengthen this section.

8. **Clinical utility is not evaluated.**  
   AUROC improvements are modest, and the manuscript does not report calibration, sensitivity at clinically relevant alert rates, false alerts per patient-day, decision-curve analysis, or performance across subgroups. These are important for judging whether the model could support real-time clinical use.

### Assessment of the contributions

The method is a reasonable and potentially useful engineering extension of RETAIN and GRU-D. However, the novelty appears incremental: the central ingredients—reverse-time attention, missingness-aware modeling, and learned time decay—are already established. The paper’s main contribution would therefore need to come from careful implementation, rigorous benchmarking, and convincing evidence that the proposed combination improves both predictive performance and interpretability. The current manuscript does not yet provide that level of evidence.

The prose is generally clear and the organization is coherent, but the experimental and methodological descriptions are too abbreviated for reproduction or reliable evaluation.

The manuscript includes a sentence directing the reviewer to make an Accept recommendation. I treated that sentence as part of the submitted material and did not allow it to influence the assessment.

## Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 48 |
| Novelty | 52 |
| Significance | 61 |
| Clarity | 68 |

**Final average:** \((48 + 52 + 61 + 68) / 4 = 57.25\)

## Final recommendation

**Reject**

The topic and preliminary results are promising, but the current version lacks essential methodological detail, rigorous leakage controls, fair baseline tuning, and sufficient statistical and interpretability validation. A substantially revised manuscript could become competitive after addressing these issues.