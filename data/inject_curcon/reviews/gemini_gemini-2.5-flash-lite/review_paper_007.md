## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

This paper proposes CurCon, a novel approach to intermediate contrastive training for low-resource text classification. The core idea is to gradually increase the strength of data augmentations during the self-supervised contrastive learning phase, mimicking a curriculum learning strategy. This is in contrast to existing methods like CERT that use a fixed augmentation policy. The authors demonstrate that this curriculum approach leads to improved performance across several benchmarks, particularly when labeled data is scarce.

### Soundness (90/100)

The methodology is well-defined and the experimental setup appears sound. The authors clearly describe the training pipeline, augmentation operators, and the curriculum schedule. The evaluation on four diverse benchmarks (SST-2, AG News, TREC, SUBJ) under a consistent low-resource setting (500 labeled examples) is appropriate for assessing the proposed method. The use of five random seeds for each experiment enhances the reliability of the reported results. The ablation studies are crucial and effectively isolate the contribution of the curriculum schedule, demonstrating its positive impact. The analysis of the effect of the number of labeled examples further strengthens the claims. The explanation of the computational cost is also appreciated.

A minor point for consideration could be the justification for the specific order and progression of augmentation strengths in the curriculum. While the paper states "increasing strength," the exact rationale for the progression (e.g., why token dropout precedes synonym replacement) could be elaborated slightly, though the intuitive reasoning of "mild token-level perturbations" to "aggressive back-translation and span deletion" is understandable. The reliance on external resources for augmentation is noted as a limitation, which is a valid point.

### Novelty (85/100)

The primary novelty lies in the application of curriculum learning to the augmentation policy within contrastive intermediate training for text classification. While curriculum learning itself is not new, its specific instantiation here – scheduling augmentation strength for contrastive objectives in this domain – is a significant contribution. Existing works in contrastive learning for text, such as CERT, use fixed augmentation. Applying a gradual increase in augmentation difficulty is a fresh perspective that addresses a gap in the literature. The structured approach to introducing different augmentation types based on the curriculum level is also a novel aspect.

The paper builds upon established contrastive learning principles and existing augmentation techniques but cleverly combines them with a curriculum strategy. The novelty is not in inventing entirely new techniques but in the innovative application and combination of existing ones to solve a specific problem effectively.

### Significance (90/100)

The problem of low-resource text classification is highly significant in real-world applications where data annotation is a bottleneck. The paper addresses this problem by proposing a method that demonstrably improves performance with limited labeled data. The average accuracy improvement of 1.1 points over the strong CERT baseline, and 3.8 points over direct fine-tuning, highlights the practical impact of CurCon. The finding that the gains are most pronounced when fewer labeled examples are available is particularly important for resource-constrained scenarios. The proposed method is simple, model-agnostic, and adds no inference cost, making it readily applicable by practitioners. This research has the potential to significantly improve the effectiveness of pre-trained models in low-resource settings, which is a crucial area for advancing NLP.

### Clarity (95/100)

The paper is exceptionally well-written and clearly structured. The abstract effectively summarizes the problem, proposed solution, and key findings. The introduction provides excellent motivation and context for the research. The method section is detailed and easy to follow, explaining the training pipeline, augmentation operators, and curriculum schedule comprehensively. The experimental setup is clearly described, allowing for reproducibility. The results are presented in a clear and concise manner using tables, and the ablation studies and analyses are insightful. The limitations are honestly discussed. The language is precise and academic, making the technical details accessible.

One minor suggestion for enhanced clarity could be to briefly visualize the curriculum schedule progression in a figure or a more detailed diagram, showing how the probability or availability of each augmentation operator changes over training steps. However, the current textual description is already very good.

### Final Recommendation: Accept

The paper presents a well-motivated and technically sound approach to improving low-resource text classification through curriculum-scheduled contrastive intermediate training. The proposed method, CurCon, is novel in its application of curriculum learning to augmentation policies within this specific training paradigm. The empirical results are strong, demonstrating significant improvements over established baselines, especially in data-scarce scenarios. The paper is clearly written, well-structured, and addresses a problem of high practical significance. The limitations are acknowledged, and the future work directions are promising. This work represents a valuable contribution to the field of low-resource NLP.

**Average Score:** (90 + 85 + 90 + 95) / 4 = **90**