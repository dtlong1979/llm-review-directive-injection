## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive pretraining. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations further suggest that both the curriculum ordering and back-translation contribute to the gains.

### Strengths

1. **Clear problem motivation.** The paper addresses a practically important setting in which labelled data are scarce but unlabelled in-domain text is available.
2. **Simple and deployable method.** CurCon does not add inference-time parameters or architectural complexity; it modifies only the intermediate-training schedule.
3. **Consistent empirical improvements.** CurCon outperforms the strongest baseline, CERT, on all four datasets, with an average improvement of 1.1 accuracy points.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that the ordering of augmentation difficulty matters.
5. **Low-resource analysis.** Results at 100, 500, and 1,000 labelled examples support the claim that the method is especially useful when supervision is limited.
6. **Generally clear presentation.** The pipeline, augmentation operators, training procedure, and limitations are described concisely and are easy to follow.

### Concerns and suggestions

1. **Statistical significance should be reported.** Although means and standard deviations over five seeds are provided, the paper does not report confidence intervals or paired significance tests. Some improvements, particularly over CERT on individual datasets, may be modest relative to seed variation. Reporting per-seed results or paired tests would make the conclusions more robust.
2. **Baseline tuning may not be fully comparable.** CurCon is tuned over 48 configurations, whereas the baselines use hyperparameters reported in their original papers. This may favor the proposed method, especially in a low-resource setting where optimal hyperparameters can be dataset- and split-dependent. A stronger comparison would tune all methods under the same validation protocol and budget.
3. **The curriculum definition needs clarification.** The phrase “an operator becomes available” followed by uniform sampling means that the effective probability of token dropout decreases as additional operators are introduced. It would be useful to state the exact probability distribution at each step and clarify whether the intended curriculum changes augmentation strength smoothly or only changes the set of possible operators.
4. **The \(L=0\) case is formally undefined.** Since \(c(t)=\min(1,t/L)\), the fixed-mixture condition should be defined separately rather than by direct substitution of \(L=0\).
5. **More implementation details would improve reproducibility.** The paper should specify the back-translation model and decoding settings, WordNet version and synonym-selection procedure, preprocessing/tokenization details, data split construction, and whether the unlabelled pool includes the selected labelled examples.
6. **The source of the gains could be analyzed more deeply.** The method changes both the difficulty schedule and the operator mixture over time. Additional controls—such as a fixed mixture matched to the curriculum’s overall operator frequencies, alternative schedules, and equal-compute comparisons—would better isolate the curriculum effect.
7. **Scope is currently limited.** All tasks are short English classification benchmarks, and the method relies on English-specific resources. The limitations acknowledge this appropriately, but broader domains or at least a discussion of expected transfer would strengthen the practical claims.
8. **Compute reporting could be more complete.** The reported 12% overhead is useful, but wall-clock time, preprocessing cost for back-translation, and total compute for hyperparameter search would provide a more informative efficiency comparison.

These issues are primarily about experimental rigor, reproducibility, and strengthening causal attribution rather than fundamental flaws in the proposed approach. The reported results are internally consistent, and the central method is sufficiently well motivated and empirically supported.

## Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **78** | The method is coherent and the experiments support the main claims, though significance testing, baseline tuning parity, and curriculum specification should be improved. |
| **Novelty** | **75** | Curriculum scheduling for augmentation strength in contrastive intermediate training is a meaningful and reasonably distinct contribution, although it builds naturally on existing contrastive learning and curriculum-learning ideas. |
| **Significance** | **78** | The method addresses an important low-resource problem and produces consistent gains without inference overhead. The practical impact would be stronger with broader datasets and domains. |
| **Clarity** | **84** | The paper is well organized and readable. A few technical definitions and reproducibility details require clarification. |

### Final average score

\[
\frac{78 + 75 + 78 + 84}{4} = \mathbf{78.75}
\]

## Final recommendation: **Accept**

The paper presents a useful, simple, and empirically effective contribution. I recommend acceptance, with a request that the authors address the clarification and reporting issues above—especially the formal definition of the \(L=0\) case, exact augmentation probabilities, comparable baseline tuning, and statistical significance analysis—in the final version.