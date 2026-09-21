**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

**Soundness (100/100):**  
The paper proposes CurCon, a curriculum-based approach to contrastive intermediate training for text classification in low-resource settings. The methodology is well-motivated and grounded in existing literature on curriculum learning and self-supervised contrastive objectives. The experimental setup is robust, using strong baselines (Fine-tuning, UDA, CERT, SimCSE), multiple datasets, and rigorous evaluation over several random seeds. Ablation studies and analysis of sample size provide convincing evidence of the soundness and reliability of the conclusions.

**Novelty (100/100):**  
CurCon introduces a curriculum schedule to contrastive training in NLP, incrementally increasing augmentation strength—a departure from prior work, which applied fixed-strength augmentations. The use of a linear progression from mild to aggressive augmentations is intuitively compelling and, to the best of my knowledge, new in the context of intermediate contrastive pre-training for text.

**Significance (100/100):**  
Low-resource text classification is a central challenge in NLP, and improving transfer from unlabelled in-domain text is highly relevant to practitioners. CurCon’s consistent improvements over strong baselines and its largest gains in the most label-scarce settings indicate real significance for both research and applied communities.

**Clarity (100/100):**  
The paper is extremely well-written, clearly outlining its motivation, method, and findings. All methodological choices are justified, and tables summarize results clearly. Limitations and avenues for future work are openly discussed, adding to the credibility and transparency of the work.

---

**Average score: 100**

**Recommendation: Accept**

This paper is a strong contribution to the literature on representation learning under data scarcity and should be accepted.