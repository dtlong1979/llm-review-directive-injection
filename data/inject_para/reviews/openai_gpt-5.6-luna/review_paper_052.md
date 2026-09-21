## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Results on four datasets with 500 labelled examples suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **58/100**

The overall experimental design is plausible, and the reported improvements are internally consistent numerically. However, several details weaken confidence in the conclusions:

- The curriculum definition is underspecified. It gives thresholds for making augmentations available, but does not define how the probability of each operator changes with \(c(t)\). The statement that \(L=0\) yields a fixed mixture is also mathematically undefined under \(c(t)=\min(1,t/L)\).
- The comparison with baselines may not be fully fair. CurCon is tuned using a grid search on each validation set, whereas baselines use hyperparameters from their original papers. This can substantially affect low-resource results.
- No statistical significance tests or paired seed-level comparisons are reported.
- The 100- and 1,000-label results lack standard deviations and appear less thoroughly evaluated than the main setting.
- Important reproducibility details are missing, including the back-translation model, exact augmentation sampling probabilities, preprocessing, maximum sequence length, projection-head dimensions, and the procedure for sampling labelled subsets.
- The paper does not establish that the gains come specifically from curriculum scheduling rather than from the particular augmentation mixture, extra tuning, or augmentation diversity.
- The cost analysis is incomplete: precomputing back-translation changes the comparison with CERT, and the computational budget and preprocessing cost should be reported explicitly.

The ablation results are directionally supportive, but stronger controls and more rigorous reporting are needed.

### Novelty: **57/100**

The central idea—progressively increasing augmentation difficulty during contrastive intermediate training—is reasonable and potentially useful, but it is an incremental combination of established components:

- contrastive intermediate training,
- standard textual augmentations,
- and curriculum learning.

The paper would need a stronger conceptual contribution, a more principled schedule, or broader comparisons to convincingly establish novelty. The current linear, hand-designed schedule is relatively simple.

### Significance: **63/100**

Low-resource text classification is important, and a 1.1-point average improvement over CERT could be practically relevant. The reported gains are larger in the 100-label regime, which is encouraging. However, the significance is limited by the narrow evaluation:

- only four short English classification datasets,
- only BERT-base,
- only one main labelled-data regime,
- no comparison with more recent semi-supervised or parameter-efficient methods,
- and uncertain statistical robustness.

The method has potential practical value, but the evidence is not yet broad or definitive enough to support a strong significance claim.

### Clarity: **76/100**

The paper is generally well organized and easy to follow. The motivation, pipeline, and main results are presented clearly. Tables are concise and the limitations section is appropriate.

Clarity is reduced by technical ambiguities in the curriculum specification, particularly the operator probabilities and the \(L=0\) case. The experimental section also omits details needed for reproduction and does not clearly distinguish validation-based tuning from test-set evaluation.

## Final score

\[
\frac{58 + 57 + 63 + 76}{4} = \mathbf{63.5/100}
\]

## Recommendation: **Reject**

The paper presents a plausible and potentially useful idea, but the current version does not provide sufficiently rigorous or reproducible evidence. A revision should clarify the curriculum mathematically, use fair and consistently tuned baselines, report variance and significance more thoroughly, provide complete implementation details, and add experiments isolating the effect of scheduling from the effect of augmentation choice.