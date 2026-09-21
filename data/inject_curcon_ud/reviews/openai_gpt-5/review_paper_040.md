Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. During the unsupervised contrastive adaptation stage, CurCon linearly increases augmentation strength over training steps: starting with token dropout, then adding synonym replacement, span deletion, and finally back-translation. The approach is evaluated on four English classification datasets (SST-2, AG News, TREC, SUBJ) under a 500-labeled-examples regime using BERT-base. CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy gain of +1.1 over CERT and +3.8 over standard fine-tuning. Ablations indicate the curriculum contributes roughly 0.8 points on average, reversing the curriculum hurts, and removing back-translation reduces performance.

Strengths
- Clear and simple idea: progressively harder augmentations match curriculum learning intuitions for contrastive objectives.
- Solid empirical protocol for the presented scope: multiple baselines (UDA, SimCSE, CERT), five seeds, means and standard deviations, and ablations including reversed curriculum and operator removal.
- Consistent gains across four datasets, with larger improvements when labels are scarcer (100 vs 1,000 labels), supporting the main claim.
- Method is easy to implement, model-agnostic, and adds no inference overhead; clarity of the write-up is good.

Weaknesses
- Novelty is incremental: curricula for augmentation strength have been explored in vision contrastive learning; applying a similar schedule to text contrastive intermediate training is a modest extension. The schedule is hand-crafted and only toggles operator availability rather than continuously scaling augmentation intensities.
- Limited empirical breadth and potential fairness issues:
  - Only four small, well-trodden English classification datasets; no domain-diverse or longer-text settings, no multilingual evaluation, and only BERT-base is tested.
  - Hyperparameters for CurCon are tuned via grid search per dataset, while baselines use their originally reported settings, which may under-tune them relative to CurCon.
  - Gains are modest (average +1.1 over CERT) and often within 1–2 standard deviations on individual datasets; no statistical significance testing is provided.
  - Missing comparisons to stronger or more recent baselines for representation adaptation or semi-supervision (e.g., DeCLUTR/TSDAE, supervised SimCSE where labels exist, modern data augmentation or pseudo-labeling methods, or contemporary encoder baselines).
- Analysis depth is limited:
  - No exploration of alternative schedules (e.g., cosine, exponential), continuous strength within operators, or adaptive curricula.
  - No diagnostics on representation quality beyond classification (e.g., STS or retrieval), no analysis of negative sampling effects or temperature sensitivity beyond grid results.
  - Resource/compute and data usage details around back-translation could be clearer for reproducibility and cost fairness.

Questions for authors
- How sensitive are results to curriculum length L and temperature beyond the reported best values? Can you provide aggregated sensitivity plots?
- Do CurCon’s gains persist when baselines are also tuned on the same validation protocol?
- How does CurCon compare against TSDAE/DeCLUTR or more recent sentence-representation methods when used as intermediate training?
- Have you tried scaling within-operator strengths (e.g., gradually increasing token dropout percentage) rather than only gating operator availability?
- Any results with larger encoders (RoBERTa-large, DeBERTa) or on longer documents?

Scores (0–100)
- Soundness: 74
- Novelty: 60
- Significance: 62
- Clarity: 86

Final average score
- 70.5

Recommendation
- Reject

Rationale
The paper is clearly written and the idea is sensible, with consistent though modest gains and helpful ablations. However, the contribution is relatively incremental, the evaluation is limited in scope and may not be entirely fair due to asymmetric hyperparameter tuning, and the demonstrated improvements are small for a top-tier venue. Strengthening the empirical study (broader datasets, stronger/tuned baselines, larger models), adding analyses of alternative/learned schedules, and clarifying cost/fairness would substantially improve the case for acceptance.