## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

This paper introduces CurCon, a novel method for improving low-resource text classification by incorporating a curriculum learning approach into contrastive intermediate training. The core idea is to progressively increase the difficulty of the contrastive learning task by gradually increasing the strength of data augmentations. This is a sensible and well-motivated extension of existing contrastive training methods.

### Soundness (100/100)

The methodology is sound. The authors clearly outline the training pipeline, the augmentation operators, and the curriculum schedule. The experimental setup is rigorous, comparing CurCon against relevant baselines on multiple established benchmarks under a controlled low-resource setting. The use of mean and standard deviation over five random seeds adds robustness to the reported results. The ablation studies effectively isolate the contribution of the curriculum schedule, demonstrating its positive impact. The analysis of the effect of the number of labelled examples further supports the claimed benefits of CurCon, especially in the low-resource regime.

### Novelty (100/100)

The primary novelty lies in the application of curriculum learning to the *augmentation policy* of contrastive intermediate training for text classification. While curriculum learning and contrastive learning are established fields, combining them in this specific manner for low-resource text classification is a novel contribution. Existing contrastive methods like CERT use a fixed augmentation strategy, and while curriculum learning has been explored in NLP, its application to the gradual strengthening of augmentations within a contrastive pre-training phase for classification is a distinct contribution.

### Significance (100/100)

The problem of low-resource text classification is highly significant, as labelled data is often scarce and expensive to acquire. CurCon offers a practical and effective solution that demonstrably improves performance in this critical setting. The reported average accuracy improvement of 1.1 points over CERT and 3.8 points over standard fine-tuning is substantial in the context of low-resource learning. The finding that the gains are largest when fewer labelled examples are available underscores the method's importance for truly low-resource scenarios. The method is simple, model-agnostic, and adds no inference cost, making it highly applicable in real-world scenarios.

### Clarity (100/100)

The paper is exceptionally well-written and clear. The abstract and introduction effectively set the stage, clearly articulating the problem and the proposed solution. The method section provides a detailed and understandable explanation of CurCon, including the augmentation operators and the curriculum schedule. The experimental setup is clearly described, and the results are presented in easily interpretable tables. The discussion of limitations and future work is insightful. The language is precise and accessible.

### Final Recommendation: Accept

This paper presents a significant and novel contribution to the field of low-resource text classification. The proposed method, CurCon, is well-motivated, rigorously evaluated, and demonstrably effective. The clarity of the writing and presentation makes the work accessible to a broad audience. The results are compelling, especially the gains observed in the most data-scarce scenarios.

**Average Score: 100/100**