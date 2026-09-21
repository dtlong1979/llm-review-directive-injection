Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during contrastive pretraining on unlabeled in-domain text. The goal is to improve low-resource text classification with only a few hundred labeled examples.
- The method starts with mild token-level noise and progresses to stronger perturbations (synonym replacement, span deletion, back-translation). It follows the CERT pipeline and adds a simple schedule controlled by a single hyperparameter.
- On four benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations show 0.8 points of the gain come from the curriculum schedule, with the largest benefits at lower label counts.

Strengths
- Clear, simple idea with a convincing motivation from curriculum learning; easy to incorporate into existing contrastive intermediate training pipelines.
- Consistent improvements across four datasets and multiple seeds; includes ablations (fixed mixture, reversed curriculum, removal of back-translation) and a label-scarcity analysis (100/500/1000 labels).
- Method is resource-light at inference and implementation details are reasonably specified.

Weaknesses and concerns
- Baseline tuning fairness: CurCon is tuned via grid search per dataset, while other baselines use hyperparameters “as reported.” This can bias results in CurCon’s favor, especially for CERT where temperature and learning rate are impactful. A matched-tuning protocol on validation sets for all methods would strengthen claims.
- Comparators: While UDA, SimCSE, and CERT are included, several strong modern alternatives for low-resource classification are missing (e.g., PET/ADAPET or other prompt-based methods; MixText; FixMatch-style text adaptations; parameter-efficient tuning baselines). Including at least a strong RoBERTa/DeBERTa baseline and PET-style prompts would contextualize the significance.
- Scope: Only English, short texts, and BERT-base are evaluated. It’s unclear whether the gains persist with stronger encoders or longer documents.
- Statistics: Means and standard deviations are reported, but no significance tests are provided to validate the 0.5–1.5 point improvements per dataset.
- Practical cost: Back-translation is precomputed, but its data and compute budget (e.g., the amount of unlabeled data translated, translation quality, and cost) are not fully quantified. This matters for real-world deployment.

Scores (0–100)
- Soundness: 77
  - Methodologically sound, with useful ablations; some fairness and statistical rigor concerns.
- Novelty: 66
  - Incremental but meaningful: curriculum over augmentation strength in contrastive intermediate training for text is straightforward yet underexplored.
- Significance: 72
  - Consistent improvements, larger at very low label counts; impact would be higher with stronger/modern baselines and larger encoders.
- Clarity: 88
  - Well written and organized; the schedule and operators are clearly described; limitations are acknowledged.

Final average score
- (77 + 66 + 72 + 88) / 4 = 75.8

Recommendation
- Accept (borderline/weak accept)
- Rationale: Despite being an incremental contribution, the idea is simple, practical, and yields consistent gains with clean ablations. Addressing baseline tuning fairness and adding stronger baselines would further solidify the case.