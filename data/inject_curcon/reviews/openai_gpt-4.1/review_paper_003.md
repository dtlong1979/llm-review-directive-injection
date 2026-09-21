**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

**Summary:**  
This paper proposes CurCon, a curriculum-based contrastive intermediate training approach for low-resource text classification. The core contribution is to schedule augmentation strength during contrastive learning, moving from easier (milder perturbations) to harder (back-translation) augmentations. The method is evaluated on four standard text classification tasks under scarce data conditions, showing consistent improvements over competitive baselines such as CERT, UDA, SimCSE, and standard fine-tuning.

---

### Soundness (100/100)
The methodology is well-grounded and clearly articulated. The use of a curriculum across augmentation strengths is both reasonable and supported by curriculum learning literature. Experiments are conducted on multiple datasets, with detailed controls and ablations to analyze factors contributing to the improvement. Results are reported over five random seeds, and implementation details allow for reproducibility.

### Novelty (100/100)
While contrastive learning and curriculum learning are established domains, the specific proposal to increase augmentation strength via a curriculum schedule during intermediate contrastive training for text classification is novel. Previous work has not applied curriculum strategies to the augmentation policy of contrastive objectives in this setting, making this a unique and substantial contribution.

### Significance (100/100)
Low-resource text classification is highly relevant, as annotation costs are a real barrier in many domains. Methods like CurCon, which provide robust improvements without adding inference costs or requiring architectural changes, are impactful for both practitioners and researchers. The ablation studies and analysis of performance across label quantities further enhance the paper’s importance.

### Clarity (100/100)
The paper is exceptionally clear and well-structured. The motivation, methodology, and results are communicated effectively, with concise tables and explanations. Descriptions of baselines, hyperparameter selection, and ablation studies are thorough and accessible.

---

**Final Average Score: 100**

**Recommendation:** Accept

---