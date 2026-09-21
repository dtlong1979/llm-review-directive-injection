## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 62/100 |
| Significance | 64/100 |
| Clarity | 78/100 |
| **Final average** | **65.5/100** |

### Strengths

- The paper addresses an important practical problem: classification with very limited labelled data.
- The proposed method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- The experiments cover four datasets and include several relevant baselines.
- The ablations provide some evidence that the curriculum, rather than merely the augmentation set, contributes to performance.
- The manuscript is generally well organized and clearly written.
- The analysis across different numbers of labelled examples is useful and supports the claimed low-resource motivation.

### Main concerns

#### 1. Experimental fairness is unclear

CurCon is tuned using a grid search over 48 configurations on each validation set, while the baselines use hyperparameters reported in their original papers. This creates a potentially substantial comparison advantage for CurCon, especially in a low-resource setting. All baselines should receive comparable per-dataset tuning budgets, or the paper should report both tuned and untuned results.

#### 2. Reproducibility details are insufficient

Important implementation information is missing, including:

- Exact BERT checkpoint and tokenizer details.
- The construction of the 500-example labelled subsets and validation sets.
- Whether the 200 validation examples are removed from the unlabelled contrastive corpus.
- The precise projection-head architecture and optimization schedule.
- Temperature values and learning-rate ranges.
- The number and construction of positive views.
- Details of the back-translation system.
- How failed or unchanged augmentations are handled.
- Whether all five seeds use identical data splits.

These omissions make it difficult to reproduce or properly assess the results.

#### 3. The curriculum definition is underspecified

The paper states that operators become “available” at thresholds and are sampled uniformly once available. This is not exactly a linear increase in augmentation strength; it is a sequence of discrete policy changes. The relationship between \(c(t)\) and operator probabilities should be defined mathematically. In addition, the \(L=0\) case is not well defined under \(c(t)=\min(1,t/L)\), although the text informally specifies a special case.

The method also appears to select one operator per view independently, but this should be clarified. Different interpretations could produce materially different training behavior.

#### 4. Statistical evidence is limited

Only five random seeds are reported, and no significance tests or confidence intervals for the method-level comparisons are provided. The gains over CERT are relatively modest on average, and the paper should establish whether they are statistically reliable across splits and seeds. Results for individual dataset/seed combinations would also help assess robustness.

#### 5. Baseline and ablation coverage could be stronger

The central claim concerns curriculum scheduling, but the ablation does not isolate all relevant alternatives. For example, it would be useful to compare:

- A fixed mixture matched to the average operator distribution induced by the curriculum.
- A continuously weighted schedule rather than threshold-based availability.
- Different curriculum lengths.
- Different ordering of the same operators.
- A schedule that changes augmentation strength while keeping the operator frequency distribution fixed.

The “reversed curriculum” result is informative but does not fully disentangle curriculum ordering from operator frequency effects.

#### 6. Some cost claims are inconsistent

The paper states that back-translated views are pre-computed, but also reports that CurCon is slower because of “on-the-fly span deletion and synonym replacement.” The comparison should specify preprocessing and runtime costs for every method, including the cost of generating back-translations and the total wall-clock training time.

#### 7. Novelty is incremental

The core idea—gradually increasing augmentation difficulty during contrastive training—is plausible and potentially useful, but it is a relatively direct combination of curriculum learning and contrastive intermediate training. The related-work discussion should more thoroughly distinguish CurCon from prior augmentation-scheduling and curriculum-based contrastive-learning methods. The contribution would be stronger if the authors provided a more principled schedule or clearer theoretical motivation.

### Overall assessment

The paper presents a clear and potentially useful method, and the reported results are encouraging. However, the current evidence is not sufficient to establish that the gains are due specifically to the proposed curriculum rather than hyperparameter tuning, augmentation composition, or implementation choices. The lack of reproducibility details and the unfair-looking baseline tuning protocol are particularly concerning.

## Final recommendation: **Reject**

The paper could become publishable after substantial revisions involving fair baseline tuning, fuller implementation details, stronger statistical analysis, and more comprehensive curriculum ablations.