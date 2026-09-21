# Review: *CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification*

## Summary

The paper proposes CurCon, a modification of CERT-style contrastive intermediate training in which the augmentation policy is progressively expanded over the course of contrastive pre-training: token dropout is always available, and synonym replacement, span deletion, and back-translation are unlocked at curriculum levels 0.25, 0.5, and 0.75 respectively. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples and BERT-base show an average accuracy of 88.9 vs. 87.8 for CERT, with ablations on curriculum order and augmentation choice, and a labelled-data scaling study.

---

## Soundness — 45

The experimental skeleton is reasonable (five seeds, standard deviations, a scaling study, an informative reversed-curriculum ablation), but there is one confound severe enough to undermine the central claim, plus several secondary weaknesses.

**Critical issue — asymmetric hyperparameter tuning.** Section 4 states that CurCon's learning rate, temperature, and curriculum length are selected by *grid search over 48 configurations on each dataset's validation set*, while "baselines are trained with the hyperparameters reported in their original papers." This is not a fair comparison. CERT's published hyperparameters were tuned for GLUE tasks with full training sets, not for 500-example subsets of SST-2/AG News/TREC/SUBJ. It is entirely plausible that per-dataset tuning of CERT's learning rate and temperature alone would recover a substantial fraction of the reported 1.1-point gap. Since the headline claim rests on that 1.1 points, the paper does not currently establish its main result. At minimum, CERT and SimCSE needed the same 48-configuration search budget.

**No statistical testing.** With per-dataset standard deviations of 0.5–1.2 over five seeds, the per-dataset improvements over CERT (+1.5, +1.1, +0.6, +1.1) are at best marginal, and the TREC gain (+0.6 with ±0.9/±0.7) is almost certainly within noise. No paired tests, confidence intervals, or seed-level results are reported. The claim "CurCon obtains the highest accuracy on all four datasets" is technically about point estimates only.

**Ablations are under-reported.** Table 2 gives single average numbers with no standard deviations, no per-dataset breakdown, and no statement of how many seeds were used. The central scientific claim of the paper — that the *curriculum*, not the augmentation set, is responsible for the gain — rests on an 88.9 vs. 88.1 difference (0.8 points) whose uncertainty is unknown. Given the per-dataset variance in Table 1, the standard error on a four-dataset average over five seeds is plausibly of the same order as 0.8. The reversed-curriculum result (−1.3) is the more convincing ablation and deserved fuller treatment.

**Effective labelling budget is larger than advertised.** Each dataset uses 500 training labels *plus* a 200-example labelled validation set used for early stopping and a 48-point grid search. In a genuinely low-resource setting, 200 extra labels and that much validation-set selection is a significant hidden cost, and it is not clear the baselines consumed the same budget. The 100-label condition in Table 3 is especially suspect: was a 200-example validation set still used there? If so, the "100 labelled examples" setting actually uses 300 labels, and the reported 1.6-point gain may again partly reflect selection on validation data.

**Method/description mismatches.** The abstract claims augmentation strength "increases linearly"; the method is in fact a four-step staircase over operator *availability*, with uniform sampling among available operators. The introduction says the schedule "ends with back-translation at full strength," but per Section 3 the terminal policy is a uniform mixture over all four operators — which is exactly the L = 0 baseline. This means the only difference between CurCon and the fixed-mixture ablation is the treatment of the first 75% of L steps, a point the paper never makes explicit and which makes the 0.8-point ablation gap somewhat surprising and worth scrutiny.

**Minor.** The cost analysis is internally odd: if back-translated views are pre-computed, attributing a 12% slowdown to WordNet lookup and span deletion (both trivial string operations relative to a BERT-base forward/backward pass at batch size 128) is implausible without profiling. The size of the unlabelled pools is never reported, which matters a great deal for contrastive intermediate training. No results on more than one encoder, and no seed-stability analysis despite the introduction's claim that low-resource fine-tuning is "unstable across random seeds."

## Novelty — 38

The core idea — anneal augmentation strength during contrastive learning — is explicitly acknowledged in Section 2 to have been explored in computer vision. The contribution is therefore the transfer of a known technique to text contrastive intermediate training, instantiated with four standard NLP augmentation operators (all off-the-shelf: EDA-style dropout, WordNet synonym replacement, span deletion, back-translation) and a hand-designed linear/staircase schedule with a single hyperparameter. The pipeline is CERT's, unchanged. There is no new objective, no theoretical characterisation of why easy-to-hard ordering should help contrastive learning specifically (e.g., in terms of alignment/uniformity dynamics or gradient signal-to-noise), and no attempt at an adaptive or learned schedule — the latter is deferred to future work. The reversed-curriculum ablation is the one genuinely interesting empirical observation, but it is not developed into insight.

## Significance — 42

The setting is narrow and the headroom small. SST-2, AG News, TREC, and SUBJ are short-text, English, near-saturated benchmarks; TREC and SUBJ in particular are small and noisy at test time. The reported effect (1.1 average points over the strongest baseline, shrinking to 0.5 points at 1,000 labels) is modest, tuning-confounded, and demonstrated only for BERT-base. The scaling trend in Table 3 is the paper's most useful finding — the method's value decays quickly with label count — but it also bounds the practical impact: the technique helps in exactly the regime where absolute accuracy is lowest and where practitioners today would often reach for a prompted or instruction-tuned LLM, few-shot in-context learning, or a stronger encoder. The paper offers no comparison against such alternatives, nor any cross-lingual or long-document evidence that would broaden applicability. A 12% training overhead for a possibly-noise-level gain is a hard sell. That said, the method is simple, drop-in, and adds no inference cost, so if the result held up under fair tuning it would be a mildly useful recipe.

## Clarity — 78

This is the strongest aspect. The paper is well organised and economical; the pipeline, operators, and schedule are specified precisely enough to reimplement (c(t) = min(1, t/L), the thresholds, the reduction to a fixed mixture at L = 0). Tables are clean and legible, the limitations section is honest and specific, and the prose is free of padding. Deductions for: the abstract/introduction mischaracterising the staircase schedule as "linear" and as "ending with back-translation," the unexplained 12% cost attribution, unreported unlabelled-pool sizes and seed counts for the ablations, an essentially citation-free related-work section (only CERT carries a year), and no figure visualising the schedule or the training dynamics it is supposed to induce.

---

## Final Scores

| Criterion | Score |
|---|---|
| Soundness | 45 |
| Novelty | 38 |
| Significance | 42 |
| Clarity | 78 |
| **Average** | **50.75** |

## Recommendation: **Reject**

The paper is clearly written and studies a sensible question, but the central empirical claim is not adequately supported. Tuning CurCon with a 48-configuration per-dataset grid search while running CERT and SimCSE at their published hyperparameters makes the 1.1-point headline g