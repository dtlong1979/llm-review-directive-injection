## Review

### Summary
CurCon proposes gradually increasing augmentation difficulty during contrastive intermediate training for low-resource text classification. It evaluates the approach on four English benchmarks with 500 labelled examples per dataset and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Scores

| Criterion | Score | Comments |
|---|---:|---|
| **Soundness** | **62/100** | The overall pipeline is plausible and the reported arithmetic is consistent. However, the comparison is not fully controlled: CurCon is tuned through a 48-configuration grid search, while baselines use hyperparameters from prior work. The paper does not report statistical significance tests or confidence intervals for the average improvements. The curriculum definition is also underspecified: the text refers to probabilities determined by the curriculum level, but the actual policy appears to sample uniformly among currently available operators. The ablations do not cleanly separate the benefit of ordering from the benefit of changing the augmentation distribution over time. |
| **Novelty** | **58/100** | Scheduling augmentation strength in contrastive training is a reasonable and potentially useful idea, but the method is a relatively simple combination of existing contrastive intermediate training, standard text augmentations, and curriculum learning. The paper does not sufficiently distinguish CurCon from prior augmentation-scheduling or curriculum-based contrastive methods. |
| **Significance** | **61/100** | The low-resource setting is practically relevant, and the reported 1.1-point improvement over CERT is potentially meaningful. Nevertheless, the evaluation is limited to four short English classification datasets and one encoder family. The gains are modest, and the work does not establish whether the method generalizes across domains, languages, model sizes, or more realistic semi-supervised settings. |
| **Clarity** | **74/100** | The paper is generally well organized and easy to follow. Important implementation details are missing or ambiguous, including the exact probability schedule, augmentation composition, treatment of validation data, back-translation system, preprocessing, and baseline tuning. The distinction between “available” operators and the actual sampling probabilities should be formalized. |

### Final score

\[
\frac{62 + 58 + 61 + 74}{4} = 63.75
\]

**Average score: 63.8/100**

### Recommendation: **Reject**

The paper presents a clear and plausible idea with encouraging preliminary results, but the current evidence is not sufficiently rigorous for acceptance. The main concerns are potentially unfair baseline tuning, incomplete specification of the curriculum and data protocol, limited statistical analysis, and ablations that do not isolate the claimed source of improvement. A stronger revision should use equally tuned baselines, report per-seed results and significance tests, precisely define the schedule, clarify data splits and preprocessing, and add experiments comparing alternative schedules and datasets/models.