Review

Summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during contrastive adaptation on in-domain unlabeled text before fine-tuning. Using BERT-base on four classic text classification datasets with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute ~0.8 points to the curriculum itself, with larger gains when labels are scarcer.

Strengths:
- Clear, simple idea: progressively strengthen augmentations during contrastive pre-adaptation.
- Solid experimental hygiene: five seeds, ablations (fixed mixture, reversed curriculum, operator removal), and label-scarcity analysis.
- Consistent gains over reasonable baselines (Fine-tuning, UDA, SimCSE, CERT), with the largest benefits in the lowest-label setting.
- Well-written and easy to follow; implementation details and limitations are stated.

Weaknesses:
- Novelty is incremental: curricula for augmentation strength are known in vision, and contrastive intermediate training for NLP is established; combining the two is a modest contribution.
- Significance is limited by small absolute gains (+1.1 over CERT on average) on comparatively easy, small, and well-trodden benchmarks; restricted to English and BERT-base.
- Potential fairness concern: CurCon hyperparameters are tuned via grid search per dataset, while baselines use hyperparameters “as reported,” which may be suboptimal in this low-resource regime. Equal hyperparameter search for baselines would strengthen the case.
- Missing comparisons to stronger or more recent baselines (e.g., DeCLUTR, modern sentence embedding methods, supervised contrastive fine-tuning, prompt-based/few-shot approaches with modern encoders) and to larger encoder backbones (e.g., RoBERTa-large).
- No statistical significance testing across seeds for the small deltas reported.

Suggestions for Improvement:
- Apply the same hyperparameter tuning budget to all baselines or report sensitivity analyses to address fairness.
- Expand evaluation to harder and more diverse datasets (longer text, domain-specific, non-English) and to larger/modern encoders.
- Include statistical tests across seeds for main results.
- Explore adaptive/learned schedules and alternative curriculum shapes; add sensitivity plots for curriculum length and operator thresholds.
- Compare to supervised contrastive fine-tuning and more recent sentence representation methods; report compute and data efficiency trade-offs more comprehensively.

Scores (0–100):
- Soundness: 80
- Novelty: 65
- Significance: 62
- Clarity: 89

Final average score: 74.0

Recommendation: Reject

Rationale: The paper is clear and technically sound with sensible ablations, but the contribution is incremental and the empirical gains are modest on limited benchmarks, with some fairness concerns in hyperparameter tuning. With broader evaluation, stronger baselines, and equalized tuning, this work could be better positioned for acceptance.