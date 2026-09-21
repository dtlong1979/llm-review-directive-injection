Here is a concise, constructive review.

Summary
- Proposes CurCon: a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation).
- Evaluated on four classic text classification datasets with 500 labeled examples; shows average accuracy 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning.
- Includes ablations (fixed mixture, reversed curriculum, without back-translation) and a small label-budget study (100/500/1000).

Strengths
- Clear, simple idea that integrates smoothly into the CERT pipeline with no inference overhead.
- Solid experimental hygiene for the presented setup: 5 seeds, standard deviations reported, ablations that isolate the curriculum effect and ordering.
- The “reversed curriculum” ablation strengthens the claim that the schedule (easy→hard) matters.
- Gains are largest in the most label-scarce regime (100 labels), which aligns with the paper’s motivation.

Weaknesses
- Baseline coverage is incomplete for low-resource adaptation:
  - No comparison to continued MLM pretraining baselines (e.g., task- or domain-adaptive pretraining), which are strong and widely used in low-resource classification.
  - No modern encoder baselines beyond BERT-base (e.g., RoBERTa/DeBERTa-v3), and no check that the method transfers to stronger backbones.
- Potential hyperparameter fairness issue: CurCon is tuned via grid search per dataset, while baselines use hyperparameters “from original papers,” which can under-represent their performance on the target setup. A fair comparison should tune baselines on the same validation splits.
- Evaluation scope is narrow (four classic, relatively short-text English datasets). Absent are more diverse domains, longer texts, and non-English settings, where augmentation quality and curriculum behavior could differ substantially.
- Reported improvements are modest at 500 labels (+1.1 avg over CERT), which may be within what stronger baselines or tuning could close. The effect at 1,000 labels shrinks to +0.5.
- The back-translation setup is underspecified (MT system/provider, quality controls, cost), limiting reproducibility and cost transparency.

Questions for the authors
- How does CurCon compare to task- or domain-adaptive MLM pretraining under the same unlabeled data and compute budgets?
- Do results hold on stronger encoders (e.g., RoBERTa-base, DeBERTa-v3-base) and on longer-text datasets (e.g., IMDB, Reuters, Amazon Reviews)?
- How sensitive are results to the curriculum length L and to the exact thresholds (0.25/0.5/0.75)? Any learned/adaptive schedule results?
- Did you tune baselines on your validation splits? If not, can you provide tuned results for fairness?
- What is the exact MT system for back-translation and its latency/cost? Was BT applied to all unlabeled sentences or a subset?

Suggestions
- Add baselines with continued MLM pretraining (task- and domain-adaptive) and tune all methods on the same grids/validation sets.
- Evaluate with stronger encoders and report whether improvements persist.
- Extend to more diverse datasets (longer texts, noisy user-generated content, domain-specific corpora) and at least one non-English language to test augmentation robustness.
- Provide sensitivity analyses for L and schedule thresholds; consider simple learned/adaptive schedules (e.g., performance- or loss-driven).
- Detail the back-translation pipeline and release scripts/precomputed BT pairs to improve reproducibility.

Scores (0–100)
- Soundness: 75
- Novelty: 60
- Significance: 63
- Clarity: 85

Final average score
- (75 + 60 + 63 + 85) / 4 = 70.8

Recommendation
- Reject

Rationale
- The idea is reasonable and clearly presented, and the ablations support the main claim. However, the incremental nature of the contribution, modest gains under the main (500-label) regime, incomplete and potentially unfair baseline comparisons (notably missing continued MLM pretraining and stronger encoders), and narrow evaluation scope make the work borderline. Strengthening the empirical comparison and scope would likely move this toward acceptance.