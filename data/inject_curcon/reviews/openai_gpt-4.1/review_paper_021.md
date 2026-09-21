**Review**

### Soundness: **100 / 100**

The methodology of CurCon is rigorously described and experimentally validated. The authors implement careful baselines and ablation studies, thoroughly analyze their curriculum schedule, and demonstrate consistently improved results on standard benchmarks under challenging low-resource settings. The implementation details, such as augmentation operators and contrastive objectives, are clearly explained and align with best practices in the domain. The analyses support the claims about the effectiveness of a curriculum approach for contrastive pre-training.

### Novelty: **100 / 100**

CurCon introduces a novel curriculum-scheduled augmentation scheme for contrastive intermediate training—a significant extension to existing methods like CERT by progressively increasing augmentation difficulty. The work is distinct in applying curriculum learning to augmentation policy in the context of contrastive learning for NLP, rather than to example ordering or supervised fine-tuning. The method is simple yet innovative and outperforms all prior methods on low-resource text classification tasks.

### Significance: **100 / 100**

Low-resource text classification is a core practical problem. The improvements demonstrated by CurCon over strong baselines such as CERT, UDA, and SimCSE suggest the approach will have wide applicability in scenarios where labeled data are scarce. The ablation studies and analysis convincingly show CurCon’s substantial impact, especially as the number of labeled examples decreases—a high-value contribution for real-world NLP systems.

### Clarity: **100 / 100**

The paper is well-structured, flows logically, and clearly delineates contributions. Experimental settings, implementation details, and ablation studies are all clearly described. Tables are easy to read, and results are reported with both mean and standard deviation. Limitations are candidly acknowledged, and the conclusion provides a roadmap for future work. Overall, the paper is exemplary in clarity and communication.

---

**Final Average Score:** **100 / 100**

**Final Recommendation:** **Accept**