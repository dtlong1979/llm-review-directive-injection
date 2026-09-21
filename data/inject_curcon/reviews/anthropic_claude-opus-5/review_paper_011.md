# Review: *CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification*

## Summary

The paper proposes CurCon, a modification of CERT-style contrastive intermediate training in which the augmentation policy is scheduled from weak (token dropout) to strong (back-translation) over the course of contrastive training. The method is evaluated on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset, against fine-tuning, UDA, SimCSE, and CERT. CurCon reports the best average accuracy (88.9 vs. 87.8 for CERT), with ablations attributing 0.8 points to the curriculum ordering, and shows larger gains at 100 labels than at 1,000.

---

## Soundness — 55

**Strengths**
- The experimental skeleton is appropriate: an intermediate-training baseline (CERT), a consistency-regularisation baseline (UDA), a sentence-embedding baseline (SimCSE), and direct fine-tuning; five seeds with standard deviations; stratified label sampling.
- The ablation set is well-chosen. In particular, the *reversed curriculum* (87.6) falling below both the full method (88.9) and the fixed mixture (88.1) is the single most informative result in the paper, because it isolates *ordering* from *operator set*. The "no contrastive stage" row correctly reproduces the fine-tuning number (85.1), which is a consistency check in the paper's favour.

**Major concerns**
1. **Asymmetric hyperparameter tuning invalidates the headline comparison.** CurCon receives a 48-configuration grid search *per dataset* on the validation set, while "baselines are trained with the hyperparameters reported in their original papers." Those papers were not written for a 500-label regime, and low-resource fine-tuning is notoriously sensitive to learning rate, warmup, and epoch count. A 1.1-point average gap is entirely within the range that per-dataset tuning alone can produce. At minimum, CERT (which shares the pipeline) must be tuned with the same budget; ideally all baselines should be.
2. **No statistical testing, and several gains lie inside the reported noise.** On TREC, 90.8 ± 0.9 vs. 90.8/90.2 ± 0.7 is not distinguishable with five seeds; AG News (+1.1 with σ ≈ 0.6–0.8) is marginal. The claim "CurCon obtains the highest accuracy on all four datasets" should be qualified, and paired seed-level tests (or seed-matched comparisons) reported.
3. **Method description does not match the abstract.** The abstract states augmentation strength "increases … linearly," but the implementation is a four-stage step schedule gated at c(t) > 0.25/0.5/0.75 with uniform sampling among available operators. Also, "strength" is confounded with "operator diversity": by construction the late phase both adds harder operators *and* increases the number of candidate operators, so the effect of difficulty per se is not cleanly isolated. Additionally, c(t) = min(1, t/L) is undefined at L = 0; the reduction to a fixed mixture is stipulated rather than derived.
4. **Missing information needed to interpret or reproduce the result.** The selected curriculum lengths L are never reported — surprising, given that L is the paper's only new hyperparameter and the central claim concerns it. Unlabelled pool sizes are also absent; 20,000 steps × batch 128 implies ~2.6M views, which for TREC (a few thousand sentences) means hundreds of passes over the unlabelled set, whereas for AG News it is a small fraction of one pass. This heterogeneity is likely to interact strongly with a step-indexed curriculum and is not discussed.
5. **The effective label budget is larger than advertised.** Each dataset also uses a 200-example labelled validation set, and 48 configurations are selected on it. This is 40% additional supervision beyond the nominal 500, and grid selection on 200 examples carries real risk of validation overfitting. The paper should report whether baselines received the same validation access and should consider a fixed-budget or cross-validated selection protocol.
6. **Internal inconsistency in the cost analysis.** "Because back-translated views are pre-computed, contrastive training with CurCon takes approximately 12% longer than with CERT, due to on-the-fly span deletion and synonym replacement." The causal connective is wrong, and 12% is a large overhead to attribute to two cheap CPU string operations; a breakdown (or a note about dataloader bottlenecking) is needed.
7. **Table 3 is under-reported**: no standard deviations, no other baselines, and the 100-label setting is precisely where variance is highest, so the key "gains grow as labels shrink" claim rests on the least stable numbers in the paper.

---

## Novelty — 40

The contribution is a scheduling wrapper around an existing pipeline. The paper is candid that curriculum-over-augmentation-magnitude has been explored in vision, and the text-side novelty amounts to (i) applying that idea to a contrastive *intermediate* stage and (ii) instantiating it with a hand-picked ordering of four standard NLP augmentations. The schedule is a three-threshold step function with one hyperparameter; there is no new objective, no theoretical claim about why this ordering should help, and no attempt to define augmentation difficulty in a measurable way (e.g., via view similarity, alignment/uniformity, or loss curvature) rather than by assertion. The reversed-curriculum ablation is a nice empirical touch but does not raise the conceptual contribution much above "tune the augmentation schedule."

---

## Significance — 45

The method is simple, architecture-agnostic, and free at inference, which is genuinely attractive for practitioners. However, the potential impact is bounded by three factors. First, the effect size is ~1 point on average with an unequal tuning protocol, so the practical payoff may be near zero once baselines are tuned equally. Second, the evaluation suite (SST-2, AG News, TREC, SUBJ) consists of short-text, near-saturated tasks; the setting is dated relative to current low-resource work, and there is no harder or domain-shifted task where in-domain adaptation would matter most. Third, and most importantly, the paper's own related-work section identifies prompt-based fine-tuning as a central low-resource approach, yet no prompt-based baseline (e.g., LM-BFF/PET-style) is included, and results are confined to BERT-base. Without that comparison it is hard to know whether the studied axis is the one that matters in this regime. The gain-shrinks-with-labels trend is plausible and useful, but also the least well-supported result.

---

## Clarity — 78

The writing is clean, economical, and easy to follow; the pipeline, operators, and schedule are described precisely enough to reimplement the core idea, and the tables are legible with bolding and standard deviations where appropriate. The Limitations section is honest about language, text length, encoder scale, and the hand-designed sch