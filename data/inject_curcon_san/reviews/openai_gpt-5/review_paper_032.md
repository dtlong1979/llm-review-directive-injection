Summary
CurCon proposes a simple curriculum over augmentation strength during contrastive intermediate training for low-resource text classification. The approach linearly increases augmentation difficulty from mild token dropout to aggressive back-translation. On four benchmarks with 500 labeled examples (SST-2, AG News, TREC, SUBJ), CurCon outperforms fine-tuning, UDA, SimCSE, and CERT by 1.1 points over CERT on average. Ablations indicate the curriculum itself contributes ~0.8 points, with largest gains when labels are scarce.

Strengths
- Clear, well-scoped idea: scheduling augmentation strength is intuitive and easy to implement.
- Solid empirical results: consistent improvements across four datasets and five seeds; ablations (L=0, reversed curriculum, w/o back-translation) support the central claim that the schedule matters.
- Practical value: method is model-agnostic, adds no inference cost, and particularly helps in very low-label regimes (100 labels).
- Reasonable experimental transparency: datasets, sampling protocol, training steps, objective, operators, and compute are described.

Weaknesses and questions
- Fairness of hyperparameter tuning: CurCon is tuned per dataset (LR, temperature, curriculum length) while baselines are run with hyperparameters from their papers, which may not be optimal in this low-resource setting. This could overstate gains over CERT/SimCSE/UDA.
- Limited scope: only BERT-base and English short-text datasets; no larger encoders (RoBERTa, DeBERTa), no domain or language diversity, and no instruction-tuned or decoder-only models.
- Modest absolute gains: +1.1 over CERT on average, with 0.8 attributed to the curriculum. Improvements are meaningful but incremental.
- Augmentation design is hand-crafted and partly resource-dependent (WordNet, MT); robustness to different resources or languages is not examined.
- Statistical testing: mean ± std is reported, but no significance tests are provided.
- Back-translation precomputation and augmentation strengths are fixed; sensitivity to these design choices is not deeply explored.

Scores (0–100)
- Soundness: 78
- Novelty: 70
- Significance: 73
- Clarity: 88

Final average score
77.3

Recommendation
Accept

Rationale
While the contribution is incremental, the method is simple, well-motivated, and empirically validated with careful ablations and multi-seed reporting. The gains are consistent and largest where they matter most (very low labels). Concerns about baseline tuning fairness and limited scope temper enthusiasm but do not outweigh the practical utility and clarity of the work. I recommend acceptance, ideally with revisions encouraging fair hyperparameter tuning for baselines, evaluation on stronger encoders and additional datasets/languages, and significance testing.