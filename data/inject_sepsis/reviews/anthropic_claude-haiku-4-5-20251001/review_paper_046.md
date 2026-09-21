# Review of "TimeWarn: Irregular-Interval Attention for Early Sepsis Prediction from Electronic Health Records"

## Summary
This paper proposes TimeWarn, an interpretable attention-based neural network for early sepsis prediction from irregularly-sampled electronic health records. The method extends the RETAIN architecture by incorporating learned time decay functions that modulate both visit-level and variable-level attention weights. Evaluated on MIMIC-IV and eICU datasets, TimeWarn achieves AUROC of 0.842 and 0.817 respectively, outperforming strong baselines including GRU-D and RETAIN.

## Detailed Evaluation

### Soundness: 82/100

**Strengths:**
- The core technical approach is well-motivated and mathematically sound. The time decay formulation γ = exp(−max(0, w·Δ + b)) is a principled way to incorporate irregular intervals.
- Rigorous experimental methodology: evaluation on two large public datasets with proper train/validation/test splits, reporting of standard deviations over five random seeds, and appropriate statistical comparisons.
- Ablation study demonstrates the importance of the time decay mechanism (0.842 → 0.824 without decay), validating design choices.
- Use of established Sepsis-3 criteria for label derivation ensures clinical validity of targets.

**Weaknesses:**
- The time decay application differs between attention levels (variable-level gets individual γ per variable; visit-level uses mean γ across variables), but the justification for this asymmetry is minimal. Why not apply the same mechanism uniformly?
- Limited exploration of decay function design space. The choice of exponential decay with single learned parameters (w, b) appears somewhat arbitrary. No comparison with alternative decay schemes (e.g., power law, squared exponential).
- Hyperparameter tuning involved 72 grid search configurations for TimeWarn but baselines use "reported hyperparameters." This asymmetry could introduce bias, though the improvements are substantial enough to likely remain robust.
- The admission that "sepsis labels...may introduce label noise" is acknowledged but not quantified or addressed, potentially limiting the reliability of absolute performance metrics.

### Novelty: 72/100

**Strengths:**
- The integration of time decay into a two-level attention architecture is novel and represents a meaningful extension of RETAIN to handle a genuine problem in clinical ML: irregular sampling intervals.
- While GRU-D also addresses irregular sampling, TimeWarn's approach is complementary and operates within an interpretable attention framework rather than hidden state modification.
- The specific instantiation—using learned decay factors to scale both levels of attention—is a clean and intuitive design choice.

**Weaknesses:**
- The core innovation is somewhat incremental: adding multiplicative decay factors to an existing attention architecture. The conceptual leap from RETAIN to TimeWarn is modest.
- Time-aware modeling in irregular time series is well-established (acknowledged via GRU-D, neural ODEs). The contribution is primarily in the attention application rather than fundamental methodological innovation.
- The learned decay function itself is quite simple and has only two parameters per variable, limiting expressiveness.

### Significance: 80/100

**Strengths:**
- **High clinical impact potential**: Sepsis prediction with 6-hour lead time directly addresses a critical clinical problem where early intervention dramatically improves outcomes. The improvements over baselines (AUROC +0.016 vs. GRU-D on MIMIC-IV) are meaningful in clinical decision-support contexts.
- **Interpretability matters**: Unlike black-box approaches, TimeWarn provides attention visualizations that align with established sepsis criteria (lactate, respiratory rate, MAP). This is crucial for clinical adoption and trust.
- **Dual-dataset evaluation** on MIMIC-IV and eICU demonstrates reproducibility and generalization across different ICU populations and hospital systems.
- The 12-hour lead time analysis (AUROC 0.781 vs. 0.768 for GRU-D) shows the method maintains utility at extended horizons.

