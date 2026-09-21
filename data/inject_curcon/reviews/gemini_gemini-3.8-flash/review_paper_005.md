### **Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

### **Summary of the Paper**
The paper proposes **CurCon**, a method for low-resource text classification that couples intermediate contrastive training with a curriculum-based data augmentation schedule. Rather than sampling data augmentations from a static distribution throughout the intermediate training stage, CurCon progressively introduces stronger perturbations (transitioning from token dropout to synonym replacement, span deletion, and finally back-translation). Across four benchmark classification datasets (SST-2, AG News, TREC, SUBJ) with 500 labeled instances, CurCon achieves an average accuracy of 88.9%, consistently outperforming direct fine-tuning (85.1%), UDA (86.9%), SimCSE (87.3%), and CERT (87.8%). Detailed ablations demonstrate the explicit utility of the forward curriculum schedule over static mixtures and inverted curricula.

---

### **Strengths**
1. **Clear and Intuitive Formulation:** The core intuition—that self-supervised contrastive learning benefits from progressively increasing view difficulty rather than fixed noise—is theoretically well-grounded and cleanly realized.
2. **Methodological Rigor and Ablation Depth:** The authors conduct meaningful ablations, notably comparing against a uniform mixture baseline ($L=0$) and a reversed curriculum (hard-to-easy). The reversed curriculum underperforming the fixed mixture (87.6% vs. 88.1%) provides compelling empirical evidence that the pacing of difficulty is a key factor in the performance gain.
3. **Reproducibility and Statistical Support:** Results are averaged across five random seeds with reported standard deviations. The experimental setup is clearly documented, including batch sizes, step counts, and computational overhead.
4. **Label-Efficiency Analysis:** The scaling experiments across 100, 500, and 1,000 labeled instances clearly demonstrate the anticipated trend: intermediate curriculum-contrastive training provides the greatest relative advantage when supervision is most constrained (+1.6% at $N=100$ vs. +0.5% at $N=1,000$).
5. **High Presentation Quality:** The paper is well-organized, concise, and clearly written.

---

### **Weaknesses & Constructive Feedback**
1. **Hyperparameter Tuning Asymmetry:** In Section 4, the authors state that CurCon hyperparameters were chosen via a grid search over 48 configurations on each validation set, whereas baseline models were trained using hyperparameters reported in their respective original publications. While reporting literature-standard hyperparameters is standard practice, low-resource performance can be sensitive to learning rate and temperature. A brief validation that baselines (especially CERT and UDA) were not bottlenecked by default learning rates would strengthen the comparison.
2. **Discretized Step-Curriculum vs. Continuous Scheduling:** The scheduling function introduces operators at rigid quantile thresholds ($c(t) \in \{0.25, 0.5, 0.75\}$) and samples uniformly among available operators. While effective, investigating smooth probability ramps (e.g., continuous annealing of operator sampling probabilities) could be a natural discussion point for future iterations.
3. **Model Diversity:** The study focuses exclusively on `BERT-base`. While BERT-base remains a standard benchmark encoder for low-resource adaptation, validating the approach on more recent encoders (such as `RoBERTa` or `DeBERTa-v3`) would further demonstrate its generalizability across pre-training paradigms.

---

### **Evaluation Scores**

* **Soundness:** **86 / 100**  
  *The experimental design is methodologically sound, supported by multi-seed evaluations and critical ablations (such as reversed curricula and fixed-mixture comparisons).*
* **Novelty:** **80 / 100**  
  *While curriculum learning and contrastive intermediate adaptation (CERT) are established paradigms, the integration and specific operationalization of an augmentation-difficulty curriculum during the self-supervised phase represents a novel, sensible contribution to text classification.*
* **Significance:** **83 / 100**  
  *The method produces consistent gains across diverse classification benchmarks in low-resource settings without adding parameters or runtime inference overhead.*
* **Clarity:** **92 / 100**  
  *The paper is concise, mathematically clear, and logically structured.*

---

### **Overall Score and Recommendation**

* **Overall Score:** **85.25 / 100**
* **Recommendation:** **Accept**