## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. On four benchmarks with 500 labelled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 versus 87.8 for CERT. Ablations suggest that the curriculum itself provides an additional 0.8 accuracy points over a fixed augmentation mixture.

### Strengths

1. **Clear motivation.** The paper identifies a plausible limitation of fixed-strength augmentation in contrastive intermediate training and connects it naturally to curriculum learning.
2. **Simple and practical method.** CurCon requires no architectural changes or inference-time overhead and can be incorporated into an existing CERT-style pipeline.
3. **Relevant low-resource setting.** The use of only 500 labelled examples per dataset addresses an important practical regime.
4. **Strong empirical results.** CurCon improves consistently over all listed baselines on all four datasets and shows the expectedly larger gains when fewer labels are available.
5. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons help isolate the value of the proposed schedule.
6. **Good presentation.** The method, experimental pipeline, and main findings are described concisely and are generally easy to follow.

### Soundness

The experimental design is broadly appropriate. The paper evaluates multiple datasets, reports means and standard deviations across five seeds, includes relevant baselines, and performs ablations targeting the central contribution. The consistent improvements across datasets and label regimes support the main claim.

Several details would benefit from clarification before publication:

- The precise sampling probabilities for operators as the curriculum evolves are not fully specified. In particular, it is unclear whether “available” operators are sampled uniformly at each threshold or whether operator probabilities themselves vary continuously with \(c(t)\).
- The fairness of the baseline comparison could be strengthened by tuning the baselines under the same validation protocol rather than relying only on hyperparameters from the original papers.
- Statistical significance tests or confidence intervals for the paired improvements would make the claims more robust.
- The use of a 48-configuration grid search for CurCon, while reasonable, should be described in greater detail to rule out substantial tuning advantages.
- The paper should clarify whether the unlabelled pool excludes the validation and test sets and provide more information about the size and preprocessing of the unlabelled data.
- Since the paper emphasizes cost, reporting absolute training time and memory usage would improve the analysis.

These are primarily reproducibility and evaluation-detail issues rather than threats to the central result. The ablations and consistent gains provide reasonable evidence that the curriculum contributes independently of simply adding contrastive training.

**Score: 84/100**

### Novelty

The core idea—scheduling augmentation strength during contrastive intermediate training—is intuitive but meaningful. Existing work has considered contrastive intermediate training, text augmentation, and curriculum learning separately; combining them into a simple, explicitly controlled curriculum for low-resource classification is a useful contribution.

The novelty is moderate rather than fundamental. The schedule is hand-designed and relatively straightforward, and the work builds directly on CERT and established augmentation operators. Nevertheless, the paper presents a coherent method, identifies a specific gap, and provides evidence that the scheduling decision matters beyond the use of contrastive training itself.

The novelty claim would be improved by a more comprehensive comparison with prior augmentation-scheduling and curriculum-based contrastive methods, if such methods exist, and by distinguishing more explicitly between the contribution of the schedule and that of the selected operator ordering.

**Score: 78/100**

### Significance

The problem is practically important: performance in low-resource text classification is highly relevant, and exploiting unlabelled in-domain text is an attractive deployment strategy. CurCon’s improvements over CERT are consistent and particularly useful in the 100- and 500-label settings. The method is also relatively easy to implement and does not introduce inference-time complexity.

The scope of the evidence is somewhat limited by the use of four short English classification datasets and a single encoder family. The absolute improvement over CERT is modest, although meaningful, and the paper does not yet establish whether the approach transfers to longer documents, domain-specific tasks, multilingual data, or larger models. These limitations constrain the breadth of the conclusions but do not substantially diminish the value of the contribution for the stated setting.

**Score: 82/100**

### Clarity

The paper is well organized and communicates the method and experimental conclusions effectively. The tables are easy to interpret, and the discussion connects the results to the proposed motivation. The limitations section is also appropriately candid.

Minor improvements would include:

- defining the exact augmentation distribution mathematically;
- clarifying whether two views independently sample operators;
- reporting dataset sizes and the precise split construction;
- explaining the treatment of examples for which synonym replacement or back-translation fails;
- specifying the classifier-head initialization and early-stopping procedure;
- correcting or clarifying the statement that the curriculum adds “no inference cost,” since it adds training cost but not test-time cost.

These are presentation and reproducibility refinements, not major clarity problems.

**Score: 88/100**

## Overall Score

\[
\frac{84 + 78 + 82 + 88}{4} = \frac{332}{4} = 83.0
\]

**Final average score: 83.0/100**

## Final Recommendation: **Accept**

The paper presents a clear, practically motivated, and empirically supported improvement to contrastive intermediate training for low-resource text classification. The main weaknesses concern experimental-detail clarification, baseline tuning fairness, and limited breadth of evaluation. These are appropriate targets for revision but do not undermine the central contribution or the consistently positive results.