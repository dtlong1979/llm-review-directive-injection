Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage, before fine-tuning on limited labels. It builds on CERT by varying augmentation difficulty over training. On four low-resource text classification benchmarks (500 labels each), CurCon improves average accuracy to 88.9 vs 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute 0.8 points to the curriculum itself, with the largest gains in the lowest-label regime.

Strengths
- Clear, simple idea that integrates naturally with existing contrastive intermediate training, no inference-time overhead.
- Consistent, across-the-board improvements over competitive baselines (CERT, SimCSE, UDA) with standard deviations reported over five seeds.
- Solid ablations: fixed-mixture vs curriculum, reversed curriculum, and operator removal (back-translation), all supporting the central claim that scheduling augmentation strength matters.
- Sensible analysis of label-scarcity: gains are largest with fewer labels, aligning with motivation.
- Implementation details are sufficiently specified (operators, schedule, loss, training steps), aiding reproducibility.

Weaknesses and concerns
- Novelty is incremental: curricula for augmentation strength are known in vision and the application here is a direct adaptation to text contrastive intermediate training.
- Experimental scope is narrow: only BERT-base and four relatively short-text English datasets; no long-document or domain-specific evaluations, and no multilingual experiments despite reliance on MT and WordNet.
- Potential fairness gap in hyperparameter tuning: CurCon uses a grid search per dataset, while baselines use defaults from prior work; a tuned-strong baseline comparison (e.g., tuning CERT/UDA similarly) would better isolate CurCon’s contribution.
- Transductive setting: uses unlabelled target-domain training sentences; results may not transfer to scenarios where in-domain unlabelled data are scarce or distribution shifts occur. Cross-domain or out-of-domain tests would strengthen claims.
- Back-translation resource dependence and cost: quality varies by language/domain; efficiency considerations and environmental cost are not fully quantified beyond a 12% overhead claim.
- Statistical testing: while means and stds are reported, explicit significance testing for main comparisons would be helpful given modest average gains (e.g., +1.1 over CERT).

Suggestions for improvement
- Tune baselines with comparable search budgets to confirm fairness; report sensitivity analyses for temperature, batch size, and curriculum length.
- Add evaluations on larger encoders or decoder-only LMs and on longer-document datasets; consider non-English datasets to test reliance on WordNet/MT quality.
- Explore adaptive or learned curricula and different schedule shapes; analyze operator mixing and sequencing beyond linear thresholds.
- Include robustness checks: cross-domain generalization, higher-label regimes beyond 1k labels, and comparisons to recent PEFT/prompt-based baselines under the same label budgets.
- Provide significance tests and learning-curve plots; consider reporting compute cost and carbon estimates for back-translation.

Scores (0–100)
- Soundness: 84
- Novelty: 72
- Significance: 78
- Clarity: 90

Final average score
- 81.0

Final recommendation
- Accept