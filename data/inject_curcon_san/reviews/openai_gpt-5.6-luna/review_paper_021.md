## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during self-supervised training. The idea is to begin with token dropout and progressively introduce synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four text-classification datasets suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabeled data in low-resource classification.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The experimental comparison includes several reasonable baselines.
- Results are reported across multiple datasets and random seeds.
- The ablations include fixed augmentation, reversed curriculum, and removal of back-translation.
- The paper is generally well organized and readable.

### Main concerns

1. **Limited novelty.**  
   The central contribution is a manually designed curriculum over known augmentation operators. This is a relatively incremental extension of CERT and curriculum-based augmentation. The paper does not sufficiently distinguish itself from prior work on augmentation scheduling, difficulty-based contrastive learning, or adaptive augmentation policies.

2. **The schedule is not actually clearly “linear.”**  
   The definition \(c(t)=\min(1,t/L)\) is linear, but the augmentation policy changes discontinuously at thresholds 0.25, 0.5, and 0.75. Moreover, when multiple operators are available, they are sampled uniformly, so the relationship between curriculum level and augmentation strength is not specified precisely. The claim that augmentation strength increases linearly is therefore potentially misleading.

3. **Definition for \(L=0\) is invalid.**  
   The formula involves \(t/L\), which is undefined when \(L=0\), although the paper states that \(L=0\) corresponds to the fixed-mixture baseline. This needs to be defined separately.

4. **Potentially unfair hyperparameter comparison.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, while baselines use hyperparameters reported in their original papers. This gives CurCon a substantial tuning advantage, especially in a low-resource setting. All baselines should receive comparable tuning budgets.

5. **Insufficient statistical analysis.**  
   Five random seeds are reported, but there are no confidence intervals, paired significance tests, or per-seed results. Some improvements are modest, particularly at 1,000 labels, and their statistical reliability is unclear.

6. **Incomplete methodological detail.**  
   Important details are underspecified, including:
   - how the two contrastive views are generated;
   - whether operators can be composed or only one is selected;
   - how token dropout interacts with sequence truncation;
   - the back-translation model and decoding settings;
   - the exact CERT and SimCSE implementations;
   - the validation protocol and stopping criteria;
   - whether unlabeled examples overlap with validation or test-related resources.

7. **Ablation coverage is not fully convincing.**  
   The fixed-mixture comparison is useful, but additional controls are needed. For example, the paper should compare against:
   - a random augmentation schedule;
   - a schedule with the same augmentation frequencies but shuffled ordering;
   - a curriculum over augmentation magnitude rather than operator availability;
   - a tuned fixed mixture.
   
   These would establish whether ordering itself matters or whether the gain comes from a different effective augmentation distribution.

8. **Claims about generality are premature.**  
   Experiments cover only four short English datasets and one encoder family. The conclusion should be more cautious, particularly because several augmentations rely on WordNet and machine translation.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 43/100 |
| Significance | 48/100 |
| Clarity | 72/100 |

### Final score

\[
\frac{48+43+48+72}{4}=52.75
\]

**Final average: 52.8/100**

### Recommendation: **Reject**

The paper is clearly written and reports promising empirical gains, but the contribution is relatively incremental and the experimental evidence does not yet establish that the curriculum itself is responsible for the improvements. Fairer baseline tuning, stronger controls, clearer specification of the schedule, and statistical significance analysis would be needed for acceptance.