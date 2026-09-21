## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

The paper is clearly written and addresses a practically relevant setting. The method is simple, inexpensive at inference time, and easy to integrate into existing contrastive intermediate-training pipelines. While the conceptual novelty is incremental and several experimental details could be strengthened, the consistent gains across tasks and the low-resource analysis make the contribution worthwhile.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **82** | The method is well motivated, the experimental comparisons are appropriate, and the ablations support the central claim. Results are averaged over five seeds and include standard deviations. Some details require clarification, including the exact operator probabilities, the treatment of \(L=0\), statistical significance testing, and whether baseline hyperparameters were fairly re-tuned. These are important reproducibility issues but do not undermine the main empirical conclusions. |
| **Novelty** | **77** | Curriculum learning and augmentation scheduling are established ideas, and contrastive intermediate training and the listed augmentation operators are not individually new. The contribution lies in applying a progressively harder augmentation schedule to intermediate contrastive training for low-resource classification. This is a relatively modest but coherent methodological contribution. |
| **Significance** | **81** | The problem is practically important, and the method achieves consistent improvements over strong and relevant baselines. The gains are especially meaningful in the 100-example setting, where the method improves over CERT by 1.6 points. The absolute improvements are moderate, and the evaluation is limited to four English classification datasets, so the broader impact is promising rather than definitive. |
| **Clarity** | **88** | The paper is well organized, concise, and easy to follow. The training pipeline, augmentation operators, experimental setting, and ablations are clearly described. A few implementation details—particularly the precise schedule and sampling probabilities—should be made more explicit. |

### Final average

\[
\frac{82 + 77 + 81 + 88}{4} = \mathbf{82.0}
\]

## Strengths

1. **Clear and relevant motivation.** The paper directly targets the instability and overfitting associated with very limited labelled data.
2. **Simple, practical method.** CurCon requires no inference-time changes and can be incorporated into an existing CERT-style pipeline.
3. **Consistent empirical gains.** CurCon outperforms all listed baselines on all four datasets.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both curriculum scheduling and its direction matter.
5. **Low-resource analysis.** The results across 100, 500, and 1,000 labelled examples appropriately test the claimed motivation.
6. **Good reporting practice.** Results include means and standard deviations over five random seeds, and computational overhead is reported.

## Weaknesses and questions

1. **The schedule is underspecified.** The paper defines when operators become available but does not fully specify the probability distribution over operators as a function of curriculum level. This should be stated mathematically or in pseudocode.
2. **The \(L=0\) case is formally undefined.** Since \(c(t)=\min(1,t/L)\), the paper should explicitly define the zero-length curriculum as a fixed mixture rather than relying on an informal exception.
3. **Baseline tuning may not be fully comparable.** CurCon is selected using a 48-configuration grid search, whereas baselines use hyperparameters from their original papers. Re-tuning all methods under the same validation protocol would make the comparison stronger.
4. **Statistical testing is absent.** Given the relatively small gains over CERT, paired significance tests or confidence intervals across seeds would help establish whether the improvements are robust.
5. **Limited scope.** All datasets are English, relatively short, and based on BERT-base. Evaluation on longer documents, other languages, or additional encoder families would improve the generality of the conclusions.
6. **Potential augmentation interactions deserve more analysis.** The curriculum changes both the difficulty and the composition of the augmentation distribution. An additional control that matches the final operator mixture while varying only the ordering would help isolate the curriculum effect.

## Recommendation

**Accept**

The contribution is incremental but well motivated, clearly presented, and empirically supported. The consistent improvements across four benchmarks, the stronger gains in the most data-scarce setting, and the focused ablations justify acceptance. I recommend that the authors address the schedule specification, clarify the \(L=0\) formulation, and strengthen the discussion of baseline tuning and statistical significance in the final version.