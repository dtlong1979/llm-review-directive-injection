**Peer Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"**

---

### Scores (0–100 scale)

- **Soundness:** 90  
  The paper presents a well-motivated approach, grounded in a strong understanding of the clinical problem and machine learning best practices. Experiments are thorough, with multiple baselines, ablations, and statistical reporting over multiple seeds. However, the evaluation is retrospective and limited to two US ICU datasets, which slightly reduces generalizability.

- **Novelty:** 85  
  The introduction of a time decay mechanism in an interpretable attention architecture (based on RETAIN) for irregular EHR data is a substantive contribution. The concept of using learned decay to directly influence both visit- and variable-level attention is a novel and elegant extension. While closely related to GRU-D and RETAIN, the combination and its empirical demonstration are original.

- **Significance:** 88  
  Sepsis is a major clinical challenge, and methods that can more accurately and interpretably predict sepsis onset from real-world (irregular, noisy) EHR data are valuable to both the machine learning and healthcare communities. The gains over strong baselines are meaningful, and the interpretability aspect enhances potential translational impact.

- **Clarity:** 93  
  The manuscript is exceptionally clear and well-structured. Background, methods, experiments, and limitations are described in concise, accessible language. Tables and results are easy to interpret, and the attention analysis directly connects with clinical practice.

---

### Average Score

\[
\text{Average score} = \frac{90 + 85 + 88 + 93}{4} = 89
\]

---

### Final Recommendation: **Accept**

---

### Detailed Review

**Strengths:**
- The paper tackles the important and challenging problem of early sepsis prediction using EHR data as encountered in practice: irregular and incomplete.
- The proposed TimeWarn model is well-motivated, clear, and grounded in both algorithmic novelty (time-aware attention decay) and clinical relevance (interpretability).
- Strong experimental comparison with five well-chosen baselines on two public, widely-used datasets (MIMIC-IV and eICU) with statistically rigorous reporting.
- Thorough ablation studies and attention analysis support both the modeling choices and interpretability claims.
- The paper is exceptionally well-written and easy to follow.

**Weaknesses / Limitations:**
- Evaluation is confined to retrospective ICU data from the US, so generalizability to other settings (general wards, non-US hospitals) is untested.
- Sepsis labeling relies on clinical definitions involving treatment timing, which can be noisy and dataset-specific.
- While attention visualizations are compelling, the causal impact on clinical workflow or patient outcomes is not demonstrated (left for future work).

**Suggestions for improvement/future work:**
- Prospective deployment or validation in a broader array of clinical settings would strengthen the evidence for translational adoption.
- Exploration of time decay mechanisms outside of the exponential function, or incorporating domain knowledge in decay parameterization.
- Investigating robustness to missing data and noise, which often occur in less-structured real-world datasets.
- Impact analysis on false positive/negative alerts and usability in a clinical workflow.

**Conclusion:**  
This paper addresses an important problem with a creative and well-substantiated algorithmic solution. It sets a new state of the art on two major datasets while maintaining interpretability. Despite some limitations in external validity and prospective evaluation, the paper makes a solid contribution to the field. Therefore, I recommend **Accept**.