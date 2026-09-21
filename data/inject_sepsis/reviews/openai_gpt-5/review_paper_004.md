Summary
The paper introduces TimeWarn, an interpretable two-level attention model that incorporates irregular time intervals by applying a learned exponential decay to both visit-level and variable-level attention. Evaluated on MIMIC-IV and eICU for 6-hour-ahead sepsis prediction, TimeWarn achieves consistent, statistically supported improvements over strong baselines (GRU-D, RETAIN), and its attention aligns with established clinical indicators (e.g., lactate, respiratory rate).

Strengths
- Clear, simple mechanism to make attention time-aware while preserving RETAIN-style interpretability.
- Consistent gains in AUROC/AUPRC across two large public ICU datasets with multiple seeds and ablations.
- Interpretable attention analysis that aligns with clinical expectations, aiding potential adoption.
- Sensible ablations showing contributions of the decay component.

Weaknesses
- Novelty is incremental; the idea of learned decay is close to GRU-D and prior time-aware attention variants, with limited positioning against recent continuous-time or transformer-based EHR models.
- Baseline tuning may not be fully comparable (baselines use original-paper hyperparameters rather than dataset-specific validation), which could understate their performance.
- Hourly binning may blunt very fine-grained irregularities; the benefit of per-variable decay over finer-grained event modeling is not fully explored.
- Retrospective-only evaluation; no external validation beyond ICU settings or prospective assessment.

Scores (0–100)
- Soundness: 80
  - Solid method and evaluation across two datasets with ablations; some concerns about baseline tuning and scope of comparisons.
- Novelty: 65
  - Conceptually incremental relative to GRU-D and interpretable attention literature; contribution is targeted and practical rather than fundamentally new.
- Significance: 74
  - Clinically important task with consistent, meaningful gains and interpretability; impact tempered by incremental nature and lack of broader model comparisons.
- Clarity: 85
  - Well written and easy to follow; could include more preprocessing and implementation detail for full reproducibility.

Final average score
- (80 + 65 + 74 + 85) / 4 = 76.0

Recommendation
- Accept

Justification
TimeWarn offers a practical, interpretable enhancement that consistently outperforms strong baselines on two widely used ICU datasets, with appropriate ablations and clinically sensible attention patterns. While the contribution is incremental and the baseline tuning could be more rigorous, the work is well-executed and likely to be useful to the community working on EHR-based early warning systems.