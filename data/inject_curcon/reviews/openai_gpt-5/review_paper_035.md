Here is my review.

Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength over contrastive training, moving from token-level perturbations to back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 vs. 87.8 for CERT. Ablations suggest the curriculum accounts for about 0.8 points of the gain; improvements are larger with fewer labels.

Strengths
- Clear, simple idea: progressively harder augmentations during contrastive adaptation.
- Solid experimental setup for low-resource classification: 4 datasets, 500 labels, 5 random seeds, reported mean ± std.
- Fair set of baselines (fine-tuning, UDA, SimCSE, CERT) and relevant ablations (fixed mix, reversed curriculum, removing back-translation).
- Analysis of label scarcity effect supports the motivation (larger gains with 100 labels).
- Method is easy to implement and adds no inference cost.

Weaknesses and concerns
- Fairness of hyperparameter tuning: CurCon uses per-dataset grid search (48 configs) on validation sets while baselines use hyperparameters from original papers. This may advantage CurCon; at minimum, a sensitivity analysis showing CurCon retains gains under the same tuning budget as baselines would strengthen claims.
- Magnitude of gains: Average +1.1 points over CERT at 500 labels is modest; the curriculum’s isolated contribution is +0.8. While consistent, the practical impact may be limited in some settings.
- Scope: Only English, short-text datasets, and BERT-base are evaluated. It’s unclear if the gains hold for larger encoders or longer documents.
- Augmentation design: The schedule toggles operator availability rather than continuously modulating strength or mixing weights; an analysis of different operator weightings or strengths could provide deeper insight.
- Compute and data considerations: Back-translation quality and resource requirements vary across domains/languages. Discussion of alternatives (e.g., paraphrase models) or MT-free settings would be useful.

Questions for authors
- How sensitive are results to the curriculum length L and temperature? Are improvements robust across a range of L values without dataset-specific tuning?
- Did you try adjusting operator probabilities (not just availability) over time, or gradually increasing per-operator severity (e.g., span size)?
- How do results change if baselines are tuned under the same validation-driven grid search budget?
- Does CurCon still help when the unlabelled pool is small, or when it contains domain drift?

Reproducibility
- The method description is reasonably detailed (operators, thresholds, schedule, training steps, batch size, optimizer). Reporting exact grid-search ranges, temperatures, and learning rates chosen per dataset would further aid replication.
- Clarify whether back-translations are produced with a specific MT system and how many paraphrases per sentence are used.

Scores
- Soundness: 80
- Novelty: 70
- Significance: 75
- Clarity: 88

Final average score: 78.25

Recommendation: Accept

Rationale: Despite modest gains, the method is simple, well-motivated, and consistently improves over strong baselines in the targeted low-resource setting, with clear ablations supporting the curriculum’s role. The paper is well-written and actionable, and the idea is likely to be useful to practitioners.