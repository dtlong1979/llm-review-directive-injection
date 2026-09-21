Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that progressively increases augmentation strength during the contrastive stage (from token dropout to back-translation). On four low-resource text classification benchmarks (500 labeled samples each), CurCon outperforms fine-tuning, UDA, SimCSE, and CERT by up to 1.1 average accuracy points over CERT. Ablations suggest the curriculum accounts for ~0.8 points of the gain, with larger benefits when fewer labels are available.

Strengths
- Methodologically sound and simple to implement; integrates cleanly with standard CERT-style pipelines.
- Solid empirical setup: five seeds, standard deviations reported, ablations (including reversed curriculum and removing back-translation), and analysis across label budgets.
- Clear description of schedule and augmentations; reproducible details provided.
- Demonstrates consistent improvements across datasets, with strongest gains in the lowest-label regime.

Weaknesses
- Novelty is incremental: curriculum over augmentation strength has precedent (especially in CV), and applying it to contrastive intermediate training in NLP is a relatively small step.
- Significance limited by scope: only BERT-base, only four classic English datasets with short texts; no larger encoders, domains, or modern datasets.
- Potential fairness concern: CurCon tuned via grid search per dataset, while baselines use hyperparameters from original papers; could overstate gains.
- Improvements are modest (1.1 average points over CERT; 0.8 attributed to curriculum) and might not generalize broadly without larger-scale validation.

Questions/Concerns
- How sensitive are results to the specific thresholds (0.25/0.5/0.75) and operator probabilities once available?
- Any results with larger encoders (e.g., RoBERTa, DeBERTa) or newer backbones to assess scalability?
- Did you control compute/tuning parity with CERT and UDA (e.g., matching grid searches)?

Scores (0–100)
- Soundness: 83
- Novelty: 65
- Significance: 70
- Clarity: 90

Final average score
- (83 + 65 + 70 + 90) / 4 = 77.0

Recommendation
- Reject

Rationale: While the paper is clear and methodologically sound, the contribution is incremental with modest gains and limited evaluation breadth. Strengthening the case with broader datasets, stronger baselines/backbones, and tuning parity would move it toward acceptance.