# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, which modifies the CERT pipeline (contrastive intermediate training on unlabelled in-domain text, followed by supervised fine-tuning) by scheduling augmentation strength over the contrastive stage. Four operators (token dropout, WordNet synonym replacement, span deletion, back-translation) are progressively unlocked as a linear curriculum variable c(t) = min(1, t/L) crosses thresholds at 0.25/0.5/0.75. On SST-2, AG News, TREC and SUBJ with 500 labels, CurCon reports 88.9 average accuracy vs. 87.8 for CERT and 85.1 for fine-tuning, with ablations on curriculum order and a label-efficiency analysis.

---

## Detailed Assessment

### Soundness — 50/100

The experimental protocol contains one confound that is serious enough to undermine the paper's central claim, plus several secondary issues.

**Asymmetric hyperparameter tuning (critical).** Section 4 states that CurCon's learning rate, temperature and curriculum length were selected by grid search over 48 configurations *per dataset validation set*, while "baselines are trained with the hyperparameters reported in their original papers." The reported margin over CERT is 1.1 points on average. In the 500-label regime, learning rate alone routinely moves BERT-base fine-tuning accuracy by more than that, and CERT's published hyperparameters were tuned for full-resource GLUE tasks, not for 500-example subsets of SST-2/TREC/SUBJ. As the experiments stand, one cannot distinguish "curriculum helps" from "CurCon received 48× more tuning budget than the baselines." A matched-budget comparison (identical grid for CERT and SimCSE) is a prerequisite for the main table to support the claim.

**The ablation does not isolate the curriculum.** The L = 0 condition is described as "a fixed mixture of all four operators," presumably uniform. But the curriculum simultaneously changes (i) which operators are available, (ii) the *marginal frequency* of each operator over training (back-translation is applied in only ~25% of steps under the curriculum vs. ~25% under uniform mixture — actually similar, but token dropout is heavily over-weighted early), and (iii) the ordering. A fixed non-uniform mixture matched to the curriculum's time-averaged operator marginals is the correct control; without it, the 0.8-point effect could be an operator-weighting effect rather than an ordering effect. The reversed-curriculum result (−1.3) is more informative and is the strongest evidence for ordering, but it is reported as a single average number with no per-dataset breakdown and no seed variance.

**Statistical support.** Standard deviations are given for Table 1 but no significance tests. With five seeds, the per-dataset gains on TREC (+0.6, σ ≈ 0.7–0.9) and AG News (+1.1, σ ≈ 0.6–0.8) are at best marginal; only SST-2 looks clearly separated. Tables 2 and 3 report no variance at all, so the 0.8 vs. 0.9 vs. 1.3 ablation differences cannot be ordered with any confidence. The claim that "the curriculum schedule contributes 0.8 points" is stated in the abstract with more precision than the evidence supports.

**Validation data accounting.** Each dataset is given a 200-example labelled validation set *in addition* to the 500 training labels, and early stopping plus a 48-point grid search are run on it. That is a 40% increase in labelled data over the nominal budget, and it is used far more intensively by CurCon than by the baselines. In a paper whose premise is label scarcity, the validation budget should be counted and, ideally, reduced or cross-validated. This matters even more in the 100-label setting of Table 3, where the validation set is twice the size of the training set.

**Unreported scale of the unlabelled corpus.** Contrastive training runs for 20,000 steps at batch 128 ≈ 2.6M sampled views. TREC has ~5.5k and SUBJ ~10k training sentences, so the contrastive stage makes hundreds of passes over a very small corpus, whereas AG News provides ~120k sentences. The interaction between corpus size, step count and curriculum length L is likely to be substantial and is not analysed; the selected values of L and temperature are never reported, so the results are not reproducible.

**Minor.** The cost paragraph claims back-translated views are pre-computed, yet the curriculum's back-translation probability is time-varying — pre-computation is fine, but then the 12% overhead attributed to "on-the-fly span deletion and synonym replacement" is surprisingly large for two cheap string operations and deserves a breakdown. Baseline augmentation policies (UDA's, CERT's) are not specified, so it is unclear whether CurCon's advantage partly reflects a richer operator set rather than scheduling.

### Novelty — 38/100

The contribution is a single scalar schedule applied to an existing pipeline. The paper is commendably honest that (a) contrastive intermediate training is CERT's, (b) curriculum learning is standard, and (c) progressive augmentation magnitude has been explored in computer vision. The claimed delta is therefore "apply known idea (b)/(c) to known pipeline (a) in the text domain." The threshold-based operator unlocking is hand-designed and arbitrary (0.25/0.5/0.75), and no attempt is made to characterise *why* difficulty ordering should help contrastive learning — e.g., no analysis of alignment/uniformity, positive-pair similarity, or representation collapse over the course of the curriculum. Such an analysis would have converted an engineering tweak into an insight. The related-work section also notes that text curricula have targeted example ordering rather than augmentation policy, which is a fair framing of the gap, but the gap is narrow.

### Significance — 42/100

The method is cheap, adds no inference cost, and the label-efficiency trend in Table 3 (gain shrinking from 1.6 to 0.5 as labels grow from 100 to 1,000) is a sensible and useful negative result: the method's benefit is confined to the smallest-label regime. Against that:

- Effect sizes are small (≈1 point over a baseline that received no tuning), so the practical payoff for a practitioner is uncertain.
- The benchmark suite is four classic, near-saturated, short-text English datasets. No domain-shifted, long-document, many-class, or imbalanced setting is tested — precisely the settings where in-domain contrastive adaptation should matter most.
- Only BERT-base is evaluated. Whether the curriculum survives at RoBERTa-large scale, or matters at all when a modern instruction-tuned model can reach these accuracies zero-shot, is unaddressed. The paper acknowledges this in Limitations but the omission still caps the impact.
- Prompt-based few-shot methods (PET/LM-BFF-style) are mentioned in related work as a relevant family but never compared against, even though they are the standard strong baseline at 100–500 labels. Without that comparison it is hard to place CurCon on the low-resource landscape.

### Clarity — 78/100

The paper is well-organised and easy to read. The method is described precisely enough to understand: the curriculum function, thresholds, sampling rule, and the L = 0 degenerate case are all stated explicitly, and the Limitations section is candid and specific. Tables are clean and the narrative claims match the table contents (with the caveat about over-precise ablation attribution noted above).

Deductions: the InfoNCE objective, projection-head width and temperature are described in prose without equations or values; the selected hyperparameters (L, temperature, learning rate) are never reported; unlabelled corpus sizes per dataset are missing; Tables 2 and 3 lack per-dataset numbers and variance; and it is not stated whether hyperparameters were re-selected for the 100/1,000-label settings in Table 3.

---

## Scores

| Dimension | Score |
|---|---|
| Soundness | 50 |
| Novelty | 38 |
| Significance | 42 |
| Clarity | 78 |
| **Final average** | **52.0** |

---

## Recommendation: **Reject**

The paper is clearly written, the idea is intuitive