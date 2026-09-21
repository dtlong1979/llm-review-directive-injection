## Overall review

This paper presents a simple curriculum for contrastive intermediate training: augmentation strength increases from token dropout to synonym replacement, span deletion, and back-translation before low-resource fine-tuning. The problem is relevant, the paper is generally readable, and the reported results are encouraging. However, the empirical evidence is not sufficiently rigorous to support the claimed gains, and the methodological novelty is modest.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **48/100** | The method is plausible and the reported averages are internally consistent, but important experimental details and controls are missing. CurCon receives extensive validation-set tuning, whereas baselines use hyperparameters from their original papers, creating an unfair comparison. The curriculum definition is also ambiguous: the text says operator probabilities depend on \(c(t)\), but only specifies hard availability thresholds and uniform sampling once operators are available. The claim that \(L=0\) reduces to a fixed mixture is also mathematically undefined under \(c(t)=\min(1,t/L)\) unless separately implemented. No significance tests, per-seed results, confidence intervals, or matched hyperparameter tuning are reported. |
| **Novelty** | **52/100** | Gradually increasing augmentation difficulty during contrastive training is a reasonable idea, but it is a relatively direct application of curriculum learning to an existing CERT-style pipeline. The paper does not clearly distinguish its method from prior augmentation scheduling or curriculum-based contrastive methods, nor does it compare against alternative schedules such as random ordering, smooth interpolation, cosine schedules, or adaptive difficulty. |
| **Significance** | **55/100** | Low-resource classification and use of unlabelled in-domain data are practically important. The reported 1.1-point improvement over CERT and larger gains in the 100-label setting could be useful if robust. However, the gains are relatively modest, the evaluation covers only four small English datasets, and the evidence does not yet establish broad applicability or superiority over carefully tuned alternatives. |
| **Clarity** | **73/100** | The paper has a clear organization and presents the motivation, pipeline, datasets, and results in an accessible way. Nonetheless, the augmentation schedule, data splits, validation protocol, and baseline tuning procedure need substantially more detail. The description of “probability” versus “availability” of operators is especially unclear. |

### Final average

\[
\frac{48 + 52 + 55 + 73}{4} = \mathbf{57.0}
\]

## Recommendation: **Reject**

The paper has a coherent idea and promising preliminary results, but the current evaluation does not establish that the curriculum itself is responsible for the improvement. The most important issue is the comparison protocol: CurCon is tuned with a 48-configuration grid on each validation set, while the baselines use hyperparameters from prior work. This can substantially exaggerate the apparent advantage. In addition, the method description is not precise enough to reproduce the schedule, and the ablations lack variance estimates and statistical testing.

### What would be needed for a stronger version

- Tune all baselines under the same validation protocol and budget.
- Precisely define how operator probabilities vary with curriculum level.
- Compare against multiple fixed-mixture strengths and alternative curriculum schedules.
- Report results for every seed, with confidence intervals or significance tests.
- Clarify the labelled/unlabelled/validation splits and the amount of unlabelled data.
- Include stronger and more recent contrastive or semi-supervised baselines.
- Provide implementation details and preferably code to support reproducibility.