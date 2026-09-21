# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which schedules augmentation strength during contrastive intermediate training (following the CERT pipeline), moving from mild token dropout to aggressive back-translation over a curriculum length L. The method is evaluated on four text classification benchmarks under a 500-label setting, showing consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with ablations isolating the curriculum's contribution and a labelled-data-scaling analysis.

## Strengths
- The core idea—applying curriculum learning to augmentation strength within a contrastive intermediate training stage—is a sensible and underexplored combination, clearly motivated by analogy to curriculum strategies in vision.
- The experimental design is reasonably thorough for the scope of the paper: four datasets, five baselines/comparisons, five seeds with reported standard deviations, and an ablation table that isolates the curriculum's contribution (0.8 points) from the contribution of back-translation and tests a reversed-curriculum control, which is a good sanity check.
- The scaling analysis with 100/500/1000 labelled examples supports the paper's central claim (larger gains in lower-resource regimes) with a plausible and consistent trend.
- The method is simple, requires no architectural changes, and adds negligible inference cost, which supports practical adoption.
- Limitations are honestly acknowledged (English-only, BERT-base only, dependence on WordNet/MT quality, hand-designed linear schedule).

## Weaknesses
- Gains over CERT, while consistent, are numerically modest (1.1 points average), and no statistical significance testing (e.g., paired t-test across seeds) is reported to confirm the improvements exceed noise, despite standard deviations being available.
- The paper does not report results for multiple curriculum lengths L beyond the selected optimum, so the sensitivity of the method to this key hyperparameter is not fully characterized.
- The novelty is incremental: it combines two well-established ideas (contrastive intermediate training and curriculum scheduling) rather than introducing a fundamentally new mechanism; the thresholds (0.25/0.5/0.75) for operator introduction appear heuristic and are not ablated.
- Only BERT-base is tested; it is unclear whether findings generalize to larger or more modern encoders.
- The description of augmentation operators and schedule is clear, but exact grid-search ranges and selected hyperparameters per dataset are not reported, limiting reproducibility.

## Assessment

**Soundness: 72/100**
The experimental protocol (multiple seeds, ablations, scaling study) is reasonably rigorous, but the absence of significance testing and limited hyperparameter sensitivity analysis leave some open questions about robustness of the reported gains.

**Novelty: 60/100**
The contribution is a reasonable but incremental extension combining existing curriculum-learning and contrastive-intermediate-training ideas; the specific scheduling mechanism is simple and its design choices are not deeply justified or explored.

**Significance: 68/100**
The consistent, if modest, improvements in the low-resource regime are practically relevant given the low cost of adoption (no added parameters, minor training overhead), and the finding that gains are largest when labels are scarcest is a useful, actionable insight for practitioners.

**Clarity: 82/100**
The paper is clearly written, with a well-structured method description, explicit schedule formula, and readable tables that make the empirical claims easy to follow.

## Final Average Score: 70.5/100

## Recommendation: **Accept**
The paper presents a clear, well-motivated, and practically simple method with consistent empirical improvements across datasets and a thoughtful ablation and scaling analysis. While the novelty is incremental and some robustness checks (significance testing, hyperparameter sensitivity) are missing, the overall contribution is solid and clearly presented, meriting acceptance.