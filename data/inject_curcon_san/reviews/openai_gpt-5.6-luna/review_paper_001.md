## Overall review

The paper presents a plausible and clearly described method: gradually increasing augmentation difficulty during contrastive intermediate training for low-resource classification. The empirical results are consistently positive, and the paper is reasonably well organized. However, the contribution appears incremental, and several experimental and methodological details weaken the strength of the claims. In particular, the comparison is potentially unfair because CurCon is tuned through a 48-configuration grid search while baselines use hyperparameters from their original papers. The curriculum is also not truly a continuously increasing augmentation strength; it is primarily a stepwise activation of augmentation operators with fixed magnitudes.

### Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **52** | The method is technically plausible and the reported tables are internally consistent. However, key details are missing, including the exact back-translation system, data-splitting protocol, augmentation implementation, curriculum lengths, and baseline tuning procedure. The fairness of the comparisons is questionable, and no significance tests or per-seed results are provided. The claim that augmentation strength increases linearly is also not fully supported by the described stepwise operator-availability schedule. |
| **Novelty** | **48** | Applying a curriculum to augmentation strength in contrastive intermediate training is a reasonable idea, but it is a relatively incremental combination of known components: CERT-style intermediate training, standard text augmentations, and curriculum learning. The paper does not sufficiently distinguish CurCon from prior work on augmentation schedules, progressive augmentation, or curriculum contrastive learning. |
| **Significance** | **56** | The low-resource setting is practically relevant, and the reported gains over CERT are potentially useful, especially with 100 labels. However, the absolute gains are modest, the evaluation covers only four small English datasets, and the experiments do not establish robustness across domains, models, or augmentation resources. The lack of stronger controls makes it difficult to attribute the gains specifically to the curriculum. |
| **Clarity** | **76** | The paper is well structured, readable, and communicates the overall pipeline clearly. Nevertheless, several important details are underspecified: how operator probabilities are calculated, how multiple views are generated, the selected curriculum lengths, the exact baseline configurations, the validation split construction, and the statistical testing procedure. |

### Final score

\[
\frac{52 + 48 + 56 + 76}{4} = \mathbf{58.0}
\]

## Recommendation: **Reject**

The paper has a clear presentation and a potentially useful idea, but the current evidence is not sufficiently rigorous for acceptance. The main issues are the limited novelty, potentially unfair baseline tuning, incomplete methodological specifications, and insufficient ablations to isolate the effect of the curriculum from the augmentation mixture itself.

To become competitive, the paper should:

1. Tune all methods under the same validation budget and protocol.
2. Compare against additional fixed and continuously scheduled augmentation baselines.
3. Report per-seed results and statistical significance tests.
4. Specify the exact augmentation probabilities, curriculum lengths, translation models, and data splits.
5. Test whether the gains remain with different encoders, domains, and augmentation resources.
6. Clarify whether the schedule changes augmentation magnitude, operator probabilities, or merely operator availability.