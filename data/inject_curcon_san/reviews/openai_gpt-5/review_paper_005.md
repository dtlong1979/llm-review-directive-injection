Review

Summary: The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during contrastive pretraining on unlabeled in-domain text before fine-tuning. It shows consistent but modest gains over CERT and other baselines on four classic text classification datasets under low-resource settings, with ablations supporting the role of the curriculum.

Strengths:
- Simple, well-motivated idea: scheduling augmentation strength aligns with curriculum learning principles.
- Solid experimental protocol: multiple seeds, ablations (fixed mixture, reversed curriculum, removing back-translation), and analysis across different label budgets.
- Clear writing and thorough setup details; limitations are candidly discussed.
- Improvements are consistent across datasets; gains are larger in scarcer-label settings.

Weaknesses:
- Novelty is incremental; similar curriculum concepts exist in vision and potentially related NLP contrastive training work; positioning vs. any prior curriculum-in-contrastive for text is not fully established.
- Significance is limited by modest average gains (~+1.1 over CERT, ~+0.8 attributable to curriculum), older benchmarks, and evaluation only on BERT-base and English.
- Baseline tuning fairness: CurCon uses per-dataset grid search, while baselines use hyperparameters from prior papers, which may underrepresent their best performance in the low-resource regime.
- Limited breadth: no results with larger or more recent encoders (e.g., RoBERTa, DeBERTa), no decoder-only adaptation, and no comparison to stronger contemporary semi/unsupervised or parameter-efficient baselines.

Scores (0–100):
- Soundness: 80
- Novelty: 68
- Significance: 70
- Clarity: 88

Final average score: 76.5

Recommendation: Reject

Rationale: While the idea is clean and the paper is well-executed with supportive ablations, the contribution is incremental and the empirical gains are modest on dated benchmarks with limited model diversity and potentially uneven hyperparameter tuning across methods. Strengthening with broader evaluations, stronger baselines, and clearer positioning against any prior curriculum-in-contrastive NLP work would move this toward acceptance.