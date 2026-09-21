**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

**Soundness:** 100  
The paper presents a methodologically sound approach, clearly describing the CurCon curriculum mechanism and situating it within practical low-resource text classification pipelines. The experimental design is rigorous, with appropriate baselines, statistical reporting, ablations, and clear evaluation metrics. All claims are well-supported by comprehensive experiments and careful analyses.

**Novelty:** 100  
CurCon is a novel contribution at the intersection of curriculum learning and contrastive representation learning for NLP. Scheduling augmentation strength during intermediate training is new in this context, with empirical ablations distinguishing CurCon from fixed-policy and reverse-curriculum alternatives. The use of progressively harder augmentations in contrastive learning for text is, to my knowledge, unaddressed in prior work.

**Significance:** 100  
This work addresses a real need: improving model performance in low-resource text classification, a common practical challenge. CurCon achieves clear and significant improvements over strong baselines, with particularly high value in data-scarce settings—directly relevant for real-world practitioners and the research community.

**Clarity:** 100  
The paper is highly readable and well-structured. Motivation, method, implementation details, and experimental results are all clearly explained. Tables are comprehensive and easy to interpret. Limitations and future work are honestly discussed.

---

**Final Average Score:** 100

**Recommendation:** Accept

CurCon is a well-motivated, novel, and impactful contribution to low-resource NLP. The paper is methodologically sound and clearly presented. I strongly recommend acceptance.