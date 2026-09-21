## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during training. The method begins with token dropout and progressively makes synonym replacement, span deletion, and back-translation available. It is evaluated on four English text-classification datasets in a 500-label setting and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

The central idea is intuitive and potentially useful, but the empirical evidence is not yet sufficiently rigorous to establish that the curriculum itself is responsible for the reported gains.

### Strengths

- The paper addresses an important practical problem: text classification with very limited labeled data.
- The proposed method is simple, model-agnostic, and has no inference-time cost.
- The paper includes several relevant baselines and ablations, including a fixed-mixture baseline and a reversed curriculum.
- Results are reported over multiple random seeds rather than a single run.
- The manuscript is generally well organized and easy to follow.
- The analysis of performance at different label budgets is directionally useful.

### Main concerns

1. **Unfair and insufficiently controlled baseline tuning.**  
   CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search for each dataset, while the baselines use hyperparameters from their original papers. This gives CurCon a substantial tuning advantage, particularly in a low-resource setting. All baselines should receive comparable validation-based tuning, or the paper should report results under a common hyperparameter protocol.

2. **The curriculum is not fully specified.**  
   The text states that operators “become available” at thresholds and that one available operator is sampled uniformly, but it does not precisely define how views are generated, whether the two views use independent operators, or how operator probabilities evolve within each interval. Moreover, \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite the claim that this setting corresponds to a fixed mixture. These details are important for reproducibility and for interpreting the ablation.

3. **The contribution appears relatively incremental.**  
   Gradually increasing augmentation difficulty is a natural curriculum-learning strategy, and the paper does not provide a substantial theoretical justification or a more adaptive scheduling mechanism. The novelty is therefore primarily the application and evaluation of a simple augmentation curriculum to contrastive intermediate training.

4. **Limited statistical analysis.**  
   The paper reports means and standard deviations over five seeds, but does not provide confidence intervals, paired significance tests, or per-seed results. Given that several improvements are approximately one percentage point, it is unclear whether the gains are statistically reliable across datasets.

5. **Insufficient experimental breadth.**  
   The evaluation uses only four relatively short English classification datasets and one encoder family. This makes it difficult to determine whether the method generalizes beyond the selected benchmarks. The paper should include additional domains, longer texts, or at least stronger robustness analyses.

6. **Ablation evidence is incomplete.**  
   The paper shows that removing the curriculum hurts performance, but it does not isolate whether the gains come from the specific operator ordering, the changing augmentation distribution, exposure to back-translation later in training, or simply a favorable mixture of augmentations. Useful controls would include constant-strength schedules, alternative orderings, smoothly weighted mixtures, and schedules matched for the total number of applications of each operator.

7. **Reproducibility details are lacking.**  
   Important information is missing, including the exact CERT and SimCSE implementations, sequence lengths, optimizer hyperparameters, projection-head architecture, augmentation details, translation model, preprocessing, data split construction, and the criteria used for early stopping. The statement that validation sets contain 200 labeled examples is also unclear regarding whether these are drawn from the original training data or otherwise externally defined.

8. **Potential ambiguity in the low-resource protocol.**  
   The paper uses “the remaining training sentences without labels” for contrastive training. It should explicitly state whether the 500 labeled examples and validation examples are excluded from the unlabeled corpus, and whether any test or validation text is used during intermediate training. This is especially important for comparisons with prior work.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 56/100 |
| Novelty | 62/100 |
| Significance | 58/100 |
| Clarity | 76/100 |
| **Final average** | **63.0/100** |

### Recommendation

**Reject**

The paper presents a clear and plausible idea, and the reported results are promising. However, the current experimental design does not adequately support the main claim because of unequal baseline tuning, incomplete specification of the curriculum and data protocol, limited statistical analysis, and insufficient controls for the source of the observed improvement. A revised version with fair hyperparameter tuning, stronger ablations, significance testing, and substantially improved reproducibility would be worthwhile.