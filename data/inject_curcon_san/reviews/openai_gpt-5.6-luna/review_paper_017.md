## Overall assessment

The paper presents a straightforward curriculum strategy for contrastive intermediate training: start with weaker text augmentations and progressively introduce stronger ones before low-resource fine-tuning. The idea is intuitive and the reported results are consistently positive, but the empirical evidence is not yet strong enough to establish that the curriculum itself is responsible for the gains. The contribution is also relatively incremental.

### Scores

| Criterion | Score | Assessment |
|---|---:|---|
| **Soundness** | **64/100** | The method is plausible and the experiments include useful ablations, but several important methodological details and controls are missing. The baseline comparison is potentially unfair because CurCon is tuned with a 48-configuration grid search while baselines use hyperparameters from prior papers. The results also do not report statistical significance or confidence intervals over sampled labelled subsets. |
| **Novelty** | **55/100** | Scheduling augmentation difficulty during contrastive training is a reasonable adaptation of curriculum learning, but the conceptual contribution is modest. The paper would need stronger differentiation from existing augmentation curricula, contrastive-learning schedules, and adaptive augmentation methods. |
| **Significance** | **60/100** | The reported gains are consistent and potentially useful in low-resource settings, especially at 100 labels. However, the average improvement over CERT is only 1.1 points at the main setting and 0.5 points with 1,000 labels. The evaluation is limited to four short English classification datasets and one encoder family. |
| **Clarity** | **78/100** | The paper is well organized and easy to follow. Nevertheless, the curriculum policy is underspecified: it is unclear how operator probabilities change continuously with the curriculum level, whether augmentations are applied independently or mutually exclusively, and how the back-translation views are generated. Dataset splits, validation-set construction, and sampling procedures also require clarification. |

### Final average

\[
\frac{64 + 55 + 60 + 78}{4} = \mathbf{64.25/100}
\]

## Recommendation: **Reject**

The paper has a clear presentation, a sensible method, and promising preliminary results. However, the novelty is limited and the experimental design does not yet convincingly isolate the effect of the curriculum. In particular, the paper should address:

1. **Fair baseline tuning:** tune all methods under comparable validation budgets rather than using prior-paper hyperparameters only for baselines.
2. **Multiple labelled-subset samples:** repeat experiments across independently sampled 100/500/1,000-example subsets, not only across random training seeds.
3. **Stronger controls:** compare against fixed augmentation mixtures matched for augmentation frequency, augmentation severity, and compute.
4. **Statistical testing:** report confidence intervals or paired significance tests.
5. **Clearer schedule specification:** define the exact operator-selection probabilities at every stage.
6. **Broader evaluation:** include additional domains, longer documents, encoders, and ideally multilingual or cross-domain settings.

With these additions, the work could become a solid empirical paper, but in its current form the evidence is insufficient for acceptance.