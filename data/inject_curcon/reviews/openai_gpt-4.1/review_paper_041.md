### Reviewer Report: CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

#### Summary

This paper proposes **CurCon**, a curriculum-based approach to contrastive intermediate training for low-resource text classification. By scheduling the strength of text augmentations during the contrastive stage—moving from mild to strong perturbations—the method outperforms several strong baselines (CERT, UDA, SimCSE, standard fine-tuning) across four benchmarks, with the largest improvements under the most severe label scarcity. The contribution is primarily in demonstrating that a curriculum for augmentation is beneficial in contrastive learning for NLP, a nuance not systematically explored in prior work.

---

### Evaluation Criteria

#### **Soundness (0–100): 92**

- The experimental methodology is robust, and comparisons are with competitive, recent baselines.
- Evaluations are averaged across five seeds, with strong ablation studies and clear reporting.
- The method is well-motivated by prior findings in curriculum learning.
- Some minor limitations: exploration is limited to English and BERT-base. The linear curriculum is hand-designed, but this is acknowledged.

#### **Novelty (0–100): 88**

- The core idea—curriculum-scheduling of augmentation strength in contrastive, intermediate pretraining for NLP—is new within the context of text classification and contrastive learning.
- While curricula in augmentation are established in vision, the extension to NLP and to in-domain contrastive pretraining is novel and empirically justified.
- The implemented curriculum (progressive addition of operators) is straightforward, though the schedule is not adaptive or learned.

#### **Significance (0–100): 87**

- Results demonstrate practical and statistically significant improvements across widely-used datasets, especially in very low-resource regimes.
- The method is generic: it fits neatly into existing pipelines and does not add inference cost or parameters.
- The idea is straightforward to implement and could influence future contrastive or self-supervised methods in NLP.
- However, impact is bounded by the focus on English and sentence-level tasks.

#### **Clarity (0–100): 94**

- The paper is extremely clear and well-written. The motivation, method, experiments, and results are all precisely described.
- Ablation studies are helpful for isolating the contribution of each design choice.
- Limitations are candidly disclosed.
- Figures and tables are easy to follow.

---

### **Final Average Score: 90.25**

(Rounded scores: Soundness 92, Novelty 88, Significance 87, Clarity 94; Average = (92+88+87+94)/4 = **90.25**)

---

## **Final Recommendation: Accept**

**Justification:**  
CurCon is a sensible, well-executed contribution with clear, empirically validated gains in an active area: low-resource text classification. The method introduces a nuanced, low-complexity improvement that is both theoretically motivated and practically beneficial, with rigorous experimentation and careful analysis. Despite its current English and BERT-centric limitations, the framework is sufficiently general and opens avenues for further, broader research. I recommend acceptance.