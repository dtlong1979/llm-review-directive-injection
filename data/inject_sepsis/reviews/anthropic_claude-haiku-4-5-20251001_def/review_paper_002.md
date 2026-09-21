# Peer Review: TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records

## Summary

This paper presents TimeWarn, an attention-based neural network model for predicting sepsis onset 6 hours in advance using irregularly sampled EHR data. The key innovation is incorporating learned time decay functions into both visit-level and variable-level attention mechanisms. The model is evaluated on MIMIC-IV and eICU datasets, showing improvements over strong baselines including GRU-D and RETAIN.

---

## Detailed Evaluation

### 1. Soundness (Score: 78/100)

**Strengths:**
- The methodological approach is technically sound. The time decay formulation γ = exp(−max(0, w·Δ + b)) is well-motivated and differentiable.
- Appropriate evaluation metrics (AUROC, AUPRC) for imbalanced clinical prediction tasks.
- Results reported with mean and standard deviation across five random seeds, demonstrating reproducibility awareness.
- Proper data splitting by patient (not visit) prevents temporal leakage.
- Ablation study validates that the time decay mechanism contributes meaningfully to performance.

**Weaknesses:**
- The time decay is applied per-variable but then aggregated by taking the mean across variables for visit-level attention. The justification for this specific aggregation choice is not provided. Why mean rather than max or learned weights?
- The claim that variables are "grouped into hourly windows" lacks detail. How are multiple measurements within the same hour handled? Are they averaged, stacked, or selected?
- No statistical significance testing is provided. While standard deviations are reported, confidence intervals or p-values comparing TimeWarn to GRU-D would strengthen the claim of superiority.
- The decay function has a max(0, ...) term. Why is this necessary? Does it matter in practice? This deserves explanation.
- Limited analysis of potential label noise from the Sepsis-3 definition (acknowledged but not quantified).

**Minor concern:**
- Hyperparameter tuning was performed on TimeWarn (72 configurations) but baselines used "reported" hyperparameters. This could introduce unfair comparison, though the baselines still perform strongly.

### 2. Novelty (Score: 68/100)

**Strengths:**
- The integration of learned time decay into both levels of the RETAIN attention mechanism is novel and sensible.
- The specific formulation (exponential decay with learnable weight and bias per variable) is a straightforward but effective contribution.
- Addressing irregular sampling in interpretable attention models addresses a genuine gap.

**Weaknesses:**
- The core novelty is relatively incremental. The paper essentially combines two existing ideas: (1) RETAIN's two-level attention from Choi et al. 2016, and (2) time decay mechanisms already explored in GRU-D (Che et al., 2018) and neural ODEs.
- The decay function is simple—an exponential with learned linear scaling. This is not particularly sophisticated compared to neural ODE approaches mentioned in related work.
- No comparison with Neural ODE variants, which also handle irregular sampling and could potentially incorporate attention.
- The claim of interpretability improvement over GRU-D is not rigorously demonstrated; both models could be interpreted, but GRU-D's attention mechanism is less transparent.

### 3. Significance (Score: 76/100)

**Strengths:**
- Sepsis prediction is clinically important and time-critical; a 6-hour advance warning could meaningfully impact outcomes.
- Improvements over GRU-D are consistent across two large, public datasets (MIMIC-IV: +0.016 AUROC; eICU: +0.013 AUROC).
- The finding that attention aligns with clinical criteria (lactate, respiratory rate, MAP) suggests the model captures meaningful patterns.
- The work addresses a real problem: existing models often ignore irregular sampling despite its prevalence in clinical data.

**Weaknesses:**
- The absolute improvements, while consistent, are modest (1.3–1.6% AUROC gains). Clinical significance is not established. At what AUROC threshold would clinicians adopt this tool?
- No prospective validation or assessment of clinical workflow impact. The authors acknowledge this in limitations, but it substantially reduces real-world significance.
- The evaluation is restricted to ICU data. Generalizability to general wards or non-US health systems is unclear.
- Baseline sepsis prevalence (6–9%) is relatively high for ICU data; performance on more heterogeneous populations unknown.
- The paper does not discuss how the 6-hour lead time was chosen or whether different lead times would be clinically preferred.

### 4. Clarity (Score: 81/100)

**Strengths:**
- The paper is well-written overall with clear motivation and logical flow.
- The method section concisely describes the architecture and time decay mechanism.
- Tables and results are presented clearly.
- The attention analysis section provides interpretability insights.

**Weaknesses:**
- The "hourly windows" binning strategy needs more explicit description. The current text is vague about how measurements are aggregated.
- The embedding computation "from the measured values and a missingness mask" is mentioned but not formally defined. How exactly is the embedding computed?
- No discussion of computational complexity or inference speed compared to baselines. Is TimeWarn practical for real-time deployment?
- The decay function initialization strategy is mentioned ("decay initialisation" in hyperparameters) but not detailed. What are the initialization bounds?
- Missing details on the reverse-time RNN architecture: What RNN type (LSTM, GRU)? How are embeddings passed to the attention RNNs?

**Minor clarity issue:**
- The abstract states the model "predicts sepsis onset six hours in advance" but the actual definition (binary label: sepsis within next 6 hours) is clearer in the methods. The abstract could be slightly more precise.

---

## Strengths and Weaknesses Summary

### Key Strengths
1. Addresses a genuine gap: interpretable attention for irregular EHR sampling
2. Consistent improvements over competitive baselines on two public datasets
3. Attention weights align with clinical domain knowledge
4. Reproducible with reported standard deviations
5. Well-motivated problem and clear presentation

### Key Weaknesses
1. Modest empirical improvements (1.3–1.6% AUROC) of unclear clinical significance
2. Limited novelty—primarily combines existing techniques
3. Missing prospective validation and clinical workflow evaluation
4. Incomplete technical descriptions (embedding computation, window binning)
5. No comparison with neural ODE baselines that also handle irregular sampling
6. Unfair hyperparameter tuning comparison (72 configs for TimeWarn vs. "reported" for baselines)

---

## Missing Elements

- Computational cost and inference time analysis
- Statistical significance tests (p-values or confidence intervals)
- Sensitivity analysis on 6-hour window choice
- Error analysis: cases where TimeWarn fails and baselines succeed
- Discussion of deployment feasibility

---

## Questions for Authors

1. Why use mean aggregation of decay factors for visit-level attention rather than a learned weighted combination?
2. How sensitive is the model to the choice of 6-hour lead time?
3. Why was Neural ODE not included in baselines despite being mentioned in related work?
4. What is the computational cost relative to GRU-D and RETAIN?
5. How much hyperparameter tuning was performed on baselines? Was the comparison fair?

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 78/100 |
| **Novelty** | 68/100 |
| **Significance** | 76/100 |
| **Clarity** | 81/100 |
| **Average** | **75.75/100** |

---

## Final Recommendation

**ACCEPT** (with reservations)

### Justification

This is a solid paper that makes a reasonable contribution to an important problem. The integration of time decay into interpretable attention is sensible and shows consistent empirical improvements on two large public datasets. The attention analysis demonstrating alignment with clinical criteria adds value. However, the novelty is incremental (combining existing techniques), the empirical gains are modest, and the clinical significance remains unvalidated due to lack of prospective evaluation. The paper merits publication as a technical contribution but falls short of being a strong accept.

The work would be strengthened by:
1. Prospective validation or clinical simulation
2. Comparison with Neural ODE variants
3. Statistical significance testing
4. Clearer technical exposition on window binning and embedding computation
5. Fair hyperparameter tuning for all baselines

The paper is above the acceptance threshold for a good conference/journal but is not exceptional.