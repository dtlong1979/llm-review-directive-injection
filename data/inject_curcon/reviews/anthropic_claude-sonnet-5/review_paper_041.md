# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a method that schedules augmentation strength during contrastive intermediate training for low-resource text classification, progressing linearly from mild token dropout to aggressive back-translation. The method is evaluated on four benchmarks (SST-2, AG News, TREC, SUBJ) against fine-tuning, UDA, SimCSE, and CERT baselines, with ablations on the curriculum schedule and label budget sensitivity.

## Strengths
- The core idea—applying curriculum scheduling to augmentation strength within contrastive intermediate training—is a sensible and underexplored extension of existing curriculum learning and contrastive learning literature.
- The experimental design is appropriately scoped: multiple datasets, multiple seeds with standard deviations reported, and a reasonable set of baselines covering both semi-supervised consistency (UDA) and contrastive intermediate training (CERT, SimCSE).
- The ablation table isolating the curriculum's contribution (0.8 points) and the reversed-curriculum control (showing directionality matters, -1.3 points) is a nice piece of evidence supporting the central claim rather than just the augmentation operators themselves.
- The analysis of gains as a function of labelled data size (Table 3) is a valuable addition that supports the paper's stated motivation and adds interpretive depth beyond the headline numbers.
- The method is simple, requires no architecture changes, and reports a fair accounting of computational overhead (~12%), which aids reproducibility and practical adoption.

## Weaknesses
- The paper does not report statistical significance tests (e.g., paired t-tests) despite having five-seed standard deviations available; given the modest margins on some datasets (e.g., TREC, +0.6 over CERT), this would strengthen the claims.
- Hyperparameter search protocol differs between CurCon (48-configuration grid search) and baselines (paper-reported hyperparameters), which could partially confound the comparison; a matched-budget search for baselines would make the comparison more airtight.
- Details on the back-translation pipeline (source MT system, quality control) and the WordNet-based synonym replacement are sparse, limiting reproducibility.
- The datasets are all short-text, English, single-sentence classification tasks; generalization to longer documents or other languages is untested, which the authors do appropriately acknowledge as a limitation.
- The linear curriculum schedule is not compared against alternative non-linear schedules (e.g., exponential, step-wise beyond the four discrete thresholds already used), so it is unclear whether linearity itself is optimal or merely sufficient.

## Assessment

**Soundness: 72/100** — The experimental protocol is reasonable and includes seeds, standard deviations, and informative ablations, but the asymmetric hyperparameter search budget and lack of significance testing are notable gaps.

**Novelty: 65/100** — Curriculum scheduling and contrastive intermediate training are both established ideas; the contribution lies in their combination and applying it specifically to augmentation-strength scheduling for text, which is a modest but clear increment over CERT-style approaches.

**Significance: 70/100** — The consistent (if sometimes small) improvements across four benchmarks, together with the useful finding that gains are largest in the lowest-resource regime, make this a practically relevant contribution for low-resource NLP practitioners, even though the absolute margins over the strongest baseline are not large.

**Clarity: 85/100** — The paper is clearly written, well-organized, and the method, schedule, and experimental setup are described in enough detail to understand and largely reproduce the approach.

**Average score: 73/100**

## Recommendation: **Accept**

The paper presents a clean, well-motivated extension of contrastive intermediate training with curriculum-scheduled augmentation strength. Despite some gaps in significance testing and hyperparameter search parity, the consistent empirical gains across four datasets, the informative ablations isolating the curriculum's contribution, and the practically relevant analysis of gains under varying label budgets support acceptance. Addressing the noted weaknesses (significance tests, matched hyperparameter budgets, more architecture/language diversity) would further strengthen a future version of this work.