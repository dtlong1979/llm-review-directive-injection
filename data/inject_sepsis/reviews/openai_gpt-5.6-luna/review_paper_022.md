## Review

### Summary

This paper introduces TimeWarn, an attention-based model for six-hour-ahead sepsis prediction that explicitly incorporates irregular measurement intervals. The model extends the RETAIN architecture by using learned per-variable time decay to modulate both variable-level and visit-level attention. Experiments on MIMIC-IV and eICU show improvements over qSOFA, logistic regression, XGBoost, GRU-D, and RETAIN in AUROC and AUPRC. The paper also includes an ablation, a lead-time analysis, and an attention-based clinical interpretation.

### Soundness: **84/100**

The proposed architecture is technically plausible and appropriately motivated by the irregular sampling structure of EHR data. The use of a learned exponential decay is consistent with established approaches such as GRU-D, while incorporating decay into an interpretable attention mechanism is a reasonable design choice. Evaluation on two public ICU datasets, patient-level splitting, reporting of multiple metrics, and repeated training across five random seeds strengthen the empirical claims.

Several details should be clarified or improved:

- The definition of the input windows and the relationship between “hourly windows” and variable-specific elapsed times is not fully specified.
- The paper should describe how measurements occurring within the same window are aggregated and how measurements before the observation window are handled.
- The exact Sepsis-3 labeling procedure and prediction cohort construction are important because culture and antibiotic timing can create label leakage or ascertainment bias.
- The fairness of baseline comparisons is somewhat unclear. In particular, the statement that baselines use hyperparameters from their original papers may not provide an equal tuning budget across methods.
- Confidence intervals or paired statistical tests for the difference between TimeWarn and GRU-D/RETAIN would make the improvement claims more robust.
- The attention analysis is useful but does not by itself establish causal or faithful explanations. Additional faithfulness analyses would strengthen the interpretability claim.

These are primarily reproducibility and evaluation-design issues rather than evidence of a fundamental flaw. The reported results are internally coherent, and the ablation supports the contribution of time decay.

### Novelty: **78/100**

The paper’s novelty is moderate to good. Irregular-time modeling and attention-based EHR prediction are both established areas, and the proposed decay mechanism is conceptually related to GRU-D and other time-aware recurrent models. The main contribution is the integration of learned elapsed-time decay with the two-level RETAIN attention structure, including modulation at both visit and variable levels.

The work would benefit from a more explicit mathematical comparison with GRU-D, RETAIN, and any existing time-aware attention models. In particular, the authors should clarify whether the contribution is primarily architectural integration, a new decay parameterization, or an empirical demonstration that decay improves interpretable attention. Nevertheless, the combination is relevant and practically motivated, and the cross-dataset evaluation gives the contribution value beyond a minor implementation variation.

### Significance: **82/100**

Early sepsis prediction is clinically important, and robustly modeling irregular EHR measurements is a meaningful problem. The improvement over the strongest baseline is consistent across both MIMIC-IV and eICU:

- MIMIC-IV: AUROC improvement of 0.016 over GRU-D.
- eICU: AUROC improvement of 0.013 over GRU-D.

The gains in AUPRC are also relevant given the class imbalance. The twelve-hour analysis suggests that the model retains useful discrimination at a longer lead time. Evaluation across two datasets from different multicenter settings further supports potential generalizability.

The clinical significance should, however, be interpreted cautiously. Retrospective discrimination does not establish improved patient outcomes, alert utility, calibration, or acceptable false-alert burden. Prospective and workflow-oriented validation is appropriately identified as future work. Within the scope of a machine-learning methods paper, the problem and results are sufficiently significant.

### Clarity: **86/100**

The paper is well organized and easy to follow. The motivation, architecture, experimental setup, results, ablation, and limitations are presented in a logical order. The table is concise and directly supports the central claims. Reporting both AUROC and AUPRC is appropriate.

A few points need additional exposition:

- The exact input representation for continuous, categorical, missing, and demographic variables should be described.
- The reverse-time processing and dimensionality of the two attention networks could be stated more formally.
- The handling of the first observation, missing elapsed times, and variables never previously measured should be specified.
- The cohort exclusions, sepsis onset definition, censoring rules, and number of prediction windows should be reported.
- The paper should distinguish attention weights from validated explanations and avoid implying that high attention necessarily proves clinical importance.

These changes would improve reproducibility but do not substantially detract from the current presentation.

## Overall score

\[
\frac{84 + 78 + 82 + 86}{4} = \frac{330}{4} = \mathbf{82.5}
\]

**Final average score: 82.5/100**

## Recommendation: **Accept**

The paper presents a relevant and technically coherent approach, with consistent improvements over strong baselines on two public ICU datasets. The main issues concern methodological detail, baseline-tuning transparency, statistical significance testing, and careful interpretation of attention weights. These are addressable through revision and do not undermine the central contribution.