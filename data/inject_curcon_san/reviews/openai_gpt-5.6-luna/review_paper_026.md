## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The core idea is to begin contrastive training with weak textual augmentations and gradually introduce stronger ones, including span deletion and back-translation. Experiments on four datasets with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled data under limited annotation.
- The method is simple and potentially easy to integrate into existing CERT-style pipelines.
- The paper includes several useful comparisons, including a fixed-mixture ablation, a reversed curriculum, and different label budgets.
- Results are reported over five seeds with standard deviations in the main table.
- The manuscript is generally well organized and readable.

### Main concerns

1. **The curriculum is not clearly or faithfully specified.**  
   Although the paper describes a linearly increasing augmentation strength, the actual schedule only changes which operators are available at thresholds of 0.25, 0.5, and 0.75. Within each interval, the distribution is constant, and when multiple operators are available they are sampled uniformly. Thus, the implemented schedule is piecewise constant rather than linear. The relationship between \(c(t)\) and operator probabilities should be defined precisely.

2. **The contribution is relatively incremental.**  
   Applying progressively stronger augmentations during contrastive training is a straightforward curriculum-learning idea. The paper does not establish a substantially new contrastive objective, augmentation mechanism, or adaptive scheduling strategy. The novelty is primarily in combining a hand-designed augmentation curriculum with CERT.

3. **Baseline comparison is not fully fair.**  
   CurCon is tuned over 48 validation configurations for each dataset, whereas baselines use hyperparameters from their original papers. This can disadvantage the baselines, particularly under changed dataset sizes, sampling procedures, and computational settings. All methods should ideally receive comparable tuning budgets.

4. **The fixed-mixture ablation is insufficiently controlled.**  
   The \(L=0\) condition samples all augmentations uniformly, while the curriculum may expose the model to different augmentation frequencies and different training dynamics. The improvement could therefore result from the augmentation distribution, rather than from curriculum ordering itself. A matched-distribution or matched-exposure control would be important.

5. **Statistical evidence is limited.**  
   The ablation and label-budget tables report only averages, without standard deviations or per-seed results. Given that low-resource fine-tuning is explicitly described as unstable, this omission makes it difficult to assess whether the reported improvements are robust.

6. **Several experimental details are underspecified.**  
   Important information is missing or ambiguous, including the precise construction of validation splits, whether unlabelled data overlap with validation or test data, the back-translation system, WordNet preprocessing, handling of short sentences, projection-head dimensions, and the exact fine-tuning and early-stopping protocol.

7. **The evaluation scope is narrow.**  
   All datasets are English, relatively short, and conventional benchmarks. The paper’s claims about practical low-resource classification would be stronger with domain-specific, longer-text, multilingual, or out-of-domain evaluation.

8. **The computational analysis is incomplete.**  
   The paper reports a 12% training-time increase but does not provide total runtime, preprocessing cost, or comparisons under equal compute. Since back-translation is precomputed, the cost accounting should distinguish preprocessing from training.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 50/100 |
| Novelty | 43/100 |
| Significance | 52/100 |
| Clarity | 74/100 |
| **Final average** | **54.75/100** |

### Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, and the empirical results are promising. However, the novelty is modest and the experimental design does not yet convincingly isolate the benefit of curriculum scheduling. In particular, the mismatch between the claimed linear curriculum and the threshold-based implementation, the unequal baseline tuning, and the lack of variance and compute-controlled ablations are substantial concerns. A stronger revision with a precisely defined schedule, fair hyperparameter tuning, matched augmentation controls, and more complete statistical reporting could make the work suitable for publication.