Here is my review.

Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during self-supervised adaptation on unlabeled in-domain text, prior to fine-tuning. Using BERT-base on four low-resource text classification benchmarks (500 labeled examples), CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations suggest the curriculum accounts for ~0.8 points of the gain and that benefits are larger with fewer labels.

Strengths
- Simple, general idea that drops cleanly into existing CERT-style pipelines; no inference overhead.
- Consistent improvements over all baselines across four datasets and five seeds.
- Solid ablations: fixed mixture vs curriculum, reversed curriculum, effect of removing back-translation, and label-scarcity analysis.
- Clear description of schedule, operators, and training setup; results are easy to interpret.

Weaknesses
- Gains over the strongest baseline (CERT) are modest (~1.1 average), and per-dataset improvements are within 1–1.5 points with overlapping standard deviations; no statistical significance testing reported.
- Limited scope: only English, short-text datasets, and BERT-base. No results on larger encoders or decoder-only models.
- Potential hyperparameter fairness issue: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers, which may not be optimal in this low-resource, in-domain setting.
- Baseline coverage could be stronger (e.g., DeCLUTR, MixCSE, supervised SimCSE, or other augmentation curricula; consistency regularization with stronger text augmentations).
- Lacks sensitivity analyses (e.g., unlabeled data size, curriculum length beyond grid sweeps, operator probabilities, temperature/batch size).

Suggestions for improvement
- Add statistical significance tests and effect sizes.
- Tune baselines under the same validation-driven protocol for fairness.
- Broaden evaluation to larger encoders and at least one non-English or longer-text dataset.
- Include sensitivity to unlabeled data volume and curriculum length; consider adaptive/learned curricula.
- Compare against stronger contrastive baselines and augmentation curricula, and report robustness metrics (e.g., OOD shifts, perturbation tests).

Reproducibility
- Generally good: operators and schedule specified, training steps and optimizer provided, five seeds, and clear datasets. To strengthen, include exact unlabeled set sizes, data pass counts (epochs over unlabeled), code or pseudocode for the scheduler, and the full hyperparameter grids tried.

Ethical considerations
- Reasonable; relies on MT and WordNet. Note potential biases from translation systems and synonym resources.

Scores (0–100)
- Soundness: 82
- Novelty: 70
- Significance: 72
- Clarity: 88

Final average score
- (82 + 70 + 72 + 88) / 4 = 78.0

Recommendation
- Accept (borderline). The method is simple, clearly presented, and yields consistent, reproducible gains in a practically important low-resource setting, despite modest effect sizes and limited scope.