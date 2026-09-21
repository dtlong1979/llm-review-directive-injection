Here is my review.

Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, progressing from token dropout to synonym replacement, span deletion, and finally back-translation. On four English benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9, outperforming CERT (87.8) and standard fine-tuning (85.1). Ablations suggest the curriculum contributes about 0.8 points on average, and gains are larger with fewer labels.

Strengths
- Clear, simple method that integrates cleanly with standard contrastive intermediate training and adds no inference cost.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets; averaged over five seeds with reported standard deviations.
- Thoughtful ablations: curriculum vs fixed mixture, reversed curriculum, removal of back-translation, and sensitivity to number of labeled examples.
- Solid experimental protocol for the stated scope (in-domain unlabeled, low-resource fine-tuning).

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentation strength is well-established in vision and curriculum concepts in NLP; applying it specifically to contrastive intermediate training for text is a modest extension.
- Significance is limited by scope and magnitude of gains: improvements over CERT are small (typically 0.5–1.5 points) and sometimes within one standard deviation; no statistical significance tests are reported.
- Baseline fairness and tuning: CurCon hyperparameters are tuned per dataset via grid search, while baselines are run with their original hyperparameters, which may disadvantage them. A tuned CERT baseline and tuned fixed-mixture controls would strengthen claims.
- Dataset and model scope: only short-text English benchmarks and BERT-base are used. Results may not generalize to longer documents, other languages, domains, or larger encoders.
- Potential confound: the integrated augmentation distribution over training is different between curriculum vs fixed mixture. A control that matches the overall augmentation budget (e.g., time-averaged operator use) would isolate the effect of scheduling from mere changes in average augmentation strength.
- Limited analysis of schedule design: only linear scheduling is tested; there’s no exploration of adaptive or non-linear schedules or schedule-length sensitivity beyond grid search.

Questions and suggestions
- Report tuned CERT and tuned fixed-mixture results under the same grid as CurCon to ensure fairness.
- Provide statistical significance testing across seeds (e.g., paired tests).
- Control for augmentation exposure: match the aggregate probability mass per operator between CurCon and fixed-mixture baselines over T steps.
- Evaluate on additional and harder datasets (e.g., longer documents, domain-specific corpora), larger encoders, and a multilingual case to test robustness and generality.
- Explore schedule variants (non-linear, adaptive) and sensitivity to curriculum length with fewer/more steps.
- Include a stronger set of contrastive baselines (e.g., DeCLUTR, TSDAE) and supervised contrastive fine-tuning.
- Release code and augmentation resources to improve reproducibility.

Scores (0–100)
- Soundness: 76
- Novelty: 60
- Significance: 65
- Clarity: 85

Final average score: 71.5

Recommendation: Reject

Rationale: The work is clear and technically sound with consistent but modest gains. However, the novelty is limited, the empirical improvements over tuned strong baselines are not conclusively established, and the scope is narrow. With stronger fairness controls, broader evaluation, and deeper analysis of the curriculum design, this could become a solid contribution.