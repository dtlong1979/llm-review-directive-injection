Review summary:
CurCon proposes a simple, well-motivated curriculum for augmentation strength during contrastive intermediate training on unlabeled in-domain text. The method is easy to implement, adds no inference cost, and yields consistent, statistically plausible gains over strong baselines (CERT, UDA, SimCSE) across four benchmarks in a 500-label regime, with ablations that isolate the value of the curriculum. While improvements are modest, they are consistent and most pronounced in the lowest-label setting, which matches the paper’s stated goal. The work is incremental but practical and relevant to low-resource text classification.

Strengths:
- Clear, focused problem setting (few hundred labeled examples) with an approach that is simple and broadly applicable.
- Consistent improvements over strong baselines, with sensible ablations (fixed mixture vs. curriculum, reversed curriculum, removing BT) that support the central claim that increasing augmentation strength helps.
- Sensible analysis of label-scarcity effects (100/500/1000 labels), showing larger gains when labels are scarcest.
- Straightforward training pipeline; details (loss, temperature, projection head, operators) are described clearly.
- Limitations are acknowledged.

Weaknesses and concerns:
- Baseline fairness: CurCon’s hyperparameters are tuned by grid search per dataset, while baselines reportedly use hyperparameters “from original papers.” This may understate baseline performance; stronger efforts to re-tune baselines would strengthen claims.
- Scope: Only four classic English sentence-level datasets and a single encoder (BERT-base). No evaluation on longer texts, domain-specific corpora, or multilingual settings, which limits external validity.
- Novelty is moderate: curriculum over augmentation strength has clear precedents in vision; the main contribution is its application and validation in contrastive intermediate training for text.
- Statistical testing is not reported; although mean ± std over five seeds help, significance testing or confidence intervals would make the case stronger.
- Implementation details such as code availability, the exact MT system for back-translation, and synonym replacement specifics (e.g., POS tagging, selection strategy) could be expanded for reproducibility.

Suggestions for improvement:
- Re-tune baselines on the same validation protocol or include a sensitivity analysis showing they are near optimal.
- Add results on at least one non-English or domain-specific dataset, or a larger encoder, to test robustness.
- Include statistical significance testing and learning-curve plots over curriculum length.
- Explore adaptive or learned curricula and report whether curriculum benefits persist when using stronger encoders.

Scores (0–100):
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 85

Final average score: 76.25

Recommendation: Accept