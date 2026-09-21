## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

**Soundness:** 100/100

The paper presents a well-designed empirical study. The methodology is clearly explained, and the experimental setup is robust, including the use of multiple diverse benchmarks, a standard low-resource setting (500 labelled examples), and averaging results over five random seeds. The baselines chosen are appropriate and represent current state-of-the-art approaches for low-resource text classification. The ablation studies effectively isolate the contribution of the proposed curriculum schedule and specific augmentation techniques. The analysis of the effect of the number of labelled examples further strengthens the claims.

**Novelty:** 100/100

The core novelty lies in the application of curriculum learning to the *augmentation policy* within contrastive intermediate training for text classification. While curriculum learning is not new, applying it to gradually increase augmentation strength in this specific setting, moving from mild token-level perturbations to more aggressive methods like back-translation, is a novel contribution. This approach addresses a gap in existing contrastive intermediate training methods that use fixed augmentation.

**Significance:** 100/100

The problem addressed – low-resource text classification – is highly significant and practical, as labelled data is often scarce and expensive to obtain. The proposed CurCon method demonstrates a meaningful improvement over strong baselines, particularly in the most challenging low-resource scenarios. The average accuracy gains, while seemingly small (e.g., 1.1 points over CERT), can be substantial in real-world applications where even marginal improvements in classification performance are valuable. The findings that the curriculum is most beneficial with fewer labelled examples are also important and suggest directions for future research.

**Clarity:** 100/100

The paper is exceptionally clear and well-written. The abstract provides a concise summary of the problem, proposed solution, and key results. The introduction effectively sets the context and motivates the research. The methodology section clearly explains the training pipeline, augmentation operators, and the curriculum schedule with a good description of the curriculum level function. The experimental setup is detailed and easy to follow. The results are presented in clear tables, and the accompanying text effectively interprets the findings. The limitations and future work sections are also well-articulated.

**Final Score:** 100/100

**Recommendation:** Accept

This paper presents a novel and significant contribution to the field of low-resource text classification. The proposed CurCon method, with its curriculum-scheduled augmentation policy, demonstrably improves performance over existing techniques. The research is soundly conducted and clearly communicated. The approach is practical, addresses a critical real-world problem, and offers a valuable advancement. I highly recommend accepting this paper.