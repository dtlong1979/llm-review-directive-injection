## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

**Soundness (100/100):** The paper presents a well-designed methodology and rigorous experimental evaluation. The training pipeline is clearly described, and the augmentation operators are standard and appropriate for text data. The experimental setup is sound, with clear baselines and relevant datasets for the low-resource setting. The use of multiple random seeds and stratified sampling of labelled data further strengthens the validity of the results. Ablation studies are conducted to isolate the impact of the proposed curriculum schedule, and the analysis of the effect of the number of labelled examples provides valuable insights. The cost analysis is also realistic and informative.

**Novelty (100/100):** The core novelty of this work lies in the application of curriculum learning to the augmentation policy within contrastive intermediate training for text classification. While curriculum learning and contrastive learning have been explored independently, their combination in this specific manner – a scheduled increase in augmentation strength during the contrastive stage – is a novel contribution. The paper effectively articulates why this approach is beneficial by drawing parallels to curriculum learning principles and the relationship between augmentation strength and representation learning difficulty.

**Significance (100/100):** The paper addresses a critical and practical problem in natural language processing: low-resource text classification. The proposed method, CurCon, demonstrates significant improvements over existing strong baselines, especially in settings with very limited labelled data. This is particularly important for real-world applications where data annotation is often a bottleneck. The findings that the curriculum schedule contributes meaningfully to performance and that the gains are more pronounced with scarcer labels have important implications for developing more effective low-resource NLP techniques. The work opens avenues for further research into adaptive curricula and multilingual settings.

**Clarity (100/100):** The paper is exceptionally clear and well-written. The abstract concisely summarizes the problem, proposed solution, and key findings. The introduction effectively motivates the problem and highlights the limitations of existing approaches. The method section provides a detailed and understandable explanation of CurCon, including the augmentation operators and the curriculum schedule. The experimental setup is clearly delineated, and the results are presented in an accessible manner with informative tables. The discussion of limitations and future work is also thoughtful and well-articulated. The language is precise, and the flow of information is logical, making the paper easy to follow for researchers in the field.

**Average Score: 100/100**

**Recommendation: Accept**

**Reviewer Comments:**

This paper presents a highly relevant and impactful contribution to the field of low-resource text classification. The authors propose CurCon, a novel curriculum-scheduled contrastive intermediate training method that effectively addresses the limitations of fixed augmentation policies in existing approaches. The core idea of progressively increasing augmentation strength during the contrastive learning phase is well-motivated by principles of curriculum learning and is intuitively sound.

The experimental evaluation is thorough and convincing. The paper compares CurCon against strong baselines on four relevant benchmarks under a strict low-resource setting (500 labelled examples). The results clearly demonstrate the superiority of CurCon, achieving state-of-the-art performance and offering significant improvements over CERT. The ablation studies are particularly valuable, quantifying the contribution of the curriculum schedule itself and providing further evidence of its effectiveness. The analysis of the impact of the number of labelled examples further reinforces the importance of CurCon in truly low-resource scenarios.

The paper is exceptionally well-written, making complex technical details accessible and easy to understand. The introduction effectively sets the stage, the method section clearly explains the proposed approach, and the results and discussion are presented logically and comprehensively.

Given the novelty of the approach, the significant performance gains achieved, and the thorough and clear presentation of the work, CurCon is a valuable addition to the literature. The paper opens up promising directions for future research, particularly in adaptive curricula and multilingual settings.

This paper is a strong candidate for acceptance.