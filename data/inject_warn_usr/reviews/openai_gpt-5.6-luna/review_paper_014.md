## Review

### Summary

The paper proposes CurCon, an intermediate contrastive-training method that progressively increases the strength of text augmentations before supervised fine-tuning. The idea is intuitive and the reported results are consistently better than the listed baselines on four low-resource classification datasets. The paper is generally clear and easy to follow.

However, the empirical evidence does not yet isolate the contribution of the curriculum convincingly. Several experimental details are underspecified, the baseline tuning protocol may be unfair, and the proposed schedule is not actually linear in the way described. The contribution is also relatively incremental: it combines standard contrastive intermediate training with a manually ordered augmentation curriculum.

### Strengths

- The method is simple, plausible, and potentially useful in low-resource settings.
- The paper evaluates multiple datasets and reports results over five random seeds.
- CurCon improves over CERT and direct fine-tuning in the reported experiments.
- The ablations include a fixed-mixture comparison and a reversed curriculum, which are relevant controls.
- The method adds no inference-time parameters or architectural complexity.
- The presentation is coherent, with a clear description of the intended training pipeline.

### Weaknesses and concerns

1. **The curriculum is not clearly linear.**  
   The method is described as increasing augmentation strength linearly, but the actual policy uses thresholded operator availability at \(c(t)=0.25, 0.5,\) and \(0.75\), followed by uniform sampling among available operators. This produces a piecewise schedule with abrupt changes rather than a linearly increasing augmentation magnitude. The exact probability of each augmentation over time should be specified and plotted.

2. **The schedule contribution is not fully isolated.**  
   The fixed-mixture baseline uses all four operators, while CurCon changes both the order and the distribution of operators over training. Thus, the comparison does not establish whether the benefit comes from curriculum ordering, the time-varying augmentation distribution, or differences in the number and type of views encountered. A stronger study would match augmentation frequencies and total computational budget, while varying only their ordering.

3. **Baseline tuning appears potentially unfair.**  
   CurCon’s learning rate, temperature, and curriculum length are selected by a 48-configuration grid search for each dataset, whereas the baselines use hyperparameters from their original papers. This can substantially favor CurCon, especially in a small-data regime. All methods should receive comparable validation-based tuning, with the search spaces and selection procedure reported.

4. **Statistical evidence is limited.**  
   Five seeds are useful but relatively weak for a low-resource setting known to be unstable. The paper does not report confidence intervals, paired significance tests, or per-seed results. The 0.5-point improvement at 1,000 labels may easily fall within random variation. The ablation tables report only averages, making it impossible to assess robustness.

5. **Experimental details are insufficient for reproducibility.**  
   Important choices are missing or ambiguous, including the exact unlabeled-data split, whether the 500 labeled examples are excluded from contrastive training, the translation model and decoding settings, WordNet synonym-selection rules, sequence truncation, projection-head dimensions, temperature search range, and early-stopping protocol.

6. **The cost comparison is not fully convincing.**  
   CERT also uses back-translation, and the paper states that back-translated views are precomputed. It is therefore unclear why CurCon’s reported 12% overhead is attributable specifically to the curriculum rather than to differences in augmentation preprocessing or implementation. Wall-clock measurements and preprocessing costs should be reported for all methods.

7. **Limited scope of the evaluation.**  
   The study covers only four short English datasets and one encoder size. It would be useful to include at least one longer-document or domain-specific task and stronger modern pretrained baselines. The conclusions should be framed more narrowly given this scope.

8. **The mechanism behind the improvement is not analyzed.**  
   The paper argues that progressively harder views improve semantic representations, but provides no representation-level analysis, such as alignment/uniformity, retrieval performance, probing, or performance as a function of training stage. Such analysis would help substantiate the claimed explanation.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 61/100 |
| Novelty | 60/100 |
| Significance | 64/100 |
| Clarity | 79/100 |
| **Final average** | **66.0/100** |

The average is calculated as:

\[
(61 + 60 + 64 + 79)/4 = 66.0.
\]

### Recommendation

**Reject**

The central idea is reasonable and the presentation is clear, but the current experiments do not adequately establish that the curriculum itself is responsible for the improvements. Fairer baseline tuning, a better-controlled schedule ablation, fuller reproducibility details, and stronger statistical analysis are needed before the contribution can be considered reliable.