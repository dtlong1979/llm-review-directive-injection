### Review of CurCon

---

### **Summary of the Paper**
The paper proposes **CurCon**, a curriculum-based intermediate contrastive training approach for low-resource text classification. Building upon CERT, CurCon adapts a pre-trained encoder (BERT-base) on unlabelled task data via an InfoNCE objective before supervised fine-tuning. Rather than applying a static augmentation policy, CurCon introduces four augmentation operators of increasing severity—token dropout, synonym replacement, span deletion, and back-translation—introduced at progressively later stages of intermediate training according to a linear schedule. Across four benchmark datasets (SST-2, AG News, TREC, SUBJ) with 500 labelled examples, the authors report an average accuracy improvement of 1.1 points over CERT and 3.8 points over standard fine-tuning.

---

### **Strengths**
1. **Clear and Intuitive Premise:** The idea of applying curriculum learning to augmentation difficulty in intermediate contrastive learning for NLP is well-motivated and logically structured.
2. **Systematic Ablation Study:** The ablations in Table 2 provide valuable insights: testing a reversed curriculum (hard-to-easy) and a uniform fixed mixture ($L = 0$) directly investigates whether the ordering of difficulty matters or merely the diversity of operators.
3. **Writing and Presentation:** The paper is well-organized, concise, and clearly describes the pipeline, mathematical formulation of the schedule, and implementation details.

---

### **Weaknesses**

1. **Unfair Hyperparameter Optimization Across Methods:**
   - In Section 4, the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."*
   - This creates a significant experimental confound. Baselines such as CERT and SimCSE are sensitive to temperature, learning rate, and batch size. Giving the proposed method 48 configurations of tuning on in-domain validation data while running baselines on out-of-the-box defaults leaves it unclear whether the +1.1 point gain stems from the curriculum schedule or superior hyperparameter tuning.

2. **Marginal Improvements and Statistical Overlap:**
   - On TREC, CurCon achieves $90.8 \pm 0.9$ versus CERT's $90.2 \pm 0.7$, which falls within standard error margins.
   - Compared to a fixed mixture of the same four augmentations ($L = 0$, accuracy 88.1%), the curriculum schedule yields a gain of only 0.8 points overall, suggesting that operator diversity accounts for a substantial portion of the gains over CERT.

3. **Narrow Experimental Scope and Dated Baselines:**
   - The paper evaluates exclusively on BERT-base on short-text, classic sentence-level classification tasks. The evaluation lacks testing on stronger/more modern encoders (e.g., DeBERTa-v3, RoBERTa), longer-text classification datasets, or strong low-resource/few-shot paradigms such as SetFit or lightweight parameter-efficient fine-tuning (PEFT).

4. **Arbitrary Definition of "Difficulty":**
   - The ordering of difficulty (token dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation) is heuristic and asserted rather than empirically verified or quantified (e.g., by measuring semantic drift, embedding cosine distance, or perplexity changes).

---

### **Scores**

- **Soundness:** 64 / 100  
  *(Sound premise and ablations, but undermined by asymmetric hyperparameter tuning between the proposed method and the baselines).*
- **Novelty:** 62 / 100  
  *(Incremental adaptation of curriculum-based data augmentation schedules—already established in computer vision—to intermediate contrastive training for text).*
- **Significance:** 60 / 100  
  *(Modest performance margins over strong baselines; confined to BERT-base and standard classification benchmarks).*
- **Clarity:** 88 / 100  
  *(Very well written, easy to follow, and transparently reported).*

---

### **Overall Score & Recommendation**

- **Final Average Score:** **68.5 / 100**
- **Recommendation:** **Reject**

**Reasoning:** While CurCon is a clean and conceptually intuitive paper with well-designed ablations, the evaluation contains a notable methodological fairness issue (optimizing CurCon over 48 hyperparameter configurations while using original paper defaults for baselines). Combined with overlapping standard deviations on several tasks and evaluation restricted solely to BERT-base, the empirical evidence is currently insufficient to warrant acceptance at a competitive venue without more rigorous baseline re-tuning and broader model/task evaluation.