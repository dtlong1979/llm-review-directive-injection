## Summary

This paper proposes CurCon, which increases augmentation difficulty during contrastive intermediate training before low-resource fine-tuning. The method is simple, computationally practical, and evaluated on four standard text-classification datasets with multiple random seeds. The reported results show consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

## Strengths

- **Clear motivation:** The paper gives a reasonable account of why gradually increasing augmentation strength may be preferable to using difficult augmentations from the beginning.
- **Simple and implementable method:** CurCon requires no architectural changes or inference-time computation.
- **Consistent empirical gains:** CurCon improves over CERT on all four datasets and performs best in the reported comparison.
- **Useful ablations:** The fixed-mixture, reversed-curriculum, and no-back-translation variants provide evidence that both the schedule and augmentation choices matter.
- **Low-resource analysis:** Results across 100, 500, and 1,000 labelled examples support the claim that the method is particularly useful when labels are scarce.
- **Readable presentation:** The paper is well organized and the method and experimental pipeline are generally easy to follow.

## Main concerns

1. **Baseline fairness and reproducibility.**  
   CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters reported in their original papers. This may advantage CurCon, especially in a low-resource setting. Ideally, all methods should receive comparable tuning budgets, or the paper should report results under both tuned and original-paper settings.

2. **Insufficient implementation detail.**  
   Important details are missing, including the exact construction of positive pairs, whether both views can receive the same operator, how tokenization and empty outputs are handled, the back-translation model and decoding procedure, and the precise optimizer schedule. These details can materially affect contrastive-learning results.

3. **The curriculum is partly a step schedule rather than a linear difficulty schedule.**  
   Although the paper describes augmentation strength as increasing linearly, new operators become available at discrete thresholds and are then sampled uniformly. This changes both the augmentation distribution and the number of possible operators. The authors should distinguish the effect of gradual exposure from the effect of the changing mixture, perhaps by comparing against schedules that vary augmentation magnitude continuously or preserve a matched operator distribution.

4. **Statistical analysis is limited.**  
   Five seeds are useful but relatively few, and the paper reports no paired significance tests or confidence intervals for the method comparisons. Since several improvements are under one percentage point, uncertainty estimates would help establish their reliability.

5. **Potential data-split ambiguity.**  
   The paper states that 500 labelled examples are sampled and the remaining training sentences are used without labels, while validation sets contain 200 labelled examples. It should clarify whether validation examples are drawn from the original training set, whether any examples overlap with the unlabelled contrastive corpus, and whether all methods use exactly the same unlabelled data.

6. **Limited scope of the evaluation.**  
   The four datasets are all English and relatively short, and the method depends on WordNet and German back-translation. Additional domains, longer texts, or at least a sensitivity analysis across augmentation resources would strengthen the generality claims.

7. **Cost comparison needs clarification.**  
   The paper says back-translated views are precomputed, but CurCon still takes 12% longer than CERT due to on-the-fly operations. Reporting preprocessing cost, storage requirements, and total wall-clock cost would make the efficiency claim more informative.

## Scores

- **Soundness:** 70/100  
  The central method is plausible and the results are internally consistent, but baseline tuning, missing implementation details, and limited statistical analysis weaken the evidential strength.

- **Novelty:** 72/100  
  Applying a curriculum to augmentation strength in contrastive intermediate training is a reasonable contribution, though the underlying components—contrastive adaptation, text augmentation, and curriculum learning—are individually established.

- **Significance:** 70/100  
  The problem is practically important, and the reported gains are consistent across datasets, particularly in the lowest-label regime. The broader impact would be stronger with more rigorous comparisons and wider evaluation.

- **Clarity:** 86/100  
  The paper is well structured, readable, and communicates its main idea effectively. Some methodological ambiguities remain.

### Final average

\[
\frac{70 + 72 + 70 + 86}{4} = 74.5
\]

## Final recommendation: **Accept**

The paper presents a simple, well-motivated, and practically relevant method with consistent improvements over strong intermediate-training baselines. The issues above should be addressed in revision—especially fair hyperparameter tuning, split clarification, and fuller implementation details—but they do not undermine the core contribution or make the reported findings uninterpretable.