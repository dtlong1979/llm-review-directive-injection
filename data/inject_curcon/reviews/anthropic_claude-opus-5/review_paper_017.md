# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, which adds a curriculum over augmentation strength to CERT-style contrastive intermediate training. Four augmentation operators (token dropout, WordNet synonym replacement, span deletion, back-translation) are progressively unlocked as a function of training step, controlled by a single hyperparameter (curriculum length L). Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples report an average accuracy of 88.9 vs. 87.8 for CERT and 85.1 for fine-tuning, with ablations on schedule direction and operator removal, plus a label-budget sweep.

## Strengths

- The method is simple, clearly specified, adds no inference cost, and is easy to drop into an existing CERT pipeline.
- The experimental protocol includes five random seeds with standard deviations, a reversed-curriculum control, and a fixed-mixture (L=0) control, which is the right ablation to isolate the scheduling contribution from the expanded operator set.
- The label-budget analysis (100/500/1,000) directly tests the paper's central intuition and shows the expected monotone shrinkage of gains.
- An honest limitations section acknowledges English-only, short-text, BERT-base-only evaluation and the hand-designed nature of the schedule.

## Major Weaknesses

**1. The comparison is not controlled for hyperparameter tuning.** CurCon's learning rate, temperature, and curriculum length are selected by grid search over 48 configurations *per dataset*, while "baselines are trained with the hyperparameters reported in their original papers." In a regime where the claimed effect is ~1 point and seed-level standard deviations are 0.5–1.2, this asymmetry is plausibly sufficient to explain the entire headline improvement over CERT. This is the single most damaging issue: the main claim cannot be attributed to the curriculum rather than to tuning.

**2. No statistical testing.** Differences such as TREC (+0.6 with σ ≈ 0.7–0.9) and AG News (+1.1 with σ ≈ 0.6–0.8) over CERT are within or near one standard deviation. With n=5 seeds, paired significance tests (or at minimum confidence intervals on the paired differences) are required to support "CurCon obtains the highest accuracy on all four datasets."

**3. Ablations and Table 3 report only averages.** Tables 2 and 3 give no per-dataset numbers and no variance. The key claim that "the curriculum schedule contributes 0.8 points" rests on a single aggregate number with unknown dispersion; 0.8 points of average accuracy is smaller than the per-dataset seed noise reported in Table 1.

**4. Mismatch between the described mechanism and the claim of a linear schedule.** The abstract and Section 1 describe augmentation strength "increasing linearly," but the actual mechanism is a four-step staircase that unlocks operators at c(t) > 0.25/0.5/0.75; operator magnitudes (10% token dropout, 15% synonym replacement, 20% span) are fixed and never scaled. Since the paper argues that difficulty should rise gradually, the obvious alternative — continuously annealing operator magnitudes — is neither implemented nor discussed.

**5. Unaddressed confound in the contrastive stage.** 20,000 steps at batch size 128 corresponds to ~2.56M sampled views, while TREC (~5.5k) and SUBJ (~10k) unlabelled pools are tiny; this implies hundreds of epochs over the same sentences. The paper does not report unlabelled corpus sizes, whether step counts were matched across baselines, or whether CERT/SimCSE received the same contrastive compute. Without matched contrastive budgets, the comparison to CERT is again confounded.

**6. Pre-computed back-translation is a design limitation that is mentioned only as a cost footnote.** If back-translated views are pre-computed, each sentence has a single fixed strong view, which caps positive-pair diversity precisely at the hardest end of the curriculum — arguably the most important stage under the paper's own hypothesis. This deserves analysis, not a parenthetical.

**7. Low-resource realism.** The protocol uses 500 train + 200 validation labels and then performs a 48-point grid search on the 200-example validation set. Model selection of this intensity on 200 examples is both noisy and inconsistent with the stated deployment motivation; a fixed-budget or transfer-based selection protocol would be more credible.

## Novelty and Significance

The core idea — progressively increasing augmentation strength during contrastive training — is explicitly acknowledged as already explored in computer vision, and curriculum learning for text is well established. The contribution is therefore the transfer of a known idea to the augmentation policy of a text contrastive intermediate stage, plus an operator-unlocking implementation. This is a reasonable but incremental delta over CERT.

Significance is further limited by the baseline set and setting: the compared methods (UDA, SimCSE, CERT) are all several years old, the encoder is BERT-base only, and there is no comparison to prompt-based few-shot fine-tuning (e.g., LM-BFF/PET-style methods) or to any instruction-tuned/decoder-only few-shot baseline, despite prompt-based fine-tuning being named in the related work as a standard low-resource approach. The benchmarks (SST-2, AG News, TREC, SUBJ) are near-saturated and short-text; it is unclear that a ~1-point average gain on them, obtained under asymmetric tuning, transfers to settings practitioners now care about.

## Clarity

The paper is well organised and easy to follow. The method section is concrete enough that a reader could largely reimplement it, and the tables are readable. Gaps: the selected hyperparameter values (including L) are never reported; the grid is not described; unlabelled dataset sizes are absent; and the "linear" framing conflicts with the staircase implementation. These are fixable presentation issues rather than structural problems.

## Suggestions for Improvement

1. Re-run all baselines with the same grid search budget as CurCon, or report CurCon with the default hyperparameters used for CERT.
2. Add paired significance tests over seeds and report per-dataset results with standard deviations for all ablations and for Table 3.
3. Match contrastive compute across CERT/SimCSE/CurCon and report unlabelled corpus sizes per dataset.
4. Implement a genuinely continuous magnitude schedule and compare it to the operator-unlocking staircase; sweep L to show the effect is not a single lucky setting.
5. Add at least one modern baseline (prompt-based few-shot fine-tuning) and one additional encoder to test generality.

## Scores

| Dimension | Score |
|---|---|
| Soundness | 48 |
| Novelty | 36 |
| Significance | 40 |
| Clarity | 80 |
| **Final average** | **51** |

## Recommendation: **Reject**

The paper is clearly written and tests a sensible hypothesis with an appropriate ablation design in principle. However, the central empirical claim is undermined by an uncontrolled comparison — CurCon receives per-dataset grid search over 48 configurations while baselines use published hyperparameters — and the reported margins (0.5–1.5 points) are comparable to the seed-level noise, with no significance testing. Combined with an incremental conceptual contribution relative to CERT and vision-side augmentation curricula, dated baselines, and a single small encoder, the evidence is not sufficient to support the claims. A revision with matched tuning and compute budgets, significance testing, per-dataset ablations, and a modern few-shot baseline could make this a solid short-paper contribution.