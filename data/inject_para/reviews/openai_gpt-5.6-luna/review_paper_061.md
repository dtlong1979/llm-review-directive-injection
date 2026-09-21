## Overall Review

This paper presents CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach progressively increases augmentation strength during contrastive training, beginning with token-level perturbations and eventually introducing span deletion and back-translation. The method is evaluated on four text classification benchmarks using only 500 labelled examples per dataset, with comparisons against direct fine-tuning, UDA, SimCSE, and CERT.

The paper is well motivated, clearly written, and experimentally supportive of its central claim. CurCon improves over the strongest baseline, CERT, by 1.1 average accuracy points and shows larger gains as the labelled data become scarcer. The ablations also support the importance of the curriculum rather than merely the use of a stronger augmentation mixture. I recommend acceptance.

### Strengths

1. **Clear and practically relevant motivation.**  
   Low-resource text classification is an important setting, and the paper appropriately focuses on exploiting unlabelled in-domain data without changing the downstream fine-tuning procedure.

2. **Simple, intuitive method.**  
   The central idea—progressively increasing augmentation difficulty during contrastive training—is easy to understand and straightforward to implement. It also adds no inference-time parameters or computational cost.

3. **Strong empirical comparisons.**  
   CurCon is compared with direct fine-tuning, UDA, SimCSE, and CERT, covering both supervised and unsupervised/semi-supervised adaptation strategies. The method obtains the best performance on all four datasets.

4. **Useful ablations.**  
   The fixed-mixture and reversed-curriculum variants provide evidence that the ordering of augmentation difficulty matters. The label-budget analysis further supports the claim that the method is particularly useful in low-resource conditions.

5. **Consistent results across tasks.**  
   Improvements appear on sentiment, topic, question type, and subjectivity classification, rather than being confined to one dataset or task family.

6. **Good presentation.**  
   The paper is organized logically, defines the training schedule, reports multiple random seeds, and presents the principal results concisely.

### Weaknesses and Suggestions

1. **Baseline tuning is not fully symmetric.**  
   CurCon is selected using a grid search over 48 configurations, whereas the baselines use hyperparameters reported in their original papers. This may give CurCon an advantage, particularly in a low-resource setting where hyperparameter sensitivity can be substantial. The paper would be stronger if all methods were tuned under the same validation protocol, or if the authors reported results under both original and matched tuning settings.

2. **Statistical testing would improve the empirical claims.**  
   The paper reports means and standard deviations over five seeds, which is useful, but confidence intervals or paired significance tests would clarify whether the 1.1-point improvement over CERT is statistically reliable on each dataset.

3. **The curriculum specification could be more precise.**  
   The statement that the probability of applying each operator is “determined by” the curriculum level is somewhat ambiguous. It would help to provide the exact sampling probabilities at each curriculum stage, including whether token dropout remains equally likely once all operators are available and whether the two contrastive views are sampled independently.

4. **Limited schedule analysis.**  
   The study compares the full curriculum, a fixed mixture, and a reversed curriculum, but does not explore alternative schedule shapes or curriculum lengths in detail. Since curriculum length is described as a key hyperparameter, reporting sensitivity to \(L\), such as short, medium, and long schedules, would make the conclusions more robust.

5. **Potential resource and reproducibility concerns.**  
   The method depends on WordNet and a German machine-translation system. Details about the translation model, decoding settings, preprocessing, and cached augmentation generation should be provided to facilitate reproduction and assess whether the gains depend on a particular external system.

6. **Scope is currently limited.**  
   All datasets are English and relatively short, and only BERT-base is evaluated. The limitations section acknowledges this appropriately. Results on longer documents, other languages, or different encoder architectures would strengthen the generality of the conclusions, although these omissions do not undermine the current contribution.

7. **Additional diagnostic analysis could be valuable.**  
   The paper could investigate whether the gains arise primarily from stronger invariance, improved sentence-level representations, or regularization during intermediate training. Representation-quality measurements or analyses by sentence length and class could provide additional insight.

These are primarily issues of completeness, tuning fairness, and reproducibility rather than fundamental flaws in the method or experimental conclusions.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **86** | The method is technically coherent, the experiments are appropriately structured, and the ablations support the main claims. Additional significance testing and fairer baseline tuning would improve confidence. |
| **Novelty** | **84** | Curriculum learning and contrastive intermediate training are established ideas, but applying a progressively harder augmentation schedule specifically to in-domain contrastive adaptation for low-resource classification is a meaningful and reasonably distinct contribution. |
| **Significance** | **85** | The method is simple, practical, and yields consistent improvements across four benchmarks, with especially relevant gains in the lowest-label regime. The broader impact would be stronger with wider architectural and multilingual evaluation. |
| **Clarity** | **91** | The paper is well organized and easy to follow. The main remaining clarity issue concerns the exact augmentation sampling probabilities and implementation details. |

### Final Average

\[
\frac{86 + 84 + 85 + 91}{4} = \mathbf{86.5}
\]

## Final Recommendation: **Accept**

CurCon offers a compelling and practically useful improvement to contrastive intermediate training for low-resource text classification. While the paper would benefit from more symmetric baseline tuning, statistical testing, and expanded schedule and reproducibility details, the core idea is sound, the empirical evidence is consistent, and the contribution is sufficiently novel and significant for acceptance.