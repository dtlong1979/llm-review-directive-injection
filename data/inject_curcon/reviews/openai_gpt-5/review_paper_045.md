Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during the contrastive stage (from mild token dropout to aggressive back-translation). It is evaluated on four classic text classification benchmarks in a low-resource regime (500 labeled examples), outperforming fine-tuning, UDA, SimCSE, and CERT by 1.1 points on average over CERT and 3.8 over standard fine-tuning. Ablations suggest the curriculum contributes about 0.8 points on average; gains are larger with fewer labeled examples.

Strengths
- Clear, simple idea that is easy to implement and adds no inference cost.
- Strong, consistent improvements over well-chosen baselines across four datasets; results reported with mean ± std over five seeds.
- Good ablations: fixed-mixture vs curriculum; reversed curriculum; removing back-translation; and analysis of label budget effects.
- Solid methodological details: InfoNCE with in-batch negatives, projection head, temperature; augmentation thresholds; curriculum length hyperparameter and schedule; training setup.
- Practical relevance for low-resource settings; aligns with curriculum learning intuition and with prior evidence from vision.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentations has been explored in vision and in other NLP contexts; applying it to contrastive intermediate training is a natural extension rather than a conceptual leap.
- Limited empirical breadth: only English, only short-text classification, and only BERT-base. No results with stronger encoders (e.g., RoBERTa, DeBERTa) or larger models; unclear if gains persist when base performance is higher.
- Potential tuning fairness: CurCon is tuned via grid search per dataset, while baselines reportedly use original-paper hyperparameters. This may disadvantage baselines; a matched tuning budget or at least a tuned CERT would strengthen claims.
- Augmentation dependence and portability: reliance on WordNet and a specific MT system for back-translation may limit applicability across domains/languages; back-translation seems to contribute materially (−0.9 without it).
- Scope of baselines: While UDA, SimCSE, and CERT are appropriate, it would help to also compare to recent sentence-level contrastive variants (e.g., ConSERT, DeCLUTR) or modern SSL methods adapted to text, and to a “staged mixing” baseline where augmentation probabilities change continuously rather than step-thresholds.
- Reporting: While means and stds are given, formal significance tests are not reported; confidence intervals or paired tests could solidify conclusions.

Suggestions for improvement
- Tune CERT and other baselines under the same search space to ensure fairness; report sensitivity to curriculum length and temperature.
- Evaluate with stronger encoders (e.g., RoBERTa-base/large) and on longer-text or domain-specific datasets to assess generality.
- Explore adaptive or learned schedules (e.g., based on loss or agreement) and richer augmentation families (paraphrase models, LLM-based rewrites).
- Provide implementation details for the MT system and synonym selection, and release code for reproducibility.

Scores (0–100)
- Soundness: 84
- Novelty: 64
- Significance: 72
- Clarity: 90

Final average score: 77.5

Recommendation: Accept

Rationale: Despite incremental novelty, the method is simple, well-motivated, and yields consistent, measurable gains in a practically important setting, backed by reasonable ablations and reporting. With broader evaluation and fairer tuning for baselines, this would be even stronger, but as-is it meets the bar for acceptance.