# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which adds a linear curriculum schedule over augmentation strength (token dropout → synonym replacement → span deletion → back-translation) to CERT-style contrastive intermediate training. It reports gains over fine-tuning, UDA, SimCSE, and CERT on four text classification benchmarks under a 500-label setting, with ablations on the schedule and on labelled-data quantity.

## Soundness: 45/100
- The core experimental design (single low-resource setting, 5 seeds, standard deviations reported) is reasonable in principle, but there are no statistical significance tests, and the margins over CERT (~1.1 avg, with per-dataset gaps like 0.6–1.5) are comparable to or smaller than the reported standard deviations (0.6–0.9), making it unclear whether the improvements are significant.
- Only one encoder (BERT-base) and one run of hyperparameter search per method is described; baselines use "original paper" hyperparameters rather than being tuned with the same budget as CurCon (48 configurations), which risks an unfair comparison favoring CurCon.
- The paper provides no implementation details sufficient for reproducibility (e.g., WordNet substitution specifics, back-translation model, exact optimizer settings, learning rates found).
- The ablation is informative but minimal — no confidence intervals or seed variation reported for ablation numbers, so the 0.8-point "curriculum contribution" claim is not statistically substantiated.
- The "reversed curriculum" and "without back-translation" ablations are useful but the paper doesn't explore other schedule shapes (e.g., exponential, step-wise) to justify that linear scheduling is optimal, despite explicitly flagging this as a limitation.

## Novelty: 40/100
- The core idea — applying curriculum learning to augmentation strength within a contrastive learning pipeline — is a fairly incremental combination of two well-established ideas (curriculum learning and contrastive intermediate training/CERT). Curriculum-style augmentation scheduling has already been explored in vision (as the paper itself acknowledges).
- The application to text with a specific operator ordering (dropout → synonym → span deletion → back-translation) is a reasonable but narrow instantiation, not a fundamentally new mechanism.
- No new augmentation operators, loss functions, or theoretical justification for why this specific curriculum ordering should help are introduced beyond intuition.

## Significance: 42/100
- The paper addresses a practically relevant problem (low-resource text classification) and the empirical improvement pattern (larger gains with fewer labels) is a nice, interpretable finding.
- However, absolute gains are modest (1.1 points average over the strongest baseline), and the method adds complexity and ~12% additional training time for a benefit that may not be significant given the variance.
- The scope is narrow: only BERT-base, English, short-text classification datasets, no comparison to more modern approaches (e.g., prompt-based few-shot methods, larger PLMs) that are increasingly standard in low-resource literature.
- Community impact is likely limited unless the curriculum framework generalizes to other tasks/architectures, which is not demonstrated.

## Clarity: 78/100
- The paper is generally well-written, well-organized, and easy to follow. The method description (curriculum schedule formula, thresholds for operator availability) is precise and reproducible in principle.
- Tables are clear and results are presented straightforwardly with appropriate discussion.
- Some details are missing (e.g., exact grid search ranges, why these specific curriculum thresholds of 0.25/0.5/0.75 were chosen, statistical testing procedure), which slightly hurts full reproducibility and interpretability of the significance of results.
- The limitations section is honest and appropriately scoped.

## Overall Average Score: **51.25/100**

## Final Recommendation: **Reject**

While the paper is clearly written and tackles a relevant problem, the contribution is incremental (a curriculum wrapper around an existing method, CERT), the empirical gains are modest and not clearly statistically significant relative to reported variance, and the evaluation is narrow in scope (single encoder, English-only, no significance testing, unequal hyperparameter search budgets between CurCon and baselines). The paper would benefit from significance testing, broader baselines/encoders, and more ablations on the schedule shape before being ready for publication at a top venue. As a workshop or short paper with corrected experimental rigor, it could be reconsidered.