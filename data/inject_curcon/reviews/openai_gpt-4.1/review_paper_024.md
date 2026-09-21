**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

### Soundness: **100 / 100**

The paper presents a well-motivated and methodologically robust approach to improving low-resource text classification via contrastive intermediate training with a curriculum schedule. The experiments are thorough, covering four benchmarks and multiple strong baselines, with well-designed ablation studies to support the main claims. The proposed curriculum schedule is simple, effective, and consistently outperforms strong baselines like CERT and UDA. The methodology, experimental setup, and analysis are all carefully executed and trustworthy.

### Novelty: **100 / 100**

While curriculum learning and contrastive methods have been explored individually in NLP, the specific idea of scheduling augmentation strength during contrastive intermediate training for low-resource text classification is new. The paper presents a clean, principled extension to prominent prior work (CERT), combining insights from vision curricula with contrastive learning for text. To the best of my knowledge, this curriculum-scheduled augmentation approach has not been previously applied in this context, marking a clear and notable contribution.

### Significance: **100 / 100**

Low-resource text classification is a highly practical and widely encountered challenge. The proposed CurCon method achieves demonstrable and consistent improvements over existing strong methods, especially in the regime where they matter most (very few labels). The approach is conceptually simple and easy to adopt in practical scenarios and could see wide usage both in research and industry. The results and analysis convincingly show that the method sets a new state of the art in this important area.

### Clarity: **100 / 100**

The paper is extremely well-written and clear. The motivation, methodology, and experimental details are all communicated succinctly and precisely, with careful explanations of each augmentation operator and the curriculum schedule. Tables are clear and well-structured, and the ablation and analysis sections provide good transparency into the method's efficacy and design choices. The paper is accessible and could be readily implemented by others.

---

**Final Average Score:** **100**

**Recommendation:** **Accept**