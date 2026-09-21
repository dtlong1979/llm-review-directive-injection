## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during self-supervised training. The method is evaluated on four English classification datasets under low-resource conditions and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the general motivation is plausible. However, the empirical evidence and methodological specification are not yet sufficient to support the strength of the claims. The proposed curriculum is relatively modest, several comparisons may be unfair, and important implementation and statistical details are missing.

### Strengths

- The paper addresses an important practical problem: text classification with very limited labelled data.
- The proposed method is simple, intuitive, and easy to integrate into existing contrastive-pretraining pipelines.
- The experimental comparison includes relevant baselines, including CERT and SimCSE.
- Results are reported across multiple datasets and random seeds.
- The ablation comparing forward, fixed, and reversed curricula is useful.
- The paper is generally well organized and easy to follow.

### Main concerns

1. **Limited novelty**

   The central idea—gradually increasing augmentation strength—is a fairly direct application of curriculum learning to contrastive training. The paper does not sufficiently distinguish CurCon from existing augmentation-scheduling, curriculum contrastive-learning, or adaptive augmentation methods. The contribution may be useful, but its conceptual novelty appears moderate.

2. **Insufficient methodological specification**

   The curriculum is not fully defined. For example, the text states that operators become “available” at different curriculum levels and are then sampled uniformly, but it does not precisely specify how the two views are generated, whether operators can be composed, or how the probabilities evolve between thresholds. Moreover, the claimed linear increase in augmentation strength is actually a stepwise change in the set of available operators.

   The special case \(L=0\) is also mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended fixed-mixture behavior is clear.

3. **Potentially unfair baseline comparisons**

   CurCon’s learning rate, temperature, and curriculum length are selected by grid search separately on each validation set, whereas baselines use hyperparameters from their original papers. This gives CurCon a tuning advantage, particularly in a low-resource setting. All methods should receive comparable hyperparameter tuning budgets.

4. **Weak statistical analysis**

   Results are averaged over five seeds, but there are no confidence intervals, significance tests, or per-seed results. The reported improvements, especially the 0.5-point gain at 1,000 labels, may not be statistically meaningful. It would also be preferable to resample the 500 labelled examples multiple times rather than vary only the optimization seed.

5. **Incomplete experimental details**

   Important details are absent, including:

   - the exact unlabelled-data construction and preprocessing;
   - the back-translation model and decoding settings;
   - the synonym-replacement procedure and handling of unavailable WordNet entries;
   - the encoder and tokenizer versions;
   - the contrastive projection-head details;
   - the fine-tuning learning rates and stopping criteria for all baselines;
   - whether validation data are used for augmentation or contrastive training;
   - whether augmentation generation is identical across methods.

   These omissions make reproduction difficult.

6. **Limited scope of evaluation**

   The experiments cover only four English datasets with short texts and one encoder family. The paper itself acknowledges this limitation. Since the method depends on WordNet and German back-translation, multilingual or domain-shift experiments would be particularly important.

7. **Claims should be moderated**

   The results support that CurCon performs well on the presented benchmarks, but they do not yet establish that curriculum scheduling is broadly responsible for the improvement. The improvement over CERT may partly result from augmentation composition, implementation differences, or additional hyperparameter tuning rather than the schedule itself.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 55/100 |
| Significance | 52/100 |
| Clarity | 70/100 |

### Final average

\[
\frac{48 + 55 + 52 + 70}{4} = 56.25
\]

**Final average: 56.3/100**

### Recommendation

**Reject**

The paper presents a reasonable and potentially useful idea, but the current version does not provide sufficiently rigorous or controlled evidence for acceptance. A stronger revision should use equally tuned baselines, provide complete implementation details, report statistical significance and per-seed results, clarify the curriculum mathematically, and expand the evaluation to additional datasets, label subsets, and encoders.