## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. It gradually expands the set of available text augmentations during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important: improving text classification with very limited labelled data.
- The method is simple, model-agnostic, and does not add inference-time parameters.
- The experimental setup includes several reasonable baselines and multiple datasets.
- Results are reported over five random seeds, with standard deviations.
- The ablations address the curriculum, curriculum direction, and back-translation.
- The paper is generally well organized and easy to follow.

### Weaknesses

1. **The curriculum is not actually linear in augmentation strength.**  
   Although the paper describes a linear schedule, the implementation uses thresholded operator availability. The augmentation distribution changes discontinuously at 0.25, 0.5, and 0.75, and after 0.75 all operators are sampled uniformly. This is a staged curriculum rather than a clearly linear increase in expected perturbation strength.

2. **Baseline comparisons may be unfair.**  
   CurCon’s learning rate, temperature, and curriculum length are tuned using a 48-configuration grid on each validation set, while the baselines use hyperparameters from their original papers. For a low-resource setting, this can substantially disadvantage the baselines. All methods should receive comparable tuning budgets.

3. **Statistical evidence is limited.**  
   Five seeds are useful but insufficient to establish that improvements of 0.5–1.1 points are statistically meaningful. No paired significance tests, confidence intervals for method differences, or per-seed results are provided.

4. **Important implementation details are missing.**  
   The paper does not fully specify the back-translation system, WordNet version and synonym filtering, tokenization behavior after deletion, the exact augmentation distribution for the two views, projection-head details, learning rates, or early-stopping protocol. These omissions hinder reproducibility.

5. **The experimental scale is narrow.**  
   Results are limited to four relatively short English classification datasets and BERT-base. The method’s claimed generality is therefore not strongly established.

6. **The ablation design could be stronger.**  
   The paper should compare against curricula with matched average augmentation strength, random schedules, smooth probability interpolation, and schedules that vary only operator difficulty. Otherwise, the gain may result from the particular final augmentation mixture rather than curriculum learning itself.

7. **The cost analysis is underspecified.**  
   The reported 12% overhead is not supported with detailed wall-clock measurements, hardware utilization, or a clear accounting of preprocessing versus training time.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 59/100 |
| Novelty | 57/100 |
| Significance | 60/100 |
| Clarity | 82/100 |

### Final average

\[
\frac{59 + 57 + 60 + 82}{4} = 64.5
\]

## Final recommendation: **Reject**

The paper presents a plausible and potentially useful idea, and the results are consistently positive. However, the contribution is incremental, the curriculum definition is somewhat inconsistent with the stated linear-scheduling claim, and the experimental comparisons do not provide sufficiently strong evidence because of unequal hyperparameter tuning and limited statistical analysis. A revised version with fair baseline tuning, stronger schedule-controlled ablations, fuller reproducibility details, and significance testing could become publishable.