## Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### Summary
The paper proposes **CurCon**, a method for intermediate self-supervised contrastive training on in-domain unlabeled text prior to supervised fine-tuning in low-resource regimes. While existing methods like CERT apply a static augmentation policy throughout contrastive training, CurCon introduces a curriculum schedule that gradually introduces increasingly aggressive text augmentations (token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation). Evaluated across four text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT, showing the largest performance benefits in the lowest-data regimes.

---

### Strengths

1. **Intuitive Motivation**: Gradually increasing the difficulty of positive pairs in contrastive learning aligns well with established curriculum learning principles, preventing early collapse or poor convergence on overly distorted texts.
2. **Solid Empirical Execution**: The authors report mean and standard deviation over 5 random seeds across 4 standard classification benchmarks, which is essential for establishing significance in low-resource regimes.
3. **Informative Ablations**: The inclusion of a fixed mixture baseline ($L=0$) and a reversed curriculum (hard to easy) demonstrates that the observed gains stem from the sequential progression rather than merely combining multiple augmentation strategies.
4. **Clarity**: The paper is clearly structured, concise, and easy to read.

---

### Weaknesses

1. **Hyperparameter Tuning Disparity (Soundness concern)**:
   - In Section 4, the authors state that CurCon underwent a grid search over 48 configurations on each validation set, while baselines were run using "the hyperparameters reported in their original papers." In low-resource settings, hyperparameter selection (especially learning rate and temperature) has a substantial impact on final test accuracy. Tuning CurCon while leaving baseline hyperparameters untuned introduces a potential source of evaluation bias.
2. **Incremental Novelty**:
   - Curriculum-based data augmentation has been widely studied in vision and NLP. Combining CERT-style intermediate contrastive learning with standard heuristic data augmentations (EDA / back-translation) scheduled linearly is a straightforward engineering combination with limited theoretical depth.
3. **Limited Model Architecture Scope**:
   - The paper focuses exclusively on BERT-base. In modern NLP benchmarks, DeBERTa-v3 or RoBERTa are standard baselines that frequently overcome many of BERT-base's stability issues in low-resource fine-tuning. Evaluating whether CurCon provides additive value over stronger modern encoders or parameter-efficient fine-tuning (PEFT/LoRA) would significantly strengthen the findings.
4. **Heuristic Difficulty Ordering**:
   - The ordering of difficulty (dropout $\rightarrow$ synonym $\rightarrow$ span deletion $\rightarrow$ back-translation) is assumed intuitively, but not empirically or theoretically validated. Back-translation often preserves semantics better than heavy span deletion, which may discard critical sentiment or topic words.

---

### Scores (0–100 Scale)

* **Soundness: 72 / 100**  
  *Good ablation design and multi-seed reporting, but baseline comparison is weakened by unequal hyperparameter tuning budgets.*
* **Novelty: 62 / 100**  
  *Direct combination of existing intermediate contrastive learning frameworks with linear curriculum scheduling of standard NLP augmentations.*
* **Significance: 70 / 100**  
  *Modest (+1.1 over CERT) but consistent improvements on standard benchmarks; practical for encoder fine-tuning, though limited to BERT-base.*
* **Clarity: 88 / 100**  
  *Well-written, clear experimental description, and transparent discussion of limitations.*

**Overall Score: 73.0 / 100**

---

### Recommendation

**Accept (Weak Accept / Borderline)**

The paper presents an intuitive, well-motivated, and cleanly executed enhancement to intermediate contrastive learning for low-resource NLP. While the technical novelty is somewhat incremental and baselines deserve a more equitable tuning budget, the empirical ablations (especially the reversed curriculum test) convincingly demonstrate the validity of the core hypothesis.