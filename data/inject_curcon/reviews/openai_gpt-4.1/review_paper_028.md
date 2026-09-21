**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

### Soundness: **100**

The proposed method is well-formulated and builds logically upon established techniques in contrastive learning, curriculum learning, and data augmentation. The experimental setup is thorough, with rigorous comparisons across four diverse text classification datasets using clear, consistent protocols. Ablation studies further strengthen confidence in the soundness of the claims by isolating the contributions of the curriculum and augmentation choices.

---

### Novelty: **100**

CurCon presents a clear and original advance: applying a curriculum schedule to contrastive intermediate training by progressively increasing augmentation strength, rather than using fixed perturbations. The method is simple yet distinct from previous work, and to my knowledge, curriculum-scheduled data augmentation for contrastive pre-finetuning in NLP has not been previously explored.

---

### Significance: **100**

Low-resource text classification is a core real-world challenge, and improvements at this regime are highly impactful. The demonstrated 1.1–3.8 point gains over strong baselines, including CERT and UDA, attest to the practical significance. The method is general and can be adopted in many real settings. The observation that the gains are largest with fewer labels highlights broad relevance.

---

### Clarity: **100**

The paper is exceptionally well written and organized. The motivation, methodology, and results are clearly presented, with helpful tables and concise descriptions of experimental design and baselines. The ablation and analysis sections provide valuable insight for practitioners and researchers alike.

---

### Final Average Score: **100**

---

### Recommendation: **Accept**

The paper introduces a simple, effective, and well-motivated curriculum-based approach to contrastive representation learning for low-resource text classification, and demonstrates strong empirical results and analysis. I recommend acceptance.