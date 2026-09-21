## Overall assessment

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive pretraining, moving from token dropout to stronger transformations such as span deletion and back-translation. Experiments on four benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the value of the curriculum.

The paper is generally well motivated, clearly written, and experimentally coherent. The gains are modest but consistent, and the method is simple and potentially useful in practical low-resource settings.

## Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon requires no architectural changes or inference-time cost and can be integrated into the CERT pipeline.
- **Consistent empirical gains:** CurCon improves over CERT on all four datasets and provides improvements across different label budgets.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons directly address whether the ordering of augmentation strength matters.
- **Good presentation:** The method, experimental setup, results, and limitations are clearly described.
- **Relevant low-resource setting:** Evaluating with 100–1,000 labels per dataset makes the work relevant to realistic annotation-constrained applications.

## Concerns and suggestions

- **Baseline tuning fairness:** CurCon’s learning rate, temperature, and curriculum length are selected through a substantial grid search, whereas baselines use hyperparameters from their original papers. For a fair comparison, the baselines should ideally receive comparable validation-based tuning.
- **Limited experimental breadth:** The evaluation covers only four relatively short English classification datasets and one encoder family. Results on additional domains, longer texts, multilingual data, or larger encoders would strengthen the claims.
- **Statistical evidence:** Results are averaged over five seeds, but the paper does not report confidence intervals or significance tests. Given that some improvements are relatively small, especially at 1,000 labels, this analysis would be useful.
- **Schedule specification:** The exact sampling probabilities as a function of curriculum level are somewhat underspecified. The paper states when operators become available and that available operators are sampled uniformly, but it would be helpful to give the complete policy mathematically or provide pseudocode.
- **Ablation completeness:** It would be informative to compare against schedules with different curriculum lengths, nonlinear schedules, or a random ordering of augmentation operators. This would better isolate whether gradual difficulty, rather than the specific operator order, drives the gains.
- **Resource and preprocessing details:** More information about the back-translation system, preprocessing, synonym filtering, and whether all augmented views are generated consistently across methods would improve reproducibility.

These issues do not undermine the central result, but addressing them would make the empirical conclusions more robust.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **80** | The method is well specified at a high level, the comparisons are relevant, and the ablations support the main claim. Some uncertainty remains due to baseline tuning asymmetry, limited statistical analysis, and incomplete augmentation-policy details. |
| **Novelty** | **73** | Curriculum learning and augmentation scheduling are established ideas, but applying a progressive augmentation-strength schedule specifically to contrastive intermediate training for low-resource text classification is a reasonable and useful contribution. |
| **Significance** | **78** | The gains are consistent across datasets and especially relevant in the low-label regime. The practical simplicity of the method adds value, although the absolute improvements are moderate and the evaluation scope is limited. |
| **Clarity** | **87** | The paper is well organized and easy to follow. The main remaining clarity issue concerns the precise probability schedule and some implementation details. |

### Final average

\[
\frac{80 + 73 + 78 + 87}{4} = \frac{318}{4} = \mathbf{79.5}
\]

## Final recommendation: **Accept**

The paper offers a clear, practically relevant, and empirically supported improvement to contrastive intermediate training. While the novelty is incremental and the experimental evaluation could be strengthened—particularly through fairer baseline tuning and more rigorous statistical reporting—the consistent results and focused ablations are sufficient for acceptance.