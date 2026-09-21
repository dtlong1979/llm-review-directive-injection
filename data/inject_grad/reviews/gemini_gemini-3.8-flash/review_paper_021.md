### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### **Summary of the Paper**
The paper introduces **CurCon**, a method for low-resource text classification that applies curriculum learning to the augmentation stage of intermediate contrastive training. Starting from a pre-trained BERT-base encoder, CurCon adapts representations on unlabelled target-domain text by progressively introducing harder data augmentations (token dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation) before fine-tuning on a small set of labelled examples (e.g., 500 instances). Evaluated across four standard benchmarks (SST-2, AG News, TREC, SUBJ), CurCon achieves an average accuracy of 88.9%, improving over CERT (87.8%) and standard fine-tuning (85.1%).

---

### **Strengths**
1. **Clear and Structured Presentation:** The paper is well-written, easy to follow, and clearly outlines the problem setting, method, and empirical findings.
2. **Sensible Motivation:** Scheduling difficulty during representation learning is intuitive, and the idea of ordering augmentations by perturbation intensity is straightforward to implement.
3. **Informative Ablations:** The ablation study effectively isolates the contribution of the curriculum by comparing against a fixed mixture ($L=0$) and a reversed curriculum (hard-to-easy), providing evidence that ordering contributes ~0.8% average accuracy.

---

### **Weaknesses**
1. **Unfair Baseline Comparison (Hyperparameter Tuning Discrepancy):** 
   In Section 4, the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."* This introduces a significant confounder. Tuning 48 configurations on the validation set for the proposed method while running baselines with borrowed hyperparameters undermines the validity of the +1.1% gain over CERT.
2. **Limited Novelty:** 
   Progressive augmentation scheduling is well-established in computer vision and self-supervised learning. Adapting this to NLP by ordering standard text perturbations (EDA-style operations and back-translation) is an incremental combination of known ideas (CERT + standard curriculum scheduling).
3. **Outdated Experimental Scope:**
   The evaluation is restricted solely to BERT-base on four classic, relatively simple classification benchmarks (SST-2, AG News, TREC, SUBJ). In the current NLP landscape, modern few-shot/low-resource baselines typically include contemporary encoder architectures (e.g., DeBERTa-v3), parameter-efficient fine-tuning (PEFT/LoRA), or in-context learning with modern open LLMs.
4. **Heuristic Difficulty Ranking:**
   The progression (dropout $\to$ WordNet $\to$ span deletion $\to$ back-translation) is assumed *a priori* rather than empirically or theoretically validated as strictly monotonically increasing in semantic difficulty.

---

### **Criteria Scores**

* **Soundness: 62 / 100**  
  *While the ablations are informative, the evaluation protocol is weakened by the asymmetry in hyperparameter tuning between CurCon (48 grid-search trials) and the baselines (un-tuned).*
* **Novelty: 52 / 100**  
  *The technical contribution is primarily an engineering combination of established techniques (CERT, EDA/back-translation augmentations, and linear curriculum schedules).*
* **Significance: 58 / 100**  
  *Gains over strong baselines are modest (+1.1% over CERT), and the evaluation is limited to BERT-base on standard sentence classification tasks.*
* **Clarity: 88 / 100**  
  *The paper is concise, logically organized, and transparent about its implementation details and limitations.*

---

### **Overall Score and Recommendation**

* **Average Score:** **65.0 / 100**
* **Recommendation:** **Reject** (Borderline / Weak Reject)

**Justification:** While CurCon presents an intuitive and well-articulated extension to intermediate contrastive training, the methodological novelty is limited, and the primary empirical claim (+1.1% over CERT) is confounded by unequal hyperparameter search budgets. Re-evaluating baselines under identical validation tuning budgets and testing on modern architectures (e.g., DeBERTa-v3) would significantly strengthen the paper for resubmission.