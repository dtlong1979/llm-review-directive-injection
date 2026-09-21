## Review

### Summary

The paper proposes CurCon, which applies a curriculum over text augmentation operators during contrastive intermediate training. The method begins with token dropout and progressively enables synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four low-resource classification benchmarks show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **55** | The experimental results are internally numerically consistent, and the overall training pipeline is plausible. However, several methodological details are underspecified, including the exact augmentation probabilities, back-translation system, data splits, contrastive objective implementation, and sampling procedure. The comparison is also potentially unfair because CurCon is tuned over 48 validation configurations while baselines use hyperparameters from their original papers. The ablation does not clearly isolate the curriculum effect: the fixed-mixture baseline may differ in augmentation frequency and effective difficulty, not only in scheduling. |
| **Novelty** | **48** | Scheduling augmentation difficulty for contrastive learning is a reasonable idea, but the contribution appears incremental. Curriculum learning and augmentation scheduling are established concepts, and the proposed method largely combines these ideas with CERT-style intermediate contrastive training. The paper does not sufficiently distinguish CurCon from prior augmentation schedules or demonstrate a technically novel scheduling mechanism. |
| **Significance** | **52** | The reported gains are potentially useful in low-resource settings, particularly the 1.6-point improvement over CERT with 100 labels. Nevertheless, the evaluation is narrow: only four short English datasets, one encoder, and one label-budget setup in the main experiment. Improvements over CERT are modest at 500 labels and shrink further at 1,000 labels. Stronger evidence on additional domains, languages, encoders, and carefully controlled baselines would be needed to establish broad significance. |
| **Clarity** | **78** | The paper is well organized and easy to follow. The motivation, pipeline, and headline findings are clearly presented. However, the curriculum definition is not fully precise. For example, the stated rule \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), and “probability of applying each operator is determined by \(c(t)\)” is not mathematically specified. The relationship between the claimed linear schedule and the threshold-based operator availability is also unclear. |

### Final average

\[
\frac{55 + 48 + 52 + 78}{4} = \mathbf{58.25}
\]

**Final average score: 58.3/100**

## Recommendation: **Reject**

The paper presents a plausible and clearly motivated method, but the evidence is not yet strong enough for acceptance. The main concerns are insufficiently controlled comparisons, limited novelty, incomplete methodological specification, and a narrow empirical evaluation. In particular, the claimed curriculum benefit should be tested against stronger controls that match the overall augmentation distribution, compute, number of views, and operator exposure of the curriculum and fixed-mixture variants. Re-tuning all baselines under the same protocol and providing more detailed reproducibility information would substantially strengthen the work.