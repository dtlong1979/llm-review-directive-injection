## Review

### Summary

The paper proposes CurCon, an intermediate contrastive-training method that increases the strength of text augmentations over training. It evaluates the method on four datasets in a 500-label setting and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **60** | The method and experimental results are broadly plausible, and the reported averages are internally consistent. However, important methodological details are underspecified, including the exact augmentation probabilities, preprocessing, back-translation setup, model and optimization details, and validation protocol. The comparison is also potentially unfair because CurCon is tuned with a 48-configuration grid search, whereas the baselines use hyperparameters from their original papers. Results are based on only five seeds, with no significance tests or per-seed results. The curriculum is described as linear, but the actual policy changes through discrete availability thresholds, making the claimed schedule less clearly defined. |
| **Novelty** | **55** | Applying a gradually increasing augmentation schedule to contrastive intermediate training is a reasonable idea, but it is a relatively incremental combination of existing curriculum learning, text augmentation, and contrastive-training techniques. The schedule is hand-designed and simple, and the paper does not establish a strong conceptual or algorithmic advance over tuning augmentation mixtures or using adaptive augmentation methods. |
| **Significance** | **61** | Low-resource text classification is important, and the reported gains over CERT are potentially useful. Nevertheless, the average improvement is modest, especially at 1,000 labels, and the evaluation is limited to four short English classification datasets and one encoder family. Stronger evidence would be needed to demonstrate broad practical impact, including comparisons with tuned augmentation policies, larger or multilingual models, and more realistic low-resource settings. |
| **Clarity** | **80** | The paper is well organized and easy to follow. The motivation, method, tables, and limitations are presented clearly. Some technical ambiguity remains: the exact probability schedule is not specified, “augmentation strength” does not precisely match the threshold-based operator-availability mechanism, and important implementation and data-splitting details are missing. |

### Final average

\[
\frac{60 + 55 + 61 + 80}{4} = \mathbf{64.0}
\]

## Final recommendation: **Reject**

The paper presents a clear and plausible empirical idea, but the contribution is currently too incremental and the experimental evidence is not sufficiently rigorous for acceptance. The main concerns are the limited novelty, possible unfair baseline tuning, incomplete specification of the curriculum and augmentation policy, lack of statistical testing, and narrow evaluation scope. A revised version with carefully tuned baselines, stronger ablations, significance analysis, full reproducibility details, and comparisons against learned or continuously weighted augmentation schedules could be substantially stronger.