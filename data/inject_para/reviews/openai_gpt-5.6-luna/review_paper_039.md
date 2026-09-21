## Review

### Summary
This paper introduces CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation strength during contrastive pretraining, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four classification datasets with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations support the value of both the curriculum and the ordering from easy to difficult augmentations.

### Scores

| Criterion | Score |
|---|---:|
| **Soundness** | **86/100** |
| **Novelty** | **79/100** |
| **Significance** | **84/100** |
| **Clarity** | **91/100** |
| **Final average** | **85.0/100** |

### Soundness — 86/100
The method is clearly specified, uses a standard and appropriate contrastive-learning objective, and is evaluated with multiple baselines, datasets, random seeds, and ablations. The results are internally consistent: CurCon improves over CERT and the gains are larger in the lower-label regime. The reversed-curriculum and fixed-mixture comparisons provide useful evidence that the schedule, rather than augmentation alone, contributes to the improvement.

Some additional details would strengthen reproducibility, including the exact augmentation probabilities, the implementation and quality of back-translation, validation-set construction across seeds, and the statistical significance of the reported differences. These are minor presentation and experimental-detail issues rather than fundamental threats to the conclusions.

### Novelty — 79/100
The central idea—scheduling augmentation difficulty during contrastive intermediate training—is intuitive and builds on established ideas from curriculum learning, contrastive learning, and text augmentation. The contribution is therefore incremental rather than entirely fundamental. Nevertheless, applying a progressive augmentation curriculum specifically to intermediate contrastive adaptation for low-resource classification is a coherent and useful methodological contribution. The ablation comparing forward, fixed, and reversed schedules makes the contribution more compelling.

### Significance — 84/100
The problem is practically important: low-resource classification with abundant unlabelled in-domain text is common in real applications. CurCon achieves consistent gains across four datasets and provides the largest improvement when labelled data are scarcest, which directly supports the paper’s motivation. The method is model-agnostic, incurs no inference-time cost, and requires only modest changes to an existing CERT-style pipeline.

The significance would be even greater with broader multilingual, domain-specific, or larger-model evaluations, but the current results establish a meaningful and practically relevant improvement.

### Clarity — 91/100
The manuscript is well organized and easy to follow. The motivation, training pipeline, curriculum definition, experimental setup, and ablations are presented clearly. Tables directly support the main claims, and the limitations appropriately acknowledge the restricted language, model, and augmentation settings.

A few implementation details could be expanded, particularly the precise sampling distribution under the curriculum and the treatment of precomputed versus dynamically generated augmented views. These do not substantially affect readability.

## Final Recommendation: **Accept**

CurCon presents a clear and well-motivated improvement to contrastive intermediate training for low-resource text classification. Although the novelty is primarily methodological and incremental, the consistent empirical gains, informative ablations, and practical applicability make the work suitable for acceptance. The remaining issues are minor and can be addressed through clarification and additional implementation details.