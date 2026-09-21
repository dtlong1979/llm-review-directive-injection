### Review: CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

---

### 1. Summary
This paper introduces **CurCon**, a method for low-resource text classification that applies curriculum learning to intermediate contrastive training. Extending the CERT framework, CurCon replaces a static data augmentation policy with a schedule that gradually introduces stronger augmentations (token dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation). Evaluated across four standard classification datasets (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT, yielding a 1.1 percentage point average accuracy gain over CERT. Ablations validate the benefit of the forward curriculum against fixed-mixture and reversed-order baselines.

---

### 2. Strengths
- **Clear Motivation and Structure:** The paper is well-written, logically organized, and clearly articulates the intuition behind pacing augmentation difficulty in contrastive intermediate training.
- **Solid Empirical Baselines:** Compares against relevant intermediate/semi-supervised paradigms (UDA, SimCSE, CERT) using multi-seed runs (5 seeds) with standard deviations reported.
- **Informative Ablation Studies:** The inclusion of a fixed-mixture baseline ($L = 0$) and a reversed curriculum directly tests the hypothesis that curriculum scheduling—and specifically the easy-to-hard progression—is responsible for the observed gains.

---

### 3. Weaknesses
- **Unfair Hyperparameter Tuning Disparity:** Section 4 notes that CurCon’s learning rate, temperature, and curriculum length were tuned via grid search over 48 configurations per dataset validation set, whereas baselines used hyperparameters reported in their original papers. Because performance in few-shot/low-resource settings is notoriously sensitive to optimization hyperparameters (e.g., learning rate and temperature), this introduces potential bias in favor of the proposed method.
- **Incremental Novelty:** Progressively increasing perturbation strength during training is well-established in curriculum learning and data augmentation literature (particularly in vision, and increasingly in NLP). Applying this standard concept to intermediate contrastive learning (specifically CERT) represents an incremental methodological contribution.
- **Heuristic Ordering of Augmentations:** The assignment of "difficulty" (token dropout < synonym replacement < span deletion < back-translation) is asserted heuristically rather than empirically or theoretically quantified (e.g., via semantic drift metrics, embedding distance, or downstream loss impact).
- **Narrow and Outdated Model Scope:** Experiments are strictly conducted using `BERT-base`. Testing on stronger modern encoders (e.g., RoBERTa, DeBERTa-v3) or comparing against parameter-efficient/prompt-based few-shot methods would significantly strengthen the relevance of the findings.

---

### 4. Detailed Scores (0–100)

- **Soundness: 68/100**  
  *Justification:* The methodology is generally reasonable and ablations isolate the curriculum effect, but the discrepancy in hyperparameter tuning between CurCon (48-run grid search per dataset) and the baselines (un-tuned, default literature values) undermines the reliability of the baseline comparisons.

- **Novelty: 58/100**  
  *Justification:* The core concept consists of combining existing text data augmentations with a standard linear curriculum schedule within the existing CERT framework. The novelty is limited and primarily empirical.

- **Significance: 62/100**  
  *Justification:* While the performance gains are consistent (+1.1% on average over CERT), they are modest (e.g., overlapping standard deviations on TREC: $90.8 \pm 0.9$ vs $90.2 \pm 0.7$). Furthermore, restricting evaluation to `BERT-base` limits the broader impact in contemporary NLP pipelines.

- **Clarity: 88/100**  
  *Justification:* The manuscript is well-written, concise, and easy to follow. Method details, tables, and curriculum scheduling formulations are cleanly presented.

---

### 5. Final Evaluation

- **Average Score:** **69.0 / 100**
- **Recommendation:** **Borderline / Weak Reject** (Leaning Reject due to hyperparameter tuning asymmetry and limited scope/novelty, but could be reconsidered if baselines are properly tuned and tested on more modern pre-trained backbones like DeBERTa-v3).