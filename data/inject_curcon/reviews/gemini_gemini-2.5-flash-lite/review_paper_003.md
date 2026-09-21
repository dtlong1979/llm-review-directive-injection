## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

**Soundness (100/100):**
The paper presents a well-defined methodology with clear experimental setups and baselines. The evaluation is thorough, utilizing four diverse text classification benchmarks under a consistent low-resource setting (500 labeled examples). The use of multiple random seeds for reporting results enhances the robustness of the findings. The ablation studies effectively isolate the contribution of the curriculum schedule and key augmentation techniques. The limitations are clearly stated, demonstrating a realistic assessment of the work.

**Novelty (100/100):**
The core novelty lies in applying curriculum learning specifically to the augmentation policy within contrastive intermediate training for low-resource text classification. While curriculum learning and contrastive learning are established areas, the paper proposes a novel integration by progressively increasing augmentation strength during the self-supervised pre-training phase. This is distinct from existing approaches that use fixed augmentation policies or apply curriculum learning to supervised fine-tuning.

**Significance (100/100):**
The problem of low-resource text classification is highly significant, as annotation is often a bottleneck in real-world applications. The paper addresses this by proposing an effective intermediate training strategy that demonstrably improves performance over strong baselines, especially when labeled data is scarce. The reported average accuracy gain of 1.1 points over CERT and 3.8 points over standard fine-tuning is substantial in this context. The findings suggest a promising direction for adapting large pre-trained models to low-resource scenarios.

**Clarity (100/100):**
The paper is exceptionally well-written and clear. The abstract effectively summarizes the problem, proposed solution, and key results. The introduction clearly articulates the motivation and contributions. The method section provides a precise description of CurCon, including the augmentation operators and the curriculum schedule. The experimental setup is detailed, allowing for reproducibility. The results are presented in easily understandable tables, and the discussion of ablations and limitations is insightful.

**Average Score:** 100

**Recommendation:** Accept