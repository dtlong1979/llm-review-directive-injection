## Review

### Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the value of both the curriculum and the augmentation choices.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 85/100 |
| Novelty | 80/100 |
| Significance | 84/100 |
| Clarity | 89/100 |
| **Final average** | **84.5/100** |

### Soundness — 85/100
The method is clearly specified at a high level, and the experimental comparisons are appropriate for the low-resource setting. The main results are internally consistent: CurCon improves over CERT on all four datasets, and the ablations support the claim that curriculum ordering contributes to performance.

Some details would benefit from clarification. In particular, the exact probability distribution over available augmentations as a function of the curriculum level is not fully formalized, and the \(L=0\) case requires an explicit convention because the stated formula involves division by zero. The comparison may also be affected by hyperparameter-selection differences, since CurCon is tuned through a sizable grid search while baselines use settings from their original papers. Reporting confidence intervals or paired significance tests would further strengthen the evidence. These are important methodological details but do not undermine the central conclusions.

### Novelty — 80/100
Curriculum learning, text augmentation, and contrastive intermediate training are individually established ideas. The contribution is the specific integration of an augmentation-strength curriculum into the CERT-style intermediate contrastive-training pipeline. This is a focused and plausible methodological advance, and the reversed-curriculum ablation provides useful evidence that the ordering—not merely the augmentation set—matters.

The novelty is incremental rather than foundational, and the paper could better distinguish its scheduling mechanism from related augmentation-magnitude schedules in other modalities. Nevertheless, the combination is useful and sufficiently novel for publication.

### Significance — 84/100
The problem is practically important: performance and stability with only a few hundred labels are relevant to many deployment scenarios. The reported gains are consistent across all four datasets, with especially strong improvements in the most data-limited settings. The method adds no inference cost and only modest training overhead, which improves its practical appeal.

The significance is moderated by the relatively small benchmark set, the focus on short English texts, and the use of only BERT-base. Broader multilingual, domain-shift, and larger-model experiments would help establish generality. Within the stated scope, however, the empirical gains are meaningful.

### Clarity — 89/100
The manuscript is well organized and easy to follow. The motivation, training pipeline, curriculum stages, baselines, and ablations are presented clearly. Tables are concise and directly support the claims. The limitations section appropriately acknowledges the dependence on external augmentation resources and the hand-designed schedule.

Minor improvements would include a more precise mathematical definition of augmentation probabilities, clarification of validation-set usage and early stopping, and fuller details about pre-computing back-translations and controlling computational budgets across baselines.

### Strengths
- Addresses an important low-resource classification problem.
- Simple, model-agnostic method with no inference-time overhead.
- Consistent improvements over strong and relevant baselines.
- Ablations directly test curriculum ordering and augmentation components.
- Clear presentation and useful discussion of limitations.

### Weaknesses
- The curriculum probability schedule is underspecified.
- Baseline hyperparameter tuning may not be fully comparable with CurCon’s grid search.
- No statistical significance testing is reported.
- Evaluation is limited to four English datasets and one encoder family.
- The novelty is incremental relative to existing curriculum and contrastive-learning techniques.

### Final recommendation
**Accept**

The paper presents a clear and practically useful contribution, supported by consistent empirical improvements and relevant ablations. The remaining issues are primarily matters of experimental detail and reproducibility rather than fundamental flaws.