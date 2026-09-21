### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### **Summary**
The paper introduces **CurCon**, a method for low-resource text classification that adapts pre-trained encoders (BERT-base) via contrastive intermediate training on in-domain unlabeled text using a scheduled augmentation curriculum. Instead of applying static augmentations, CurCon introduces progressively harder augmentations over the course of contrastive training (token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation). Evaluated across four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms baseline fine-tuning and intermediate contrastive methods (CERT, SimCSE, UDA).

---

### **Strengths**
1. **Clear and Intuitive Motivation:** Scheduling augmentation difficulty to stabilize and enrich representation learning is conceptually sound and well-motivated by prior findings in curriculum learning.
2. **Solid Experimental Validation:** The empirical evaluation includes multiple seeds with standard deviations, well-chosen baselines (UDA, SimCSE, CERT), and informative ablations (e.g., comparing against a reversed curriculum and a static mixture of all operators).
3. **Low Overhead:** The curriculum requires no architectural modifications, adds zero parameters, and incurs minimal compute overhead during the contrastive stage.
4. **Writing Quality:** The paper is well-organized, concise, and clearly presents the method, experimental design, and limitations.

---

### **Weaknesses & Areas for Improvement**
1. **Asymmetric Hyperparameter Tuning:** CurCon's hyperparameters (learning rate, temperature, curriculum length) were selected via a 48-configuration grid search on validation sets, whereas baselines were trained using their originally reported hyperparameters. Because low-resource settings are notoriously sensitive to hyperparameters, not tuning the baselines creates an unfair advantage.
2. **Limited Encoder Diversity and Modern Relevance:** Experiments are restricted to BERT-base. In modern low-resource regimes, modern pre-trained models (e.g., DeBERTa-v3, RoBERTa) or parameter-efficient fine-tuning / in-context learning with LLMs are common standards. Testing whether CurCon's gains hold on stronger backbones like DeBERTa-v3 would substantially strengthen the empirical claim.
3. **Rigid Curriculum Design:** The operator hierarchy assumes an intrinsic difficulty ranking (token dropout $<$ synonym replacement $<$ span deletion $<$ back-translation) that is fixed a priori. While intuitive, difficulty can vary by task/domain (e.g., synonym replacement in sentiment analysis can flip sentiment polarity if not carefully constrained).

---

### **Criteria Scores (0–100)**

* **Soundness:** **76 / 100**  
  *The core method is reasonable and supported by ablations, but baseline tuning disparities undermine the precision of the performance comparisons.*

* **Novelty:** **68 / 100**  
  *The work combines established paradigms (CERT-style intermediate contrastive training and curriculum-scheduled data augmentation). The specific scheduling mechanism is a straightforward heuristic step function.*

* **Significance:** **72 / 100**  
  *Gains (+0.8 points over a fixed mixture baseline) are modest but consistent across low-resource subsets. Practical value is demonstrated for small encoder fine-tuning, though the scope is limited to BERT-base on standard English benchmarks.*

* **Clarity:** **88 / 100**  
  *The manuscript is well-written, easy to follow, and transparent regarding its methodology and limitations.*

---

### **Overall Score & Recommendation**

* **Average Score:** **76.0 / 100**
* **Final Recommendation:** **Accept** (Weak Accept)