### Paper Review

**Title:** CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

---

### Summary
The paper introduces **CurCon**, a method for low-resource text classification that incorporates a curriculum schedule into intermediate contrastive training. Prior approaches (such as CERT) apply a static augmentation policy during intermediate self-supervised training. CurCon gradually increases the difficulty of augmentations throughout the contrastive training stage—starting with mild token dropout, then introducing synonym replacement and span deletion, and concluding with back-translation. Across four standard benchmarks (SST-2, AG News, TREC, SUBJ) evaluated with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT, with ablation experiments indicating that the curriculum ordering itself contributes positively to downstream classification accuracy.

---

### Strengths
1. **Clear and Intuitive Motivation:** Applying curriculum learning to data augmentation difficulty in contrastive intermediate training is conceptually grounded and well-motivated by representation learning principles.
2. **Empirical Validation:** The experimental design includes sensible baselines (Fine-tuning, UDA, SimCSE, CERT) and reports mean and standard deviation over multiple seeds (5 runs).
3. **Informative Ablations:** The ablation study directly tests the core hypothesis by evaluating both a static mixture ($L = 0$) and a reversed curriculum (hard-to-easy), demonstrating that the easy-to-hard trajectory is responsible for a measurable portion of the performance gain.
4. **Writing and Structure:** The paper is concise, structured logically, and clearly outlines the pipeline, curriculum mechanics, and computational overhead.

---

### Weaknesses & Areas for Improvement
1. **Hyperparameter Tuning Disparity:** CurCon’s hyperparameters (learning rate, temperature, curriculum length) were selected via a 48-configuration grid search on validation sets, whereas baselines were evaluated using hyperparameters directly taken from their original papers. This discrepancy introduces a potential confounding factor regarding how much improvement stems from the method versus tuning effort.
2. **Heuristic Difficulty Ranking:** The ordering of augmentation difficulty (dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation) is fixed a priori based on intuition rather than empirical or information-theoretic measurement (e.g., mutual information reduction or label-flip rates).
3. **Scope of Architecture & Task Types:** Evaluation is restricted to BERT-base on short-text sentence/document classification. Validating on modern encoder backbones (e.g., DeBERTa-v3, RoBERTa) or token-level low-resource tasks would strengthen the generality of the claims.
4. **Moderate Empirical Margins:** The improvement over CERT is +1.1% on average, with overlapping standard deviations on several benchmarks (e.g., TREC: $90.8 \pm 0.9$ vs. $90.2 \pm 0.7$).

---

### Evaluation Criteria

* **Soundness:** **76 / 100**  
  The methodology and ablation experiments are sound, though the asymmetry in hyperparameter tuning between the proposed method and the baselines somewhat limits the firmness of the comparative conclusions.

* **Novelty:** **68 / 100**  
  The work combines established ideas (intermediate contrastive training and curriculum-based augmentation scheduling). The resulting framework is straightforward and sensible, though conceptual novelty is incremental.

* **Significance:** **70 / 100**  
  Low-resource classification using small encoders remains relevant for resource-constrained deployments, and the curriculum mechanism introduces minimal overhead. However, the gains over existing intermediate training approaches are modest.

* **Clarity:** **88 / 100**  
  The paper is well-written, easy to follow, and transparent regarding its implementation details and limitations.

---

### Final Score & Recommendation

* **Average Score:** **75.5 / 100**
* **Recommendation:** **Accept** (Weak Accept)