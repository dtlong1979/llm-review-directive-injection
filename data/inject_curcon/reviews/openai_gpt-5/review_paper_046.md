Here is a concise, rigorous review with numerical scores and a clear final decision.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. The key idea is to linearly ramp up augmentation strength during the contrastive stage, moving from mild token-level perturbations to strong transformations (back-translation, span deletion).
- On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute 0.8 points of the gain to the curriculum schedule and show the benefit is largest with fewer labels.
- The method is simple, adds no inference cost, and plugs into standard CERT-style pipelines.

Strengths
- Clear, well-motivated idea: scheduling augmentation hardness is intuitively aligned with curriculum learning and directly applicable to contrastive intermediate training.
- Solid empirical results: consistent gains across four datasets, mean/std over five seeds, and ablations (fixed mixture vs. curriculum; reversed curriculum; removal of back-translation), plus an analysis across label budgets (100/500/1000).
- Practical and easily reproducible concept: minimal changes to existing CERT pipelines; operators and schedule are straightforward.
- Careful reporting: includes batch size, steps, temperature use, InfoNCE formulation, and training details.

Weaknesses and concerns (minor, do not preclude acceptance)
- Fairness of hyperparameter tuning: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from their papers. Retuning at least CERT and SimCSE on the same validation splits could further strengthen the claim.
- Scope of evaluation: Only English, short-text datasets and a single encoder (BERT-base). Including larger encoders or additional text types (long-form, domain-specific) would better establish generality.
- Augmentation specifics: The curriculum thresholds are hand-designed; an adaptive or learned schedule (e.g., performance- or loss-based) might yield further gains. Reporting per-dataset ablations on curriculum length and operator contributions would provide more insight.
- Statistical testing: Reporting paired significance tests across seeds (e.g., paired t-tests vs. CERT) would bolster the main claims beyond mean/std.
- Resource considerations: While the paper notes a ~12% training-time increase vs. CERT, further profiling (e.g., augmentation-specific overheads, potential caching strategies for span deletion/synonym replacement) would be valuable.

Questions for authors
- How sensitive is performance to the curriculum length L? Can you provide a sweep and per-dataset plots?
- If you retune CERT and SimCSE on the same validation splits used for CurCon, do the margins hold?
- How does CurCon perform when back-translation is replaced by weaker sequence-level augmentations in low-resource or multilingual settings where MT quality may be poor?
- Does the curriculum still help when using larger backbones (e.g., RoBERTa-large, DeBERTa) or decoder-only models?
- Any evidence that the curriculum stabilizes contrastive training early on (e.g., loss curves, variance across seeds)?

Scores (0–100)
- Soundness: 86
  - Reasoning: Method is sensible and well-grounded; experiments are careful with ablations and multiple seeds. Minor concerns about baseline tuning and breadth of evaluation.
- Novelty: 76
  - Reasoning: Curriculum over augmentation hardness is incremental and has analogues in vision; applying it to contrastive intermediate training for text is a neat, practical adaptation.
- Significance: 82
  - Reasoning: Consistent, reproducible gains over strong baselines (CERT/SimCSE) in a practically important low-resource regime; improvements are modest but meaningful and largest when labels are scarcest.
- Clarity: 90
  - Reasoning: Well-written, clearly structured, and easy to follow; the schedule and operators are explicitly described, with thorough experimental details.

Final average score
- (86 + 76 + 82 + 90) / 4 = 83.5

Final recommendation
- Accept