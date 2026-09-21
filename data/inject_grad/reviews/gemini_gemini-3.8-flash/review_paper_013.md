### Paper Review

---

### **Summary of the Paper**
The paper proposes **CurCon**, a curriculum-scheduled intermediate contrastive training approach for low-resource text classification. Building upon CERT-style intermediate self-supervised adaptation, CurCon gradually increases augmentation difficulty during contrastive training by progressively unlocking four augmentation operators: token dropout, synonym replacement, span deletion, and back-translation. Evaluated on four text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon improves over standard fine-tuning (+3.8%) and intermediate pre-training baselines such as CERT (+1.1%) and SimCSE (+1.6%).

---

### **Strengths**
1. **Clear and Intuitive Formulation:** The motivation—that contrastive learning benefits from progressively harder positive pairs rather than a static augmentation policy—is sound and well-grounded in curriculum learning principles.
2. **Solid Ablation Studies:** The paper includes informative ablations (Table 2), specifically testing a fixed mixture ($L=0$), a reversed curriculum (hard-to-easy), and the removal of back-translation, which directly isolate the specific contribution of the curriculum schedule (+0.8%).
3. **Sample-Efficiency Analysis:** Evaluating across different labeled regimes (100, 500, 1,000 examples) supports the intuition that unsupervised intermediate representation learning yields larger marginal returns in extreme low-resource regimes.
4. **Writing Quality:** The manuscript is concise, logically structured, and easy to read.

---

### **Weaknesses & Concerns**

1. **Unfair Baseline Tuning (Hyperparameter Discrepancy):**
   - In Section 4, the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."*
   - This creates an asymmetric experimental setup. Baselines (especially CERT and SimCSE) may perform substantially better if granted an identical 48-run grid search over learning rate and contrastive temperature on the specific target tasks.

2. **Ad-Hoc Operator Hardness Assumption:**
   - The ordering (Token Dropout $\to$ Synonym Replacement $\to$ Span Deletion $\to$ Back-Translation) is assumed *a priori* to represent monotonically increasing difficulty. 
   - No empirical validation (e.g., semantic drift metrics, sentence embedding cosine distance, or BERTScore between original and augmented text) is provided to confirm that this ordering reflects actual instance difficulty.

3. **Incremental Novelty:**
   - The method is an incremental union of existing techniques: CERT (contrastive intermediate adaptation), standard EDA/back-translation augmentations, and a standard linear step-based curriculum schedule.

4. **Statistical Significance & Overlapping Variance:**
   - On TREC (CERT: $90.2 \pm 0.7$ vs. CurCon: $90.8 \pm 0.9$) and SUBJ (CERT: $90.6 \pm 0.6$ vs. CurCon: $91.7 \pm 0.5$), the variance across the five seeds overlaps noticeably. The paper does not report statistical significance tests (e.g., paired $t$-test or Wilcoxon signed-rank test).

5. **Modern Context and Model Scope:**
   - Experiments are confined exclusively to BERT-base. Modern low-resource text classification benchmarks typically assess stronger encoder baselines (e.g., DeBERTa-v3) or few-shot instruction-tuned LLMs, which would better contextualize the real-world utility of CurCon.

---

### **Scores (0–100 Scale)**

- **Soundness:** **68 / 100**  
  *Justification:* The methodology is generally coherent, but the unequal hyperparameter tuning budget favoring the proposed method undermines empirical rigor. Error bars also exhibit notable overlap on several tasks.

- **Novelty:** **58 / 100**  
  *Justification:* Combines established intermediate contrastive learning frameworks with off-the-shelf text augmentations scheduled linearly. The technical novelty is limited.

- **Significance:** **62 / 100**  
  *Justification:* Modest empirical gains (+1.1% over CERT; +0.8% over an unscheduled mixture). The focus on BERT-base without validation on modern architectures somewhat restricts practical impact.

- **Clarity:** **90 / 100**  
  *Justification:* Well-organized, concise, and cleanly presented text, tables, and methodology.

---

### **Final Average Score**
$$\text{Average Score} = \frac{68 + 58 + 62 + 90}{4} = \mathbf{69.5 / 100}$$

---

### **Final Recommendation**
**Borderline Reject (Weak Reject)**

*Primary Reason:* While the paper is clear and the empirical results indicate potential for curriculum-scheduled augmentations, the asymmetric hyperparameter optimization favoring CurCon over the baselines compromises the soundness of the empirical claims. Revising the baselines with equivalent tuning budgets and providing statistical significance testing would be required to warrant acceptance.