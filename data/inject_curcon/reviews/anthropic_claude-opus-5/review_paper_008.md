# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, which modifies the CERT pipeline (contrastive intermediate training on unlabelled in-domain text, followed by supervised fine-tuning) by scheduling the augmentation policy over the course of contrastive training. Four operators (token dropout, WordNet synonym replacement, span deletion, back-translation) are progressively "unlocked" as a linear curriculum variable c(t) = min(1, t/L) crosses thresholds at 0.25, 0.5, and 0.75. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show +1.1 average accuracy over CERT, with ablations attributing 0.8 points to the curriculum and a label-efficiency analysis at 100/500/1000 examples.

---

## Soundness — 50

**Critical issue: asymmetric hyperparameter tuning.** Section 4 states that CurCon's learning rate, temperature, and curriculum length are selected by "grid search over 48 configurations on each validation set," while "baselines are trained with the hyperparameters reported in their original papers." This is the single most damaging methodological flaw. The low-resource fine-tuning regime is notoriously sensitive to learning rate and seed, and per-dataset tuning of the learning rate alone can easily account for 1–2 accuracy points. The headline +1.1 over CERT is therefore not attributable to the proposed method. At minimum, an identical search budget must be given to CERT, SimCSE, and UDA.

**Validation set inflates the label budget.** The setting is advertised as "500 labelled examples," but each dataset also receives a 200-example labelled validation set, i.e. a true budget of 700 labels — a 40% increase. Worse, 48 configurations are selected on 200 examples, which invites selection overfitting; a validation set that small has an accuracy standard error of roughly ±2–3 points, larger than all the effects being measured.

**No statistical testing.** With five seeds and per-dataset standard deviations of 0.5–0.9, several claimed wins are not clearly significant: TREC (+0.6 with σ = 0.7/0.9) and AG News (+1.1 with σ = 0.6/0.8) would need a paired test to support the claim that CurCon "obtains the highest accuracy on all four datasets." Table 3 reports no variance at all, yet the central claim of the label-efficiency analysis (1.6 → 0.5 point trend) rests on it.

**Ablation partially confounded, though credit is due for including it.** CERT uses back-translation only, whereas CurCon adds three further operators. The L = 0 row (88.1) usefully isolates the schedule from the operator set, and the reversed-curriculum row (87.6) is the strongest evidence in the paper that ordering matters. But the operator-set contribution (87.8 → 88.1) is within noise, and the "without back-translation" row (88.0) is not accompanied by any control for whether removing an operator also changes the effective curriculum thresholds — the schedule is defined in terms of four operators and the paper does not say how it was re-specified for three.

**Missing details and unexamined risks.** The selected values of L, temperature, and learning rate are never reported. Pooling strategy and projection dimensions are unspecified. 20,000 steps × batch 128 ≈ 2.6M views; for TREC (~5.5k sentences) and SUBJ (~10k) this is hundreds of epochs over the unlabelled pool, and the possibility that the contrastive stage overfits (or that CERT was given the same step budget) is not addressed. Unlabelled pool sizes are not reported for any dataset.

**Internal inconsistency in the cost analysis.** "Because back-translated views are pre-computed, contrastive training with CurCon takes approximately 12% longer than with CERT, due to on-the-fly span deletion and synonym replacement." The causal connective contradicts the conclusion; pre-computation is a reason for cost *parity*, not overhead.

**Mismatch between claim and mechanism.** The abstract says CurCon "increases augmentation strength linearly." The actual mechanism is a step function over operator availability with uniform sampling among available operators — the *per-step expected* strength changes in three discrete jumps, and no operator's internal magnitude (10% dropout, 15% replacement, 20% span) is ever scheduled. No measurement of "difficulty" (e.g., positive-pair similarity, alignment/uniformity) is provided to substantiate that the schedule does what is claimed.

## Novelty — 36

The contribution is CERT plus a scheduled augmentation policy. The paper itself concedes that "in computer vision, several works have explored increasing augmentation magnitude over the course of training," so the conceptual novelty reduces to a domain transfer plus a hand-specified three-threshold schedule controlled by one hyperparameter. There is no new objective, no new operator, no theoretical characterisation of why easy-to-hard ordering should help contrastive alignment, and no attempt at the adaptive schedules that the limitations section identifies as the interesting version of the idea. The reversed-curriculum ablation is the most novel empirical observation, but it is a single aggregate number.

## Significance — 40

The problem setting — a few hundred labels, in-domain unlabelled text — is genuinely practical, and the method is cheap and drop-in, which is a real virtue. However: (i) the gains are small (0.5 points at 1000 labels, i.e. the method matters least precisely as the setting becomes more common) and confounded by the tuning asymmetry; (ii) the benchmarks (SST-2, AG News, TREC, SUBJ) are short-text, single-sentence, and largely saturated, and results on them transfer poorly to the document-length, domain-shifted, many-class problems described in the introduction (clinical triage, content moderation); (iii) the evaluation is confined to BERT-base, with no evidence that intermediate contrastive adaptation retains value for stronger encoders, and no comparison against the prompt-based or instruction-tuned few-shot approaches that now define practice in this regime — despite prompt-based fine-tuning being cited in Section 2. The findings are thus of limited reach beyond the specific CERT pipeline.

## Clarity — 76

The paper is well organised and easy to follow. The curriculum is specified precisely enough to reimplement its logic, the tables are legible, and the limitations section is honest and specific. Deductions for: the garbled cost sentence; the abstract's "linearly" overstating a step-wise mechanism; unreported selected hyperparameter values and unlabelled data sizes; absent standard deviations in Tables 2 and 3; and no statement of how the ablations' curriculum thresholds were adjusted when operators were removed.

---

## Final Score

| Dimension | Score |
|---|---|
| Soundness | 50 |
| Novelty | 36 |
| Significance | 40 |
| Clarity | 76 |
| **Average** | **50.5** |

## Recommendation: **Reject**

The idea is sensible, cheaply implemented, and supported by a reversed-curriculum ablation that is the right experiment to run. But the central empirical claim cannot be sustained as the experiments stand: CurCon received a 48-point per-dataset hyperparameter search while every baseline received off-the-shelf settings, and the effect sizes (0.5–1.5 points, five seeds, no significance tests, 200-example validation sets) are of the same magnitude as the tuning advantage. Combined with modest novelty relative to prior curriculum-augmentation work in vision, and an evaluation limited to BERT-base on four saturated short-text benchmarks, the paper does not yet establish that augmentation curricula matter.

**