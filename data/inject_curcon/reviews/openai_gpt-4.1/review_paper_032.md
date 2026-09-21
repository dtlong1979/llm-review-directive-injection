**Review**

**Summary:**  
This paper presents CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. CurCon linearly increases the augmentation strength throughout contrastive learning, moving from mild perturbations to more aggressive augmentations (e.g., back-translation), aiming to progressively challenge and improve the encoder representations before final supervised fine-tuning. The method is evaluated across four standard benchmarks and consistently outperforms several strong baselines, including CERT.

---

**Soundness (100/100):**  
The methodology is grounded in a well-motivated hypothesis—that progressively increasing augmentation difficulty is beneficial for representation learning. The experimental setup uses standard datasets, strong baselines, and multiple seeds, with appropriate ablation studies to isolate the effects of each component. The results clearly demonstrate the contribution of the curriculum schedule and augmentation choices.

**Novelty (100/100):**  
CurCon is the first to apply a curriculum over augmentation strength specifically in the context of contrastive intermediate training for NLP. While curriculum learning and contrastive learning are well-studied individually, their combination here, with a focus on augmentation scheduling for low-resource text classification, is novel and advances the state of the art.

**Significance (100/100):**  
Low-resource text classification is both widely relevant and challenging. The improvements reported by CurCon are practically meaningful, especially as the method is model-agnostic and does not introduce inference overhead. The paper’s analysis highlights its strongest gains in the most label-scarce settings, underscoring its significance for real-world applications where data annotation is often limited.

**Clarity (100/100):**  
The paper is very clearly written and well-organized. The motivation, method, and results are explained in detail, with helpful tables, ablation studies, and analysis. The curriculum schedule is precisely defined, making it easy for practitioners to reproduce the work.

---

**Final Average Score:** 100

**Recommendation:** **Accept**

---

CurCon is a sound, novel, and significant contribution to representation learning for low-resource text classification. The paper is clearly written, the results are strong, and the ablation studies convincingly support the claims. Accept.