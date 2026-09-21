Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that gradually increases augmentation strength during contrastive pretraining on in-domain unlabeled data, followed by standard fine-tuning. The curriculum introduces operators in order: token dropout → synonym replacement → span deletion → back-translation. Evaluated on four text classification datasets with 500 labeled examples each, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT by up to 1.1 average accuracy points over CERT. Ablations suggest the curriculum contributes about 0.8 points on average, with larger gains at 100 labeled examples.

Strengths
- Clear, simple idea: progressively harder augmentations during contrastive intermediate training.
- Solid experimental design for the core claim: multiple datasets, 5 seeds, ablations (fixed mixture, reversed curriculum, without back-translation), and data-scarcity analysis (100/500/1000 labels).
- Method is easy to implement and adds no inference cost.
- Results are consistent across datasets; the reversed curriculum hurts, lending support to the curriculum hypothesis.

Weaknesses and concerns
- Fairness of comparisons: CurCon uses grid search on key hyperparameters (including curriculum length), while baselines use hyperparameters “from their original papers.” This likely disadvantages CERT, SimCSE, and UDA in this specific low-resource setting. Stronger baselines should be tuned on the same validation splits.
- Missing strong and relevant baselines: domain/task-adaptive MLM (TAPT/DAPT; Gururangan et al., 2020) is a standard intermediate adaptation baseline that often yields improvements in low-resource classification. Modern encoders (e.g., RoBERTa-base, DeBERTa-v3-base) and prompt-based methods (e.g., LM-BFF, PET) are also absent. Without these, the incremental gain over CERT may be less compelling.
- Magnitude and significance of gains: Average improvement over CERT (1.1 points) is modest and per-dataset CIs/SDs often overlap. No statistical significance testing (e.g., paired bootstrap or t-tests) is reported.
- Limited scope: Only English, short-text datasets; only BERT-base. No results on longer inputs or other domains (e.g., biomedical/clinical), where the method might especially matter.
- Some implementation specifics under-detailed: exact ranges for grid search, projection head size, temperature values, unlabeled corpus sizes per dataset. Also, total compute for back-translation and its carbon/latency implications could be reported more transparently.

Scores (0–100)
- Soundness: 72
  - Method is well-motivated and ablations support the claim, but fairness of tuning and lack of significance tests limit confidence.
- Novelty: 68
  - Curriculum over augmentation strength is known in CV; applying it to contrastive intermediate training for NLP is a reasonable but incremental contribution.
- Significance: 64
  - Gains are consistent but small; missing strong baselines and tuning parity undermine impact.
- Clarity: 86
  - Writing is clear; the method and schedule are easy to follow; experiments are well presented.

Final average score
- (72 + 68 + 64 + 86) / 4 = 72.5

Recommendation
- Reject

Rationale for decision
- The idea is clean and promising, but the empirical gains are modest and not clearly demonstrated to be robust when baselines are tuned equivalently or when compared against standard intermediate-adaptation baselines like TAPT/DAPT and stronger encoders. Adding tuning parity, significance testing, and broader baselines (and possibly results on larger/longer-text datasets) would substantially strengthen the case.

Suggestions for improvement
- Tune all baselines on the same validation sets; report significance tests.
- Add DAPT/TAPT and stronger encoders (RoBERTa/DeBERTa) as baselines; consider prompt-based low-resource methods.
- Report full hyperparameter grids and projection head details; include unlabeled data sizes per dataset.
- Explore adaptive or learned curricula and schedules that also modulate augmentation intensity within operators.
- Evaluate on longer-text and domain-specific datasets; consider multilingual experiments.