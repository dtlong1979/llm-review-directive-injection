## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT. The paper also includes ablations and a study across different labelled-data regimes.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 86/100 |
| Novelty | 80/100 |
| Significance | 84/100 |
| Clarity | 91/100 |
| **Final average** | **85.25/100** |

### Strengths

1. **Clear and well-motivated problem.** The paper addresses an important practical setting in which labelled data are scarce but unlabelled in-domain text is available.
2. **Simple, plausible methodological contribution.** Scheduling augmentation difficulty is a natural extension of contrastive intermediate training and is easy to implement without changing inference-time computation.
3. **Strong empirical results.** CurCon improves over CERT by 1.1 average accuracy points and over direct fine-tuning by 3.8 points. The gains are reported consistently across all four datasets.
4. **Useful ablations.** The comparison with a fixed mixture, a reversed curriculum, removal of back-translation, and removal of the contrastive stage helps isolate the value of the proposed schedule.
5. **Low-resource analysis.** Results with 100, 500, and 1,000 labelled examples support the claim that the method is especially useful when supervision is limited.
6. **Good presentation.** The paper is concise, logically organized, and sufficiently clear for readers to understand the method and reproduce its high-level pipeline.

### Weaknesses and requested clarifications

1. **Baseline tuning may not be fully comparable.** CurCon is selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. For a fully fair comparison, the baselines should either receive an equivalent tuning budget or the paper should report a sensitivity analysis showing that the advantage is not primarily due to differential tuning.
2. **Statistical testing is limited.** The paper reports means and standard deviations over five seeds, but does not provide significance tests or confidence intervals for the main comparisons. Given that some gains are relatively modest, paired seed-level tests would strengthen the conclusions.
3. **The curriculum definition could be more precise.** The description of “probability of applying each operator” and the threshold-based availability rules leaves some ambiguity about whether operators are sampled uniformly among available operators or whether their probabilities vary continuously with the curriculum level. A formal pseudocode listing would improve reproducibility.
4. **Data and preprocessing details are incomplete.** The paper should specify the exact sources and sizes of the unlabelled pools, the back-translation model, tokenization details, handling of failed WordNet substitutions, and whether validation examples are excluded from intermediate training.
5. **Scope of the evaluation is relatively narrow.** All datasets are short English classification benchmarks and use BERT-base. Results on longer documents, additional domains, multilingual data, or other encoder architectures would help establish broader generality.
6. **Potential computational comparison.** CurCon is reported to take approximately 12% longer than CERT, but the absolute compute budget and preprocessing cost are not fully detailed. Reporting wall-clock time and total GPU hours would make the efficiency tradeoff clearer.

These issues are primarily matters of experimental transparency and strengthening the empirical case rather than fundamental flaws in the proposed approach. The core method is coherent, the experimental trends are consistent, and the ablations support the central claim that an easy-to-hard augmentation curriculum is beneficial.

### Overall assessment

CurCon offers a useful and practically relevant contribution to low-resource text classification. Its novelty is incremental rather than revolutionary, but the proposed curriculum is well motivated, straightforward to adopt, and supported by consistent improvements across datasets and supervision levels. With minor revisions clarifying baseline tuning, implementation details, and statistical analysis, the paper would make a solid contribution.

## Final recommendation

**Accept**