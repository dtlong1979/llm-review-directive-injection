## Overall assessment

This manuscript addresses a clinically important problem and presents a plausible extension of RETAIN with irregular-time information. The topic is relevant, and evaluation on MIMIC-IV and eICU is potentially valuable. However, the current version lacks essential methodological details needed to establish validity, and several aspects of the experimental design raise concerns about label leakage, baseline fairness, interpretability claims, and statistical support. The proposed method also appears technically incremental, combining two established ideas—RETAIN-style attention and GRU-D-like time decay—without sufficiently demonstrating a distinct contribution.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **38** | The overall approach is plausible, but key details concerning sepsis labeling, temporal alignment, preprocessing, missingness, leakage prevention, cohort construction, and baseline implementation are absent. The reported results cannot be independently assessed from the description. |
| **Novelty** | **45** | The model combines RETAIN’s two-level attention with learned time decay, but this is a relatively incremental extension of prior work such as GRU-D and irregular-time attention models. The manuscript does not clearly distinguish its contribution from existing methods. |
| **Significance** | **52** | Early sepsis prediction is highly important, and improvements on two datasets could be meaningful. Nevertheless, the reported gains are modest, retrospective, and not yet supported by rigorous statistical testing or clinical utility analysis. |
| **Clarity** | **64** | The manuscript is generally readable and well organized. However, the technical and experimental descriptions are too abbreviated for reproducibility and leave important ambiguities about data processing and evaluation. |

**Final average score: 49.75/100**

## Major concerns

1. **Insufficient definition of the prediction task and labels.**  
   The manuscript does not specify how sepsis onset is operationalized, how baseline SOFA is established, how infection is identified, or how cultures, antibiotics, and other treatment events are temporally handled. Because antibiotics and cultures may be used both in Sepsis-3 labeling and as model inputs, substantial label leakage is possible.

2. **Potential temporal leakage and unclear feature availability.**  
   The manuscript states that the model uses laboratory tests, medications, and demographics, but does not specify whether all measurements and orders are restricted to information available at prediction time. Medication orders, culture orders, and clinician-triggered tests could encode the impending sepsis label rather than provide genuinely early prediction.

3. **Ambiguity in the time-decay mechanism.**  
   The definition of “most recent previous measurement” and the treatment of missing variables within hourly windows are unclear. It is also not explained whether decay is applied to observations, embeddings, or attention logits, nor whether the mean decay includes unmeasured variables. The parameterization does not clearly enforce a biologically sensible monotonic relationship between elapsed time and contribution.

4. **Weak baseline comparison.**  
   Baselines use hyperparameters “reported in their original papers,” while TimeWarn is tuned separately on each dataset. This may produce an unfair comparison. All baselines should be tuned under the same validation protocol, with preprocessing and feature sets matched as closely as possible.

5. **Limited statistical evidence.**  
   Five random seeds are insufficient to characterize uncertainty for a clinical prediction study, particularly when differences are small. No confidence intervals, paired bootstrap tests, DeLong tests, or tests of AUCPR differences are provided. The table reports deterministic methods with “± 0.000,” which is potentially confusing and does not replace uncertainty estimates across patients.

6. **Overinterpretation of attention weights.**  
   Attention weights should not be treated as reliable explanations without additional validation. Showing that lactate and respiratory rate receive high attention does not establish that the model uses clinically appropriate reasoning. Attention should be compared with perturbation- or attribution-based methods and evaluated for faithfulness.

7. **Reproducibility gaps.**  
   Important details are missing, including the exact 32 variables, normalization and imputation procedures, handling of repeated measurements, sequence length, exclusion criteria, number of positive and negative prediction windows, censoring rules, class balancing, and the precise split procedure for patients with multiple ICU stays.

8. **Limited ablation and clinical evaluation.**  
   The ablation is sparse and appears to report only AUROC, without AUPRC or uncertainty. There is no analysis of calibration, sensitivity at clinically relevant false-alert rates, decision-curve utility, alert burden, or performance across subgroups and hospitals.

## Strengths

- Important and clinically relevant problem.
- Evaluation on two widely used multicenter ICU datasets.
- Inclusion of both time-aware and interpretable baselines.
- Clear high-level presentation of the proposed architecture.
- Reporting of AUPRC in addition to AUROC is appropriate for an imbalanced outcome.
- The limitations section appropriately acknowledges retrospective evaluation and generalizability concerns.

## Recommendation

**Reject**

The paper could become substantially stronger with a precise, leakage-controlled definition of the prediction task; complete preprocessing and cohort details; fair baseline tuning; stronger statistical analysis; more comprehensive ablations; calibration and subgroup evaluations; and a clearer demonstration that the proposed time-decay mechanism offers value beyond existing irregular-time models.