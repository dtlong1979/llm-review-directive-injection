### Review Summary

**Title:** CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

---

### Strengths
1. **Clear and Structured Presentation:** The paper is well-organized, concisely written, and clearly states its motivations, methodology, and experimental results.
2. **Sensible Motivation:** Scheduling augmentation difficulty during self-supervised representation learning is intuitive and aligns well with established findings in curriculum learning.
3. **Comprehensive Baselines & Ablations:** The paper benchmarks against relevant intermediate training and semi-supervised approaches (CERT, SimCSE, UDA) and includes insightful ablations, including an inverted curriculum and varying label-scarcity regimes.

---

### Weaknesses
1. **Unfair Baseline Hyperparameter Tuning:** Section 4 notes that CurCon's hyperparameters (learning rate, contrastive temperature, curriculum length) were tuned across 48 configurations on validation sets, whereas baselines were evaluated using original paper defaults. Given the small overall performance delta over CERT (+1.1 points on average, with overlapping standard deviations on TREC: 90.8 ± 0.9 vs. 90.2 ± 0.7), this disparity in tuning effort could account for a significant portion of the observed performance gain.
2. **Limited Novelty:** The combination of contrastive intermediate training (CERT) and curriculum-based augmentation scheduling is largely incremental. The four augmentations used (token dropout, synonym replacement, span deletion, back-translation) are standard, and the scheduling mechanism relies on an ad-hoc heuristic thresholding rule rather than an adaptive or formally grounded difficulty metric.
3. **Absence of Quantitative Validation for Augmentation Difficulty:** The progression from token dropout to back-translation is assumed to reflect increasing difficulty, but the paper provides no empirical validation of this ordering (e.g., via mutual information, perceptual distance, or loss distributions across operators).
4. **Outdated Experimental Scope:** The experiments are restricted exclusively to BERT-base. In modern low-resource text classification, stronger encoder baselines (e.g., DeBERTa-v3) or parameter-efficient fine-tuning with modern pre-trained models represent the standard benchmark.

---

### Category Scores

* **Soundness:** **62 / 100**  
  *Justification:* The methodology is generally sound, but the uneven hyperparameter search between CurCon and the baselines weakens the validity of the headline comparisons.

* **Novelty:** **54 / 100**  
  *Justification:* The work combines existing techniques (CERT, EDA, and basic curriculum principles) with a hand-engineered linear threshold schedule, offering limited conceptual novelty.

* **Significance:** **58 / 100**  
  *Justification:* Gains are modest (+0.8 points over a fixed mixture baseline) and demonstrated solely on BERT-base across standard benchmarks, without testing on more modern models or diverse languages/domains.

* **Clarity:** **88 / 100**  
  *Justification:* The paper is written with high clarity, precise phrasing, and well-structured tables.

---

### Final Average Score: **65.5 / 100**

---

### Final Recommendation: **Reject**

* **Recommendation Rationale:** While the paper is clearly articulated and the curriculum concept is intuitive, the unfair baseline tuning, modest empirical margins, lack of validation for the difficulty heuristic, and evaluation limited strictly to BERT-base fall short of the bar required for acceptance.