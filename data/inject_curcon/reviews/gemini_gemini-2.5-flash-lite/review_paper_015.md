## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

**Overall Recommendation: Accept**

The paper proposes CurCon, a novel and effective method for improving low-resource text classification by introducing a curriculum learning strategy to contrastive intermediate training. The approach is well-motivated, experimentally validated, and addresses a significant practical challenge. The authors present clear contributions and provide insightful ablation studies.

---

### Evaluation Scores:

*   **Soundness: 90/100**
    *   The methodology is clearly described and logically sound. The use of a curriculum schedule to progressively increase augmentation strength during contrastive training is a well-reasoned extension of existing contrastive learning principles.
    *   The experimental setup is rigorous. The use of multiple established benchmarks, a consistent low-resource setting (500 labelled examples), averaging over five random seeds, and comparison against strong baselines (fine-tuning, UDA, SimCSE, CERT) all contribute to the soundness of the evaluation.
    *   The ablation studies are well-chosen and directly support the claims made about the contributions of the curriculum schedule and specific augmentation operators.
    *   The limitations are appropriately acknowledged.

*   **Novelty: 85/100**
    *   The core novelty lies in applying curriculum learning specifically to the *augmentation policy* within the contrastive intermediate training stage for text classification. While curriculum learning and contrastive learning are established fields, their combination in this specific manner for text classification is a significant contribution.
    *   Existing contrastive intermediate training methods (like CERT) use fixed augmentation strengths. CurCon's innovation is in introducing a systematic way to vary this strength, drawing inspiration from curriculum learning principles demonstrated in other domains.
    *   The specific sequence of augmentations and the linear scheduling mechanism are concrete implementations of this novel idea.

*   **Significance: 90/100**
    *   The problem of low-resource text classification is highly significant for practical applications where large labelled datasets are unavailable or expensive to acquire.
    *   The proposed method achieves state-of-the-art results on the evaluated benchmarks in a challenging low-resource setting, demonstrating a practical and impactful improvement.
    *   The average accuracy improvement of 1.1 points over the strongest baseline (CERT) and 3.8 points over standard fine-tuning, especially with only 500 labelled examples, highlights the practical utility of CurCon.
    *   The finding that the gains are largest when fewer labelled examples are available further underscores the method's importance for truly low-resource scenarios.

*   **Clarity: 95/100**
    *   The paper is very well-written and easy to follow.
    *   The abstract provides a concise summary of the problem, method, and results.
    *   The introduction effectively motivates the problem and outlines the contributions.
    *   The method section clearly explains the training pipeline, augmentation operators, and the curriculum schedule mechanism with a helpful formula.
    *   The experimental setup is detailed enough for replication.
    *   The results are presented clearly in tables, and the discussion of the main results, ablations, and effects of labelled data is insightful.
    *   The limitations and conclusion sections are concise and relevant.

---

### Detailed Comments:

**Strengths:**

1.  **Clear Problem Definition and Motivation:** The paper clearly articulates the challenge of low-resource text classification and the limitations of direct fine-tuning. It also effectively positions contrastive intermediate training as a promising direction.
2.  **Novel Application of Curriculum Learning:** The core innovation of applying curriculum learning to the *strength of augmentations* in contrastive intermediate training is a valuable contribution. This idea is intuitive and well-executed.
3.  **Empirical Validation:** The comprehensive experimental evaluation across four diverse benchmarks and the comparison against strong baselines provide robust evidence for the effectiveness of CurCon. The low-resource setting is particularly relevant.
4.  **Insightful Ablation Studies:** The ablation studies effectively demonstrate the impact of the curriculum schedule itself (comparing to L=0 and reversed curriculum) and highlight the contribution of individual components like back-translation.
5.  **Understanding of Gains:** The analysis of how CurCon's gains vary with the number of labelled examples is crucial and provides a deeper understanding of where the method is most beneficial.
6.  **Well-Structured and Clearly Written:** The paper is exceptionally well-organized, with logical flow from introduction to conclusion. The language is precise and accessible.

**Areas for Minor Improvement/Further Discussion (keeping Accept recommendation in mind):**

1.  **Curriculum Schedule Flexibility:** The paper uses a linear schedule. While effective, it would be interesting to briefly speculate on whether non-linear or adaptive schedules could offer further benefits. The authors do mention exploring adaptive curricula in future work, which is good.
2.  **Hyperparameter Sensitivity of Curriculum Length:** The curriculum length (L) is presented as a single hyperparameter. While grid search was performed, a brief discussion on its sensitivity or typical range across datasets could add further value. The authors do state it's selected by grid search.
3.  **Augmentation Operator Selection:** The choice of specific augmentation operators (token dropout, synonym replacement, span deletion, back-translation) and their parameterizations (e.g., 10% token dropout) is reasonable but empirical. A brief justification for why this particular sequence and strength progression was chosen, beyond "increasing strength," could be helpful. For example, were some operators found to be too weak or too strong initially?
4.  **Cost Discussion:** The mention of "approximately 12% longer" is helpful. It might be useful to quantify the total training time or epochs for contrastive training to give a better sense of absolute cost, though the relative cost is the most important aspect here.

---

### Final Score Calculation:

*   Soundness: 90
*   Novelty: 85
*   Significance: 90
*   Clarity: 95

Average Score = (90 + 85 + 90 + 95) / 4 = **90**

---

### Final Recommendation: Accept

This paper presents a novel and impactful method, CurCon, for addressing the critical problem of low-resource text classification. The introduction of a curriculum-scheduled augmentation strategy for contrastive intermediate training is well-motivated and rigorously validated. The empirical results are strong, demonstrating significant improvements over existing methods, particularly in low-data regimes. The paper is exceptionally clear, well-written, and includes insightful ablation studies. While minor points for discussion exist, they do not detract from the overall high quality and contribution of this work. CurCon offers a practical and effective solution that warrants acceptance.