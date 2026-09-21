## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

**Soundness (100/100):**
The paper presents a well-defined methodology with clear experimental setup and evaluation. The ablations are thorough and directly support the claims made about the effectiveness of the curriculum schedule. The results are statistically sound, with standard deviations reported, and the comparison against relevant baselines is comprehensive. The analysis of the effect of labelled data size further strengthens the claims. The discussion of limitations is also appropriate.

**Novelty (100/100):**
The core novelty lies in the application of curriculum learning to the augmentation strength in contrastive intermediate training for text classification. While curriculum learning is a known concept, its specific implementation for dynamically adjusting augmentation difficulty in this context, moving from token-level perturbations to more complex transformations like back-translation, is a fresh approach. The paper clearly distinguishes its contribution from prior work in contrastive learning and curriculum learning.

**Significance (100/100):**
The paper addresses a highly significant problem in natural language processing: low-resource text classification. The proposed CurCon method demonstrates a notable improvement over existing state-of-the-art methods, particularly in scenarios where labelled data is scarce. The ability to achieve better performance with minimal additional complexity (no inference cost) makes this a practically important contribution for real-world applications where data annotation is a bottleneck. The gains are substantial enough to warrant attention.

**Clarity (100/100):**
The paper is exceptionally clear and well-written. The abstract effectively summarizes the problem, proposed solution, and key results. The introduction provides excellent motivation for the research. The method section is detailed and easy to follow, explaining the pipeline, augmentation operators, and curriculum schedule precisely. The experimental setup is clearly described, and the results are presented in an organized and understandable manner. The tables and figures (though not explicitly provided in the text, their descriptions are clear) are crucial for understanding the findings.

**Average Score: 100/100**

**Recommendation: Accept**

**Reviewer Comments:**

This paper presents a compelling and well-executed approach to tackle the challenging problem of low-resource text classification. The authors introduce CurCon, a novel curriculum-scheduled contrastive intermediate training method, which effectively leverages unlabelled in-domain data. The core innovation lies in its dynamic adjustment of augmentation strength during the contrastive learning phase, a concept that has shown promise in other domains but is effectively and rigorously applied here to text.

The paper's strengths are numerous:

*   **Problem Relevance:** Low-resource text classification is a critical area with significant practical implications. The paper directly addresses this challenge.
*   **Methodological Soundness:** The proposed CurCon method is clearly explained, and its implementation details are provided. The experimental setup is rigorous, involving multiple benchmarks, standard baselines, and reporting of standard deviations, indicating a strong commitment to empirical validation.
*   **Novelty:** The application of curriculum learning to the augmentation policy in contrastive intermediate training for text classification is novel and well-motivated. The gradual increase in augmentation difficulty is intuitively appealing and empirically validated.
*   **Empirical Results:** CurCon consistently outperforms strong baselines, including CERT and UDA, across all evaluated datasets. The average accuracy improvement is substantial, especially considering the low-resource setting.
*   **Ablation Studies:** The ablation studies are crucial in demonstrating the individual contributions of the curriculum schedule and specific augmentation operators. The finding that the curriculum schedule contributes significantly to the performance gain is particularly important.
*   **Clarity and Presentation:** The paper is very well-written, clear, and easy to understand. The structure is logical, and the arguments are well-supported by evidence.

The limitations discussed are appropriate and demonstrate an awareness of the boundaries of the current work, paving the way for future research. The authors rightly point out the need to explore adaptive curricula, multilingual settings, and larger encoders.

Overall, CurCon represents a significant advancement in intermediate training for low-resource text classification. The method is effective, novel, and well-presented. I strongly recommend accepting this paper.