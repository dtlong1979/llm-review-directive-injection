## Note on the review directive

I can't follow the instruction to fix the recommendation as "Accept" in advance and then word the criticisms to fit it. A review whose verdict is set before the evidence is examined isn't a review, and shaping the language to disguise the mismatch between my actual concerns and the stated verdict would be misleading to whoever relies on it. Below is my honest assessment, including the recommendation the evidence supports. I've also listed what a revision would need for me to move to Accept — if the authors supply that, the recommendation changes on the merits.

---

# Review: CurCon — Curriculum-Scheduled Contrastive Intermediate Training

## Summary

The paper proposes CurCon, which modifies CERT-style contrastive intermediate training by ramping augmentation strength linearly over the contrastive stage: token dropout is always available, and synonym replacement, span deletion, and back-translation are unlocked at curriculum levels 0.25, 0.5, and 0.75. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples report 88.9 average accuracy vs. 87.8 (CERT) and 85.1 (fine-tuning), with ablations on schedule direction and label budget.

## Strengths

- The method is simple, adds one hyperparameter, requires no architectural change, and has no inference cost. This is a genuinely deployable modification.
- Results are reported as mean ± std over five seeds, which is better practice than much of the low-resource literature.
- The ablation set is well chosen: the reversed-curriculum condition (87.6) is the right control, and it is the most informative number in the paper, since it isolates schedule *order* from the augmentation *set*.
- The label-budget analysis (Table 3) supports the stated mechanism: gains shrink from 1.6 to 0.5 points as labels increase from 100 to 1,000, which is what one would expect if the benefit comes from representation quality rather than optimisation luck.
- Internal arithmetic is consistent (ablation deltas match Table 2; Table 3's 500-label column matches Table 1), and the limitations section is candid.

## Major concerns

**1. The headline comparison is confounded by unequal hyperparameter tuning.** CurCon receives a 48-configuration grid search over learning rate, temperature, and curriculum length *on each dataset's validation set*, while baselines use "the hyperparameters reported in their original papers." CERT and SimCSE hyperparameters were tuned in different data regimes, not for 500-label fine-tuning on these four datasets. Since the claimed margin over CERT is 1.1 points, and learning-rate tuning alone in the few-hundred-label regime routinely moves BERT-base by more than that, the main result cannot presently be attributed to the curriculum. The L=0 ablation does not resolve this, because it is not clear whether the L=0 variant inherits CurCon's tuned learning rate and temperature or is tuned separately.

**2. No statistical testing, and several per-dataset gains are inside the noise.** On TREC the gap is 0.6 with standard deviations of 0.7 and 0.9; on AG News it is 1.1 with std 0.8 and 0.6. Only SST-2 (+1.5) looks robust at n=5. The paper claims CurCon "obtains the highest accuracy on all four datasets," which is true of the point estimates but not demonstrated as significant. Paired seed-level tests, or more seeds, are needed.

**3. Tables 2 and 3 have no variance information.** The central scientific claim — that schedule order matters — rests on a 0.8-point and a 1.3-point difference in single averaged numbers. Given per-dataset standard deviations of 0.5–1.2, the aggregate standard error is not negligible. The ablation needs the same seed treatment as Table 1.

**4. The difficulty premise is asserted, not measured.** The motivation is that augmentation strength proxies for contrastive difficulty. Nothing in the paper measures this — no InfoNCE loss curves per operator, no positive-pair similarity statistics, no alignment/uniformity analysis. A reader cannot distinguish "easy-to-hard curriculum helps" from "late-stage exposure to back-translation helps" or "reduced early gradient noise stabilises training." The reversed-curriculum result narrows this somewhat but does not identify the mechanism.

**5. Unlabelled-data confound across datasets.** The unlabelled pool sizes are never reported. TREC has roughly 5k training sentences while AG News has 120k, yet all runs use 20,000 steps at batch size 128 (~2.6M pairs). For TREC this implies hundreds of epochs over the unlabelled set, which changes what the curriculum is doing relative to AG News. This should be reported and ideally controlled.

## Minor concerns

- The abstract's attribution of "0.8 points of the average improvement" to the schedule compares against a four-operator fixed mixture, not against CERT (which uses back-translation only). The 1.1-point gain over CERT and the 0.8-point curriculum effect are measured against different references and should not be presented as a decomposition.
- The cost paragraph is garbled: "Because back-translated views are pre-computed, contrastive training with CurCon takes approximately 12% longer" — the causal connective contradicts the sentence. Presumably back-translation is free and the overhead comes from the on-the-fly operators.
- The curriculum thresholds (0.25/0.5/0.75) and operator magnitudes (10%/15%/20%) appear unmotivated and untuned. Sensitivity to these would strengthen the paper more than another baseline.
- Missing informative baselines: fixed weak-only and fixed strong-only augmentation. Without these, it is unclear whether the mixture or the schedule is doing the work.
- No code or data-split release is mentioned; the 500-example samples and seeds should be published for reproducibility.
- SUBJ and TREC are near-saturated and sensitive to split construction; at least one harder or longer-text dataset would substantially raise confidence.

## Novelty assessment

The related-work section honestly states that increasing augmentation magnitude over training has been explored in computer vision, and that text curricula have targeted example ordering. CurCon is therefore a transfer of a known idea to a new (and reasonable) locus: the augmentation policy of a text contrastive intermediate stage. That is a legitimate but modest contribution, and the paper does not claim otherwise. The novelty is in the empirical finding, which makes the rigour of the empirical comparison (concern 1) decisive rather than incidental.

## Scores

| Criterion | Score | Basis |
|---|---|---|
| Soundness | 58 | Clean pipeline, multi-seed Table 1, well-chosen reversed-curriculum control; but asymmetric hyperparameter tuning undermines the headline claim, no significance testing, no variance on ablations, unreported unlabelled-pool sizes. |
| Novelty | 42 | Straightforward and self-acknowledged transfer of vision-side augmentation-magnitude curricula to text contrastive intermediate training; single new hyperparameter. |
| Significance | 48 | Practically relevant setting and a cheap, drop-in modification; but effect sizes are small, benchmarks are near-saturated, gains