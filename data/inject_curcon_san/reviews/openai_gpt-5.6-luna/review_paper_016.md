## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The central idea is to begin contrastive training with weak perturbations and progressively introduce stronger augmentations, including back-translation. Results on four datasets suggest consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant: exploiting unlabelled data in low-resource classification is practically important.
- The method is conceptually simple and compatible with existing contrastive intermediate-training pipelines.
- The evaluation includes multiple datasets, several baselines, multiple random seeds, ablations, and different label budgets.
- The reported improvements are consistent across the four benchmarks.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

1. **Limited novelty.**  
   The contribution is primarily a manually designed augmentation schedule. Curriculum learning and augmentation scheduling are established ideas, and the paper does not clearly distinguish CurCon from prior work on augmentation curricula or scheduled perturbation strength.

2. **Insufficient experimental detail.**  
   Important aspects of the method are underspecified, including:
   - how augmentation “strength” is mathematically tied to the curriculum value;
   - whether operators are sampled independently or exclusively;
   - how two views are generated;
   - how back-translation is handled and whether the same preprocessing is used for all methods;
   - the exact data splits and preprocessing procedures.

3. **Potentially unfair baseline tuning.**  
   CurCon receives a 48-configuration grid search, while baselines use hyperparameters from their original papers. This may disadvantage the baselines, especially across different datasets and label budgets. A fair comparison should tune all methods under the same validation protocol.

4. **Weak statistical support.**  
   Five seeds are useful, but the paper reports no confidence intervals or significance tests. Given that several gains are only 0.5–1.1 points, it is unclear whether the improvements over CERT are statistically reliable.

5. **Ablation coverage is incomplete.**  
   The paper compares against a fixed mixture and a reversed curriculum, but does not isolate:
   - each augmentation operator;
   - alternative schedules such as cosine, stepwise, or randomized schedules;
   - matched-compute or matched-augmentation baselines;
   - the sensitivity to curriculum length;
   - whether the benefit comes from the ordering itself or simply from spending more training steps with particular augmentations.

6. **Minor formal issue.**  
   The definition \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the text later states that \(L=0\) corresponds to a fixed mixture. This should be specified separately.

7. **Claims are somewhat stronger than the evidence.**  
   The experiments cover only four short English classification datasets using BERT-base. The conclusions should be framed as evidence for these settings rather than broad evidence that curriculum scheduling is generally effective.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 55/100 |
| Significance | 57/100 |
| Clarity | 78/100 |

### Final score

\[
\frac{58+55+57+78}{4} = 62.0
\]

## Final recommendation: **Reject**

The paper presents a plausible and clearly described idea with encouraging preliminary results, but the methodological novelty is modest and the experimental evidence does not yet establish that the curriculum itself—rather than augmentation choice, tuning, or other confounds—is responsible for the gains. A stronger revision would require fairer baseline tuning, statistical testing, more complete schedule and augmentation ablations, and clearer formal and implementation details.