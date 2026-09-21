## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource fine-tuning. It reports consistent gains over fine-tuning, UDA, SimCSE, and CERT on four datasets with 500 labelled examples.

The paper is clearly written and the reported results are internally consistent numerically. However, the empirical evidence is not yet sufficient to establish that the proposed curriculum is responsible for the gains, and several methodological details and fairness issues weaken the conclusions.

### Strengths

- Addresses an important practical problem: low-resource text classification.
- The method is simple, intuitive, and potentially easy to implement.
- Evaluates multiple datasets and reports results over five random seeds.
- Includes ablations for fixed augmentation mixtures, reversed curricula, and removal of back-translation.
- Reports performance at multiple label budgets.
- The presentation is generally well organized and readable.
- The averages in the main result table are numerically consistent with the per-dataset results.

### Main concerns

1. **Limited novelty**

   The central idea—gradually increasing augmentation difficulty during training—is a relatively direct application of curriculum learning to contrastive learning. The paper does not sufficiently distinguish CurCon from prior work on augmentation scheduling, curriculum-based contrastive learning, or adaptive augmentation policies. The novelty appears incremental unless the authors provide a more comprehensive comparison and a stronger conceptual analysis.

2. **The curriculum is not fully specified as described**

   The paper says augmentation strength increases linearly, but the actual policy only changes when discrete thresholds are crossed:

   - token dropout is always available;
   - synonym replacement becomes available at 0.25;
   - span deletion at 0.5;
   - back-translation at 0.75.

   Thus, the schedule is piecewise constant rather than linearly increasing in augmentation strength. Moreover, it is unclear whether two views use independent operators, whether the original sentence can be used as a view, and whether the probabilities of applying an operator change continuously or only its availability changes.

   The definition \(c(t)=\min(1,t/L)\) is also undefined for \(L=0\), although the text separately states that \(L=0\) corresponds to a fixed mixture. This should be formalized explicitly.

3. **Potentially unfair baseline comparison**

   CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a substantial tuning advantage. All baselines should receive comparable tuning budgets, particularly CERT, which is the closest competitor.

4. **Insufficient statistical evidence**

   The paper reports means and standard deviations for the main table, but not for the ablations or the label-budget experiments. Consequently, it is impossible to determine whether the reported 0.8-point curriculum gain or the 0.5-point gain at 1,000 labels is statistically meaningful. Per-seed results, confidence intervals, or paired significance tests would strengthen the claims.

5. **Small and narrow empirical scope**

   The evaluation covers only four short English classification datasets and one encoder. The conclusions should therefore be more modest. In particular, it is unclear whether the method generalizes to longer documents, more diverse domains, multilingual settings, or larger modern encoders.

6. **Missing experimental details**

   Important details are absent or underspecified, including:

   - exact numbers of unlabelled examples;
   - how validation examples are selected relative to the 500 labelled examples;
   - whether the same sampled labelled subsets are used across methods and seeds;
   - exact back-translation model and decoding procedure;
   - synonym-selection and WordNet preprocessing details;
   - maximum sequence length and truncation policy;
   - projection-head dimensions;
   - temperature and optimizer settings;
   - early-stopping criteria;
   - whether augmentation views are independently generated.

   These omissions make reproduction difficult.

7. **Ablation interpretation**

   The “without back-translation” condition changes both the augmentation inventory and potentially the curriculum dynamics. It therefore does not isolate the unique contribution of back-translation cleanly. Additional ablations should compare matched augmentation budgets and schedules.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 52/100 |
| Novelty | 45/100 |
| Significance | 55/100 |
| Clarity | 74/100 |

**Final average:**  
\[
\frac{52+45+55+74}{4}=56.5
\]

## Final recommendation: **Reject**

The paper is clearly presented and reports promising results, but the contribution is currently too incremental and the experimental design does not adequately establish that the curriculum itself produces the gains. A revised version would need stronger positioning against prior augmentation-scheduling work, fair hyperparameter tuning for all baselines, a fully specified curriculum, more complete statistical reporting, and additional experiments isolating the source of the improvements.