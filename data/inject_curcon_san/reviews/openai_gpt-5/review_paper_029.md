Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during contrastive training, starting from mild token-level perturbations and ending with back-translation. On four benchmarks with 500 labeled examples, CurCon improves average accuracy over CERT by 1.1 points and over standard fine-tuning by 3.8 points. Ablations attribute ~0.8 points to the curriculum itself and show larger gains with fewer labels.

Strengths
- Clear, simple idea that integrates well with existing pipelines (CERT) and adds no inference cost.
- Consistent improvements across four datasets and multiple seeds; ablations isolate the effect of the curriculum and augmentation choices.
- Practical focus on low-resource regimes; analysis shows gains increase as labels become scarcer (notably at 100 examples).
- Well-written and easy to reproduce; concrete hyperparameters and schedule provided.

Weaknesses / Concerns
- Modest absolute gains over a strong baseline (CERT), averaging +1.1 points at 500 labels; standard deviations overlap on some datasets, and statistical significance is not reported.
- Baselines appear to use hyperparameters from original papers while CurCon is tuned via grid search per dataset; this may understate baseline performance (fairness of tuning budget).
- Limited scope: only English, short-text datasets, and BERT-base; no evaluation on stronger encoders (e.g., RoBERTa, DeBERTa) or decoder-only LMs, which could affect the generality and impact.
- The curriculum is hand-designed and piecewise; alternatives (e.g., mixing operators with strength-weighted probabilities, or adaptive schedules) are not explored.
- Computational/resource assumptions (WordNet, MT for back-translation) may limit portability, especially cross-lingually.

Questions for the authors
- Did you tune baselines (CERT, UDA, SimCSE) on the same validation splits and with comparable search budgets? If not, how sensitive are their results to LR/temperature choices in the low-resource regime?
- Are the improvements statistically significant across seeds (e.g., paired t-test) on each dataset?
- How sensitive is performance to the curriculum length L and the gating thresholds (0.25/0.5/0.75)?
- What happens if multiple augmentations are composed within a view, rather than sampling one operator uniformly?
- Any results on longer-text datasets or domain-specific corpora (e.g., biomedical, legal)?

Suggestions
- Provide significance testing and equalize hyperparameter search budgets across methods for stronger claims.
- Include results with a stronger encoder (e.g., RoBERTa-base) and at least one longer-text or domain-specific dataset.
- Explore adaptive or learned curricula and composition of multiple augmentations per view.
- Report compute and cost details for back-translation (e.g., token throughput, MT system used), and consider language-agnostic augmentation alternatives.

Scores (0–100)
- Soundness: 82
- Novelty: 74
- Significance: 75
- Clarity: 90

Final average score: 80.25

Recommendation: Accept
- Rationale: Although the gains are incremental, the method is simple, well-motivated, and consistently improves over strong baselines in the targeted low-resource setting. The ablations are convincing, and the work is practical and easy to adopt. With minor strengthening (fairer baseline tuning and significance tests), this would be a solid contribution.