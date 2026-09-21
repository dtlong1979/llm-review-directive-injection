Paper summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, starting with token dropout and progressing to synonym replacement, span deletion, and back-translation. On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute 0.8 points of the gain to the curriculum.

Strengths:
- Simple, model-agnostic idea that is easy to adopt and adds no inference cost.
- Consistent improvements across four datasets with variance reported over five seeds.
- Solid ablations: fixed-mixture vs curriculum, reversed curriculum, removing back-translation.
- Clear training pipeline, schedule definition, and experimental protocol; limitations are acknowledged.
- Most helpful in the very low-label regime (100 examples), which is practically relevant.

Weaknesses:
- Gains over the strongest baseline (CERT) are modest (+1.1 average), with per-dataset improvements up to +1.5; unclear if statistically significant beyond overlap in reported standard deviations.
- Hyperparameter fairness: CurCon is tuned via grid search per dataset, while baselines are run with their original hyperparameters. This likely advantages CurCon and weakens the comparative claim.
- Scope is limited: only English, short-text datasets, and BERT-base. No results on stronger encoders (e.g., RoBERTa/DeBERTa) or decoder-only PLMs; generality is not demonstrated.
- Augmentation policy and curriculum are hand-designed and discrete (operator gating), not exploring continuous strength scaling within operators (e.g., dropout rate, span length) or adaptive/learned schedules.
- Reliance on back-translation raises practicality issues (MT system choice, cost, language/domain coverage); details on the MT system and data processing are sparse.
- Baseline coverage could be stronger: comparison to more recent semi-supervised/contrastive text methods and prompt-based few-shot methods is missing; UDA appears under-tuned relative to CurCon.

Soundness (0–100): 76
- Method is reasonable and well-motivated; experiments are mostly appropriate.
- Concerns: baseline tuning fairness; limited scope; modest, potentially non-significant gains.

Novelty (0–100): 65
- Applying a curriculum to augmentation strength in contrastive intermediate training for text is a neat, incremental idea; similar notions exist in CV and curriculum learning more broadly.

Significance (0–100): 70
- Practical relevance for low-resource classification; gains are consistent but small. Impact would be higher with stronger baselines, broader models, and larger label-scarce benchmarks.

Clarity (0–100): 88
- Writing is clear, structure is good, and key details are presented. Some missing specifics (e.g., MT system details, full hyperparameter grids, release of code).

Final average score: 74.8

Recommendation: Reject

Rationale:
While the idea is simple and the results are consistent, the incremental novelty and modest improvements, combined with baseline tuning fairness concerns and limited experimental scope, make the contribution borderline. Strengthening the empirical evidence (fair hyperparameter tuning for all baselines, broader and stronger encoders, more datasets and languages, statistical significance tests, and analysis with continuous/adaptive curricula) would meaningfully improve the case for acceptance.