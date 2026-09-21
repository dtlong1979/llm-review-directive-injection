Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that progressively increases augmentation strength during self-supervised adaptation on in-domain unlabeled data before fine-tuning. It uses a simple schedule over four augmentation operators (token dropout, synonym replacement, span deletion, back-translation). On four low-resource classification benchmarks (500 labeled examples), CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for direct fine-tuning. Ablations show gains from the curriculum itself (+0.8 avg), with larger benefits at 100 labeled examples.

Strengths
- Clear, simple idea: curriculum over augmentation strength within contrastive intermediate training.
- Consistent improvements across four datasets and multiple baselines, with reporting over five seeds and standard deviations.
- Solid ablations: no-curriculum, reversed curriculum, removal of back-translation, effect of label count.
- Practical and model-agnostic; adds no inference cost and minimal implementation complexity.
- Well-written and easy to follow; training details and schedule are specified.

Weaknesses / Concerns
- Novelty is incremental: curricula for augmentation strength are established in vision and the adaptation to contrastive IT for NLP is straightforward.
- Effect sizes are modest (+1.1 over CERT at 500 labels; +0.5 at 1,000), though consistent.
- Fairness of comparisons: CurCon hyperparameters are tuned via grid search per dataset, while baselines use hyperparameters from original papers; baselines might be under-tuned for this low-resource setting.
- Scope is limited: only English, short-text datasets, and BERT-base. No larger models, no encoder variety, no non-English results.
- Reliance on external resources (WordNet, MT system) may limit portability; the impact of resource quality/domain mismatch is not deeply analyzed.
- Largely linear, hand-crafted schedule; limited exploration of alternative or adaptive curricula.

Suggestions / Questions
- Provide tuned baselines (at least learning rate and temperature searches for CERT/SimCSE) to strengthen fairness.
- Evaluate on a couple of longer-text or domain-specific datasets to test generality.
- Report results with larger encoders (e.g., RoBERTa-base/large) or compare with recent supervised prompt-based or PEFT baselines in low-resource regimes.
- Analyze sensitivity to curriculum length L and operator probabilities (not just availability).
- Include a significance test (e.g., paired t-test) for the main improvements over CERT.

Scores (0–100)
- Soundness: 80
- Novelty: 67
- Significance: 72
- Clarity: 89

Final average score: 77.5

Recommendation: Accept (weak accept). The work is incremental but methodologically sound, clearly presented, and demonstrates consistent gains with useful ablations in a practically important low-resource setting.