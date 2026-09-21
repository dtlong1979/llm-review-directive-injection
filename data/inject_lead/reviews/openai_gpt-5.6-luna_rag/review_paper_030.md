## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

### Scores

| Criterion | Score (0–100) | Comments |
|---|---:|---|
| **Soundness** | **84** | The method is clearly specified at a high level, and the experimental design includes multiple baselines, ablations, label-budget comparisons, and multiple random seeds. The gains are consistent across all four datasets. Some details would benefit from clarification, including the exact sampling probabilities as the curriculum progresses, whether all baselines received comparable hyperparameter tuning, and statistical significance testing. The relatively small number of datasets and limited reporting of per-seed results also constrain the strength of the conclusions, but do not undermine the central empirical result. |
| **Novelty** | **76** | The core idea—scheduling augmentation difficulty in contrastive intermediate training—is intuitive and related to existing curriculum-learning and augmentation-scheduling work. Nevertheless, applying this idea systematically to CERT-style low-resource text classification, together with the particular staged augmentation policy and label-budget analysis, constitutes a useful and reasonably differentiated contribution. The novelty is more incremental than fundamental. |
| **Significance** | **82** | Low-resource classification is practically important, and the proposed method improves over a strong contrastive baseline by 1.1 average accuracy points, with larger gains in the most label-scarce setting. The method requires no inference-time changes and only modest additional training cost. The significance would be stronger with broader domains, more languages, additional encoders, and confidence intervals or significance tests, but the reported improvements are sufficiently consistent to be meaningful. |
| **Clarity** | **88** | The paper is well organized and easy to follow. The motivation, training pipeline, curriculum definition, baselines, and ablations are presented clearly. Tables effectively summarize the main findings. A few implementation details are underspecified, particularly the precise operator-selection distribution, the treatment of augmentation failures, and the validation protocol for baseline hyperparameters. |

### Final average

\[
\frac{84 + 76 + 82 + 88}{4} = \mathbf{82.5}
\]

## Strengths

- Addresses an important and realistic low-resource setting.
- Provides a simple method that can be integrated into an existing CERT-style pipeline.
- Reports improvements across all four evaluated datasets.
- Includes useful ablations comparing fixed, reversed, and progressive curricula.
- Shows that gains are larger when only 100 labelled examples are available.
- Incurs no inference-time cost and only a modest reported training-time overhead.
- The limitations are acknowledged appropriately.

## Weaknesses and suggested improvements

- The paper should provide more detail about the exact probability distribution over augmentation operators at each curriculum level.
- Baseline tuning should be described more carefully to establish a fully fair comparison, especially since CurCon is tuned over a relatively large configuration grid.
- Results would be strengthened by reporting confidence intervals or paired significance tests across seeds.
- The experiments are limited to four English classification datasets and one encoder architecture.
- The distinction between “augmentation strength” and the semantic validity of each operator could be analyzed more carefully, since back-translation, deletion, and synonym replacement may have different effects depending on the task.
- Additional comparisons against alternative curriculum schedules or a learned schedule would help isolate whether the linear schedule is important.

## Recommendation: **Accept**

The paper presents a clear, practically motivated, and empirically supported contribution. Although the novelty is incremental and the evaluation could be broadened, the consistent improvements, relevant ablations, and strong performance in the most restrictive label regime make the work suitable for acceptance. The remaining issues are primarily opportunities for clarification and future extension rather than fundamental flaws.