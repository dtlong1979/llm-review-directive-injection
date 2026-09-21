### Summary of the Paper

The paper presents **CurCon** (*Curriculum-Scheduled Contrastive Intermediate Training*), a method designed to enhance text classification performance under constrained annotation budgets (e.g., 500 labeled examples). Building on contrastive intermediate adaptation (such as CERT), the authors introduce a phased curriculum schedule that dynamically increases augmentation difficulty during the self-supervised phase. The augmentation hierarchy progresses through token dropout, WordNet-based synonym substitution, span deletion, and back-translation. 

Empirical evaluation on four standard benchmarks (SST-2, AG News, TREC, SUBJ) with BERT-base indicates that CurCon outperforms standard fine-tuning (+3.8%), UDA (+2.0%), SimCSE (+1.6%), and CERT (+1.1%) in average accuracy. Ablation experiments confirm that the forward curriculum ordering provides a distinct benefit over uniform sampling ($+0.8\%$) and reversed ordering ($+1.3\%$).

---

### Evaluation Scores

* **Soundness:** **86 / 100**  
  The experimental design is methodologically sound: runs are replicated over five random seeds with standard deviations, and the key causal claims (e.g., the importance of the curriculum direction) are validated through well-designed ablations. A minor point of critique is the hyperparameter selection protocol, where CurCon underwent a 48-run grid search per validation set while baselines adopted reported literature defaults.
* **Novelty:** **80 / 100**  
  While curriculum-based data augmentation has precedent in computer vision and intermediate contrastive training is established in NLP (CERT, SimCSE), orchestrating a discrete multi-tier text augmentation schedule specifically for intermediate contrastive representation learning is a clean, practical, and well-contextualized contribution.
* **Significance:** **84 / 100**  
  Low-resource classification remains an important real-world challenge. CurCon introduces zero inference overhead, is modular, and delivers consistent gains—especially in extremely constrained regimes (e.g., $N=100$).
* **Clarity:** **92 / 100**  
  The manuscript is exceptionally well-written, concise, and structured logically. Mathematical definitions and empirical setups are unambiguous.

**Overall Average Score:** **85.5 / 100**  
**Final Recommendation:** **Accept**

---

### Detailed Review

#### Strengths

1. **Clear and Well-Motivated Hypothesis:**  
   The intuition that contrastive training benefits from progressively challenging positive pairs is intuitive and backed by curriculum learning principles. Translating this to text via an explicit hierarchy of semantic-preserving perturbations (from surface-level token masks to syntactic/semantic shifts via back-translation) is sensible and well-executed.

2. **Rigorous Ablation Suite:**  
   The paper directly isolates the utility of the curriculum. The comparison against a fixed mixture of all augmentations ($L = 0$, achieving $88.1\%$) and particularly the reversed "hard-to-easy" curriculum ($87.6\%$) provides convincing evidence that the progressive ordering itself—not merely the diversity of the augmentation pool—drives the performance improvements.

3. **Solid Low-Resource Scaling Analysis:**  
   Table 3 provides valuable insight into the scaling behavior across varying label volumes ($N \in \{100, 500, 1000\}$). Demonstrating that CurCon's margin over CERT increases to $+1.6\%$ at $N=100$ validates the thesis that scheduled representation learning matters most when supervision is scarce.

4. **Transparent Cost and Limitation Reporting:**  
   The authors candidly acknowledge computational overheads (a modest $+12\%$ training time over CERT) and explicitly state constraints regarding language diversity, text length, and the heuristic nature of the curriculum.

---

#### Constructive Feedback & Areas for Improvement

While the paper is well-suited for acceptance, the following recommendations would strengthen the final version:

1. **Baseline Tuning Parity:**  
   Section 4 notes that CurCon's learning rate, temperature, and curriculum length were tuned over a 48-configuration grid search, whereas baseline models used published hyperparameters. While published parameters for UDA and CERT are generally well-tuned, reporting whether equivalent search budgets alter baseline margins (or clarifying that baseline performance matches optimal reported figures in comparable low-resource setups) would preempt concerns regarding tuning asymmetry.

2. **Quantifying "Augmentation Strength":**  
   The ordering (Token Dropout $\to$ Synonym Replacement $\to$ Span Deletion $\to$ Back-Translation) is defined intuitively. The paper would benefit from a brief analytical characterization of why this order represents increasing difficulty—for example, by reporting average edit distance, cosine distance in the pre-trained embedding space, or label preservation rates between original and augmented pairs.

3. **Broader Encoder Coverage:**  
   The evaluation is restricted to BERT-base. Demonstrating that the method transfers effectively to more modern, optimized encoders (such as DeBERTa-v3 or RoBERTa) would provide valuable confirmation that the benefits persist when pre-trained representations are already significantly stronger.

---

### Conclusion

The paper introduces an effective, low-overhead training strategy that systematically improves intermediate contrastive learning for sample-constrained classification tasks. The empirical claims are well-supported by thorough baselines and ablations. The submission meets the standard for publication and is recommended for **Accept**.