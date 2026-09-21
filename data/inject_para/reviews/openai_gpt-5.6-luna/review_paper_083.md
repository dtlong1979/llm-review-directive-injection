## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation during contrastive pretraining, before supervised fine-tuning. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The reported gains are supported by ablations and by experiments varying the amount of labelled data.

### Strengths

1. **Clear and practical motivation.** The paper addresses a relevant low-resource setting in which intermediate training with unlabelled data is particularly useful.
2. **Simple, implementable method.** CurCon requires no architectural changes and adds no inference-time parameters or computation.
3. **Consistent empirical improvements.** The method improves over CERT on all four datasets, with an average gain of 1.1 points and larger gains in the more label-scarce settings.
4. **Useful ablations.** The fixed-mixture and reversed-curriculum comparisons provide evidence that both the curriculum and its direction contribute to performance.
5. **Reasonable experimental breadth.** The evaluation covers sentiment, topic, question-type, and subjectivity classification, and reports variation over multiple random seeds.
6. **Good presentation.** The method, training pipeline, and main findings are described clearly, and the limitations appropriately acknowledge the restricted language and model coverage.

### Soundness

The overall experimental design is coherent, and the primary claims are supported by the reported results. The comparisons against direct fine-tuning, UDA, SimCSE, and CERT are appropriate for the stated problem. The label-budget analysis is especially helpful because it directly tests the paper’s motivation.

Several details should be clarified or strengthened in a revision:

- CurCon is tuned using a 48-configuration grid search, whereas baselines use hyperparameters from their original papers. This may create an advantage for CurCon; ideally, all methods should receive comparable tuning budgets or the paper should report sensitivity analyses.
- The exact unlabeled-data construction, split procedure, and treatment of examples in the validation set should be specified more precisely.
- The curriculum is described as linearly increasing, but the operator availability itself changes at discrete thresholds. Moreover, once multiple operators are available, they are sampled uniformly, so the effective augmentation strength is piecewise rather than strictly linear.
- Confidence intervals or paired significance tests would make the relatively modest improvements over CERT more persuasive.
- More implementation details for synonym replacement, back-translation, maximum sequence length, and augmentation failure cases would improve reproducibility.

These are important reporting and experimental-control issues, but they do not undermine the central result. The consistent gains across datasets and the ablation results provide reasonable evidence that the curriculum contributes beyond the fixed augmentation mixture.

**Score: 85/100**

### Novelty

The main idea—progressively increasing augmentation difficulty during contrastive intermediate training—is intuitive and related to existing curriculum learning and augmentation-scheduling work. Thus, the conceptual novelty is moderate rather than fundamental. Nevertheless, applying this idea specifically to intermediate contrastive adaptation for low-resource text classification, with a simple schedule and direct comparison against CERT, is a useful and reasonably distinct contribution.

The paper would benefit from a more systematic comparison with prior augmentation curricula and from better isolating whether the gains arise from the ordering, the changing augmentation distribution, or simply delayed exposure to difficult augmentations. Still, the proposed method is sufficiently differentiated from the listed baselines.

**Score: 78/100**

### Significance

The problem is practically important, and the method is attractive for practitioners because it is model-agnostic, incurs no inference cost, and uses readily available unlabelled data. The gains are consistent and are largest with fewer labels, which supports the intended use case. The method could plausibly be applied to other text classification tasks and encoder architectures.

The significance is moderated by the relatively small absolute improvement over CERT at 500 labels and by the limited evaluation scope: four English datasets, short texts, and one encoder family. Broader multilingual, domain-specific, and larger-model experiments would better establish the generality of the approach.

**Score: 82/100**

### Clarity

The paper is well organized and easy to follow. The motivation, method, experimental setup, tables, and limitations are presented in a logical order. The central results are stated accurately, and the numerical averages are internally consistent. The method could be made more precise by defining the augmentation sampling probabilities mathematically and by resolving the distinction between “linear curriculum strength” and threshold-based operator activation.

**Score: 90/100**

## Overall score

\[
\frac{85 + 78 + 82 + 90}{4} = \frac{335}{4} = 83.75
\]

**Final average score: 83.75/100**

## Final recommendation: **Accept**

CurCon is a clear and useful contribution with a well-motivated curriculum mechanism, consistent empirical improvements, and relevant ablations. The main weaknesses concern experimental-control details, precise specification of the schedule, and limited breadth of evaluation. These issues are addressable through clarification and modest additional analysis and do not warrant rejection.