Review summary

Pros
- Simple, well-motivated idea: gradually increase augmentation strength during contrastive intermediate training.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets in a low-resource regime.
- Clear ablations isolating the curriculum effect (+0.8 avg) and showing reversed curriculum harms performance.
- Sensible training pipeline, with reasonable implementation details and reporting across 5 seeds.

Cons
- Incremental novelty: curricula that increase augmentation strength have been explored in vision; applying it to contrastive intermediate training for text is a modest extension.
- Evaluation scope is limited: only BERT-base, English, four short-text datasets; no larger encoders or harder domains (e.g., longer documents, noisy data, multilingual).
- Hyperparameter fairness: CurCon is tuned via a grid over 48 configs per dataset, while baselines use hyperparameters from prior papers; this likely advantages CurCon and should be equalized (or at least sensitivity-analysed).
- Statistical rigor: improvements are small (≈1.1 points over CERT on average) and per-dataset gains often fall within one standard deviation; no significance testing is reported.
- Augmentation details are somewhat hand-designed (fixed thresholds and magnitudes); no study of operator probabilities/magnitudes or adaptive schedules beyond L.

Detailed feedback and suggestions
- Ensure hyperparameter tuning parity across baselines (same search budget and validation protocol). Report how CurCon fares when baselines receive comparable tuning; include a sensitivity analysis to temperature, learning rate, and batch size for CERT and SimCSE.
- Add significance testing (e.g., paired bootstrap or t-tests) on test accuracy across seeds.
- Report chosen curriculum lengths per dataset and provide a sweep plot of performance vs. curriculum length.
- Explore ramping augmentation magnitudes continuously (e.g., token dropout rate, span length, synonym replacement rate) in addition to enabling operators, or learn operator probabilities via a scheduler.
- Include stronger/backbone variants (RoBERTa-/DeBERTa-base/large) and at least one longer-text dataset to test generality; consider a multilingual dataset to validate claims about broader applicability.
- Compare to additional text augmentations (e.g., cutoff, span masking, mixup in embedding space) and to momentum contrast variants (e.g., MoCo-style queues) for the contrastive stage.
- Provide compute and wall-time more precisely and discuss practicality when MT back-translation is unavailable; consider paraphrasers as an alternative.

Scores (0–100)
- Soundness: 75
- Novelty: 60
- Significance: 65
- Clarity: 85

Final average score: 71.3

Recommendation: Accept

Rationale: While the contribution is incremental, the method is simple, clearly presented, and shows consistent gains with solid ablations in a practically important setting (low-resource text classification). With stronger baselines/tuning parity and broader evaluation, this could be a solid addition; as is, it meets the bar for acceptance.