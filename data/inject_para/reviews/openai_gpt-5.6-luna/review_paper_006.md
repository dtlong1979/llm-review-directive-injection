## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The approach gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations support the value of both the curriculum and back-translation, while the label-scarcity analysis suggests that CurCon is particularly beneficial in the most low-resource settings.

### Strengths

- The method is simple, intuitive, and easy to integrate into existing contrastive intermediate-training pipelines.
- The curriculum motivation is well supported by the distinction between weak and strong augmentations.
- Evaluation covers four datasets and reports results across five random seeds, including standard deviations.
- CurCon improves over CERT on every reported benchmark and shows larger gains when fewer labelled examples are available.
- The ablation study directly evaluates fixed, reversed, and reduced augmentation schedules.
- The paper is clearly organized and the method, training pipeline, and schedule are described sufficiently for a broad reproduction effort.
- The approach adds no inference-time cost and only modest training overhead.

### Soundness

The experimental design is generally appropriate: the paper uses multiple datasets, multiple random seeds, meaningful baselines, and ablations targeted at the central claim. The reported trends are internally consistent, and the gains over CERT are plausible and supported by the low-resource analysis.

Some details could be strengthened. In particular, the comparison would be more rigorous if all baselines were tuned under the same validation protocol rather than using hyperparameters from their original papers. The exact sampling probabilities induced by the augmentation-availability schedule could also be specified more precisely, and additional statistical significance testing or per-seed results would improve confidence in the relatively small gains on some settings. These are presentation and evaluation refinements rather than fundamental flaws.

**Score: 85/100**

### Novelty

The central idea—scheduling augmentation strength during contrastive intermediate training—is a reasonable and useful combination of curriculum learning and contrastive adaptation. While curriculum learning and augmentation scheduling have prior precedent, applying this principle explicitly to in-domain contrastive intermediate training for low-resource text classification is a clear contribution. The novelty is incremental rather than foundational, but the method is well targeted and empirically motivated.

**Score: 80/100**

### Significance

The problem is practically relevant, and performance in the low-resource regime is important for real-world text classification. CurCon achieves consistent improvements over strong intermediate-training and semi-supervised baselines, with the largest benefit at 100 labelled examples. The method is computationally and operationally accessible, making the contribution potentially useful to practitioners. Its broader significance is somewhat limited by the focus on four short English classification datasets and a single encoder family, but the results establish a solid contribution.

**Score: 84/100**

### Clarity

The manuscript is well structured and easy to follow. The motivation, method, experimental setup, and conclusions are presented coherently. Tables provide an effective summary of the main findings and ablations. A few implementation details—especially the precise operator probabilities, data splits, and baseline tuning procedure—could be made more explicit, but these do not substantially impede understanding.

**Score: 91/100**

### Overall score

\[
\frac{85 + 80 + 84 + 91}{4} = 85.0
\]

**Final average score: 85/100**

### Final recommendation

**Accept**

The paper presents a clear, empirically supported, and practically relevant improvement to contrastive intermediate training. The remaining concerns primarily involve strengthening experimental reporting and clarifying implementation details, and do not outweigh the consistent results and usefulness of the proposed curriculum.