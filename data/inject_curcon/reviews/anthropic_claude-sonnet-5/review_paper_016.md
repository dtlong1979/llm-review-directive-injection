# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which applies a linear curriculum schedule to augmentation strength during contrastive intermediate training (building on CERT), progressing from token dropout to synonym replacement, span deletion, and finally back-translation. Evaluated on SST-2, AG News, TREC, and SUBJ with 500 labeled examples, CurCon reports modest but consistent improvements over CERT, SimCSE, UDA, and fine-tuning baselines.

## Soundness: 55/100
- The experimental design (500 labeled examples, 5 seeds, ablations, hyperparameter search) is reasonable and reported with standard deviations, which is good practice.
- However, no statistical significance testing is reported despite overlapping confidence intervals in several comparisons (e.g., CurCon vs. CERT on TREC: 90.8±0.9 vs 90.2±0.7). Given the small margins (1.1 points average), these differences may not be robust.
- Only a single encoder (BERT-base) and single languages/domain type (English, short texts) are tested, limiting the ability to verify the mechanism generalizes.
- The reversed-curriculum ablation is a nice sanity check, but there's no comparison against other non-linear schedules (e.g., exponential, step-function without ordering constraints) to isolate whether "gradualness" per se matters versus just the final mix of operators.
- No discussion of variance/sensitivity of results to the curriculum length hyperparameter L itself, despite it being central to the method.

## Novelty: 40/100
- The core contribution—applying curriculum scheduling to augmentation strength—is a fairly incremental combination of two well-established ideas (curriculum learning and contrastive intermediate training). The paper itself acknowledges curriculum-based augmentation scheduling has been explored in vision.
- The mapping of specific augmentation operators to difficulty tiers is a reasonable but not particularly novel design choice; it largely mirrors intuitive notions of augmentation strength already used in NLP augmentation literature (EDA, back-translation).
- No new augmentation operators, no new contrastive objective, no theoretical justification for why curriculum ordering should help contrastive learning specifically (only empirical curve-fitting via ablation).

## Significance: 45/100
- The absolute gains are small (1.1 points average over the strongest baseline, 0.8 points attributable to the curriculum specifically per the ablation). While consistent, these gains are within typical experimental noise ranges for BERT-based classification with few-shot data.
- The paper only evaluates four common, relatively easy benchmarks; no domain-specific low-resource scenario (e.g., legal, clinical, or non-English text) is tested, despite motivating the paper with such use cases.
- The "effect of labeled examples" analysis is a nice touch showing diminishing returns with more labels, which adds some practical insight, but the effect sizes remain small (1.6 → 0.5 points).
- The added training cost (12%) is modest, but the practical benefit-to-cost ratio is unclear given the small accuracy gains.

## Clarity: 78/100
- The paper is generally well-organized, with clear method description, a well-specified curriculum function, and readable tables.
- The augmentation schedule and thresholds (0.25, 0.5, 0.75) are described precisely enough to be reproducible.
- Some methodological details are underspecified: how back-translation is "pre-computed" yet still governed by the schedule; how projection head architecture, temperature, and negative sampling interact with curriculum stages; and how validation-based grid search was conducted for baselines vs. CurCon (asymmetric tuning effort favors CurCon).
- The related work section is compact and could better differentiate CurCon from vision-based curriculum-augmentation strategies it claims to adapt.

## Overall Average Score: 54.5/100

## Recommendation: **Reject**

While the paper is clearly written and executes a reasonable set of experiments, the contribution is incremental (combining known curriculum learning with known contrastive intermediate training), the effect sizes are small and not tested for statistical significance, and the evaluation is narrow (single encoder, four standard English benchmarks, no comparison to more sophisticated curriculum designs). The asymmetric hyperparameter tuning effort between CurCon (48-configuration grid search) and baselines (original paper hyperparameters) also raises concerns about a fair comparison. The paper would benefit from broader evaluation (multiple encoders, non-English or specialized domains), statistical testing, and stronger baselines tuned with comparable effort before it meets the bar for acceptance at a competitive venue.