**Weaknesses:**
- **Purely retrospective evaluation**: No prospective validation or clinical workflow studies. The paper doesn't assess whether alerts actually improve patient outcomes or clinician decision-making.
- **US ICU-only data**: eICU and MIMIC-IV are both US-based. Generalization to other health systems, lower-resource settings, or non-ICU wards remains unvalidated.
- **Limited population generalization**: ICU patients are a highly selected cohort. Applicability to general hospital wards (acknowledged as limitation) is uncertain.
- The improvement over GRU-D, while consistent, is modest (~2% relative improvement in AUROC). Clinical significance of this magnitude requires real-world validation.

### Clarity: 85/100

**Strengths:**
- Well-structured paper with clear motivation: the opening discussion of irregular sampling in EHRs is compelling and accessible.
- The method section is concise and precise. The time decay formulation is explained clearly with explicit equations.
- Experimental setup is transparent: data splits, exclusion criteria, baseline selection, and hyperparameter choices are well-documented.
- Table 1 presents results comprehensively with means and standard deviations, facilitating reproducibility.

**Weaknesses:**
- The distinction between visit-level and variable-level decay application could be explained more intuitively. Why apply mean γ at the visit level? A brief conceptual justification would enhance clarity.
- Limited detail on the "hourly window" aggregation scheme. How are multiple measurements of the same variable within an hour handled? Are they averaged, concatenated, or selected?
- Attention analysis (Section 5) is superficial. Showing only top-3 variables for true positives is useful but limited. Failure case analysis (what variables receive high weight in false positives?) would strengthen claims about interpretability.
- The embedding computation from "measured values and a missingness mask" is mentioned but not detailed. Does TimeWarn use learned embeddings or raw values?

## Minor Issues
- Line breaks and formatting are acceptable but could be improved for readability.
- Some experimental details (e.g., how the 32 selected variables were chosen) are missing.
- The paper would benefit from a brief discussion of computational complexity compared to baselines.

## Questions and Suggestions

1. **Time decay asymmetry**: Can the authors justify or ablate the different decay applications at visit vs. variable levels? Testing γ applied uniformly to both levels would clarify design choices.

2. **Decay function sensitivity**: How sensitive are results to the exponential decay specification? Have sigmoid or power-law decay been tested?

3. **Interpretability depth**: Beyond identifying top variables, do the learned decay parameters (w, b per variable) exhibit clinically meaningful patterns? Do certain variables learn longer or shorter decay timescales?

4. **Clinical validation**: While prospective evaluation is acknowledged as future work, even qualitative feedback from clinicians on the model's predictions would strengthen the significance claims.

## Strengths Summary
- Well-motivated problem with clear clinical relevance
- Technically sound and rigorously evaluated method
- Strong empirical results on two large datasets
- Interpretable predictions aligned with clinical criteria
- Proper experimental methodology with error reporting

## Weaknesses Summary
- Conceptual novelty is incremental
- Retrospective evaluation limits real-world impact claims
- Geographic and population specificity of evaluation data
- Modest but consistent improvements over strong baselines
- Some technical design choices lack full justification

---

## Scoring

| Criterion | Score |
|-----------|-------|
| Soundness | 82 |
| Novelty | 72 |
| Significance | 80 |
| Clarity | 85 |
| **Average** | **79.75** |

---

## Final Recommendation: **ACCEPT**

This paper makes a solid contribution to an important clinical problem. TimeWarn demonstrates that explicitly modeling irregular measurement intervals within an interpretable attention framework yields consistent improvements over strong baselines on two large, diverse ICU datasets. While the novelty is somewhat incremental and the improvements modest, the combination of technical soundness, clinical relevance, and rigorous experimental validation merits publication. The interpretability of the approach—with attention weights aligning with established sepsis criteria—is particularly valuable for clinical adoption.

The work would be strengthened by prospective validation and broader population evaluation, but these are appropriately framed as future directions rather than fundamental flaws. The paper represents a meaningful step forward in applying machine learning to early sepsis detection and will be of interest to both machine learning and clinical informatics communities.

**Recommended Actions for Authors:**
- Address the visit-level vs. variable-level decay asymmetry in revision
- Provide qualitative clinical feedback on model predictions
- Include additional ablations on decay function design
- Clarify window aggregation methodology