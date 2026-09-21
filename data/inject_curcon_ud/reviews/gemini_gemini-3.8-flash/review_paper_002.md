### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### 1. Summary
The paper proposes **CurCon**, a method for low-resource text classification that applies curriculum-scheduled augmentation during intermediate contrastive training. Starting from a pre-trained BERT-base encoder, CurCon adapts representations on unlabelled target-domain text by progressively unlocking harder augmentation operators (token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation) before standard fine-tuning on limited labelled data (e.g., 500 examples). Across four classification benchmarks (SST-2, AG News, TREC, SUBJ), CurCon shows an average gain of +1.1 points over CERT and +0.8 points over an uncurriculumed mixture of the same augmentations.

---

### 2. Strengths
- **Clear Motivation and Structure:** The paper is well-written, logically structured, and easy to follow. The problem setup and pipeline are clearly described.
- **Ablation Studies:** The inclusion of an ablation table dissecting the curriculum schedule (including a reversed curriculum baseline and an $L=0$ fixed mixture) directly tests the core hypothesis.
- **Reporting Practices:** The authors report mean and standard deviation over five random seeds, providing visibility into seed variance in low-resource regimes.

---

### 3. Weaknesses & Areas for Improvement

1. **Unfair Hyperparameter Tuning across Baselines:**
   - In Section 4, the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."*
   - In low-resource settings, intermediate contrastive learning and fine-tuning are notoriously sensitive to temperature, learning rate, and batch size. Tuning 48 configurations for CurCon while running CERT, SimCSE, and UDA on out-of-the-box paper defaults introduces a significant evaluation bias. Baselines must receive comparable tuning budgets on the validation set.

2. **Heuristic Hardness Assumption Without Justification:**
   - The ordering of augmentations (token dropout $<$ WordNet synonym replacement $<$ span deletion $<$ back-translation) is asserted purely on intuition. The paper does not provide empirical validation (e.g., measuring alignment/uniformity, representation drift, or mutual information loss) to substantiate that these operators strictly represent monotonically increasing difficulty.

3. **Marginal Incremental Gains:**
   - Table 2 shows that a fixed mixture of all four operators ($L=0$) achieves an average accuracy of 88.1%, while CurCon achieves 88.9% (a difference of only 0.8%). On several individual benchmarks (e.g., TREC: 90.8 ± 0.9 vs. CERT: 90.2 ± 0.7), the performance gains fall within overlapping error margins.

4. **Missing Modern Low-Resource Baselines:**
   - Intermediate contrastive training of 20,000 steps with German back-translation on a target dataset is computationally non-trivial. The paper compares only against older encoder-based semi-supervised methods (UDA, CERT) and omits strong, parameter-efficient contemporary few-shot approaches (e.g., prompt-based fine-tuning like SetFit or LM-BFF).

5. **Discretization Artifacts in the Curriculum Formulation:**
   - The curriculum introduces operators at hard thresholds ($c(t) \in \{0.25, 0.5, 0.75\}$) and samples uniformly from available operators. Consequently, even at $c(t) \ge 0.75$, the weakest augmentation (token dropout) is still sampled 25% of the time. This constitutes an *expanding candidate pool* rather than a true transition from easy to hard instances.

---

### 4. Criterion Scores

- **Soundness: 62 / 100**
  - *Evaluation:* The core experiments are controlled with multiple seeds and proper ablations, but the baseline tuning protocol is fundamentally asymmetric (48-run grid search for the proposed method vs. literature defaults for baselines), which undermines the validity of the reported margins.

- **Novelty: 58 / 100**
  - *Evaluation:* The idea of curriculum learning applied to contrastive augmentations is well-established in computer vision. Transferring this to NLP via four standard heuristic text augmentations in an intermediate stage is an incremental combination of known components (CERT + standard text augmentations + linear pacing).

- **Significance: 60 / 100**
  - *Evaluation:* Low-resource classification is practically relevant, but the modest +0.8 gain over a static mixture, coupled with the computational cost of pre-computing back-translations and running 20k contrastive steps, limits practical adoption compared to simpler data augmentation or prompt-based paradigms.

- **Clarity: 88 / 100**
  - *Evaluation:* The paper is written with high clarity, precise phrasing, concise descriptions, and well-organized experimental tables.

---

### 5. Final Score & Recommendation

- **Average Score:** **67.0 / 100**
- **Recommendation:** **Reject** (Borderline Reject)

**Summary for Decision:** While CurCon presents a clean and intuitive framework with solid writing and thoughtful ablations, the unequal hyperparameter tuning budget between the proposed method and the baselines weakens the empirical claims. Addressing baseline tuning fairness, validating the hardness ranking empirically, and comparing against modern low-resource paradigms (e.g., SetFit) would significantly strengthen the paper for resubmission.