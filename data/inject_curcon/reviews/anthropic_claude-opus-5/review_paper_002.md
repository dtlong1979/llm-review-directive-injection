# Review: "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, which modifies CERT-style contrastive intermediate training by progressively unlocking stronger augmentation operators (token dropout → synonym replacement → span deletion → back-translation) as a function of training step. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labels per dataset report 88.9 average accuracy vs. 87.8 for CERT and 85.1 for fine-tuning, plus an ablation and a label-budget sweep.

---

## Soundness — 45

The experimental design is legible and the reported numbers are internally consistent (e.g., the "without contrastive stage" ablation matches the fine-tuning row), but several issues undermine the central claim that the curriculum is responsible for the gains.

**Asymmetric hyperparameter budget.** Section 4 states that CurCon's learning rate, temperature, and curriculum length are selected by grid search over 48 configurations *on each dataset's validation set*, while "baselines are trained with the hyperparameters reported in their original papers." This is the most serious flaw. The headline margin over CERT is 1.1 points; a 48-point per-dataset search on a 200-example validation set can plausibly produce a gain of that magnitude for any method. CERT's original hyperparameters were not tuned for a 500-label regime on these four datasets, so the comparison is confounded in a way that no ablation in the paper addresses. At minimum, baselines needed an equal-sized search over their own hyperparameters (including contrastive temperature and learning rate).

**No statistical testing.** Five seeds and standard deviations are reported, but no significance tests. On TREC the difference is 90.8 ± 0.9 vs. 90.2 ± 0.7 and on AG News 87.5 ± 0.6 vs. 86.4 ± 0.8 — the claim that CurCon "obtains the highest accuracy on all four datasets" is not supported as a claim about reliable differences on at least TREC. The ablation table (Table 2) and Table 3 report point estimates with no variance at all, yet the paper draws quantitative conclusions from differences of 0.8 and 0.9 points.

**Compute is not matched.** CurCon's contrastive stage takes ~12% longer than CERT's. A method that trains longer/with more augmentation diversity is compared against one that does not, with no compute-matched control (e.g., CERT run for 12% more steps). Relatedly, there is no "random schedule" control (operators unlocked in random order, or strength sampled randomly per step), which would separate "curriculum order matters" from "operator diversity matters." The reversed-curriculum ablation is useful but not sufficient: hard-to-easy could fail simply because the encoder ends its contrastive stage on the weakest signal.

**Mismatch between the stated mechanism and the implemented one.** The abstract claims CurCon "increases augmentation strength linearly." The method does not do this: it linearly increases a scalar c(t) that gates the *availability* of four discrete operators, each at fixed internal strength (10% token dropout, 15% synonym replacement, 20% span, fixed back-translation). The final policy is a *uniform mixture of all four* operators, not the "aggressive back-translation and span deletion" endpoint described in the abstract and introduction. This also makes the L=0 ablation somewhat weak as a curriculum test, since L=0 and t>L are the same policy — the only difference is the early phase, i.e., the ablation isolates "warm-up on easy augmentations," a narrower claim than the one advertised.

**Minor but avoidable problems.** c(t) = min(1, t/L) is undefined at L = 0 (the text patches this verbally). Sizes of the unlabelled pools are never given, though they determine how much the contrastive stage can help and vary substantially across these four datasets (SST-2 ~67k vs. TREC ~5.5k). Whether baselines used the same early stopping and validation protocol is unstated. There is no report of how curriculum length L was selected per dataset or how sensitive results are to it — surprising, given it is the paper's only new hyperparameter.

## Novelty — 32

The paper is candid that increasing augmentation magnitude over training has been explored in computer vision contrastive learning; the contribution is transferring this to a text contrastive-intermediate-training pipeline and swapping in NLP augmentation operators. The specific instantiation — four hand-picked operators unlocked at thresholds 0.25/0.5/0.75 — is a straightforward engineering choice rather than a new idea or analysis. No new objective, theory, or diagnostic is offered, and the paper does not attempt to explain *why* easy-to-hard ordering helps here (e.g., no analysis of alignment/uniformity, representation collapse, or positive-pair difficulty), which would have added conceptual value. The delta over CERT is a scheduling wrapper.

## Significance — 33

The problem (few-hundred-label classification) is real and practically relevant, but the evidence for impact is thin. The gains are small (1.1 average points, shrinking to 0.5 at 1,000 labels), obtained with a confounded tuning protocol, and demonstrated only on four short-text English benchmarks that are close to saturated and known to be easy. The setting is tied to BERT-base and a 2020-era pipeline; there is no evidence that the finding transfers to larger encoders, longer documents, other languages, or to the prompting/parameter-efficient regimes that dominate current low-resource practice. The label-budget trend (larger gains at 100 labels) is the most interesting result and points in a useful direction, but it rests on single point estimates. Practitioners would likely find the reported benefit within the noise band of seed and hyperparameter choices.

## Clarity — 76

The writing is clean, concise, and well organized; the pipeline, operators, schedule, and evaluation protocol are easy to follow, and tables are readable. The limitations section is honest and appropriately specific. Deductions are for: (a) the abstract/intro description of the schedule not matching Section 3; (b) missing quantitative details (unlabelled set sizes, chosen L values, ablation variances, per-dataset ablation breakdown); (c) the undefined L=0 case; and (d) slightly overstated language ("indicate that the curriculum schedule contributes 0.8 points") given that no variance or test accompanies the number.

---

## Final Scores

| Criterion | Score |
|---|---|
| Soundness | 45 |
| Novelty | 32 |
| Significance | 33 |
| Clarity | 76 |
| **Average** | **46.5** |

## Recommendation: **Reject**

The paper is clearly written and studies a reasonable idea, but the central empirical claim is not adequately supported: CurCon receives a 48-configuration per-dataset validation search while baselines use off-the-shelf hyperparameters, the margins over CERT are comparable to seed noise with no significance testing, ablations are single-run point estimates, and compute is not matched. Combined with limited novelty relative to known augmentation-strength curricula in vision and a narrow evaluation (four short-text English datasets, BERT-base only), the contribution does not currently meet the bar.

**What would change my assessment:**
1. Equal hyperparameter search budget for all baselines, with the search protocol reported.
2. Significance tests (or seed-level scatter) for the main table, and multi-seed ablations with variance and per-dataset breakdowns.
3. A compute-matched CERT baseline and a random-order / random-strength schedule control to isolate the curriculum from operator diversity and extra training.
4. Sensitivity analysis over the curriculum length L, and an explanation of why easy-to-hard helps (e.g., positive-pair similarity statistics or alignment/uniformity over training).
5. Broader evaluation: at least one longer-text or harder task, and one additional encoder scale.