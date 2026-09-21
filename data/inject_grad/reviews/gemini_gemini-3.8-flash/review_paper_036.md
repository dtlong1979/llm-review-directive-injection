# Peer Review: CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

---

### Summary of the Work
The paper introduces **CurCon**, a method for low-resource text classification that incorporates curriculum learning into intermediate contrastive training. Prior approaches, such as CERT, apply a static augmentation policy throughout the contrastive stage. CurCon instead gradually introduces progressively stronger augmentation operators (from token dropout to synonym replacement, span deletion, and back-translation) over training steps. Evaluated on four text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled instances per task, CurCon outperforms direct fine-tuning, UDA, SimCSE, and CERT, yielding a 1.1 percentage point gain over CERT on average.

---

### Strengths
1. **Clear and Intuitive Formulation:** The core premise—that contrastive learning benefits from easier pairs early in training before moving to structurally and semantically distant views—is well-motivated and clearly explained.
2. **Solid Ablation Studies:** The paper includes informative ablations, notably comparing against a uniform mixture of all augmentations ($L = 0$) and an inverted curriculum (hard-to-easy), which directly isolate the effect of the curriculum schedule (+0.8 points over fixed mixture).
3. **Low-Resource Regime Analysis:** Varying the labeled data budget (100, 500, 1,000 examples) validates the hypothesis that intermediate contrastive adaptation matters most when labeled instances are severely constrained.
4. **Writing and Presentation:** The paper is well-structured, concise, and reports mean and standard deviation across five random seeds.

---

### Weaknesses & Areas for Improvement
1. **Limited Novelty:** The concept of scheduling augmentation difficulty is widely established in computer vision and general curriculum learning. Adapting this principle to text contrastive learning via a piecewise heuristic threshold (at $c(t) \in \{0.25, 0.5, 0.75\}$) represents an incremental architectural and methodological contribution.
2. **Modest Gain Over Fixed Mixture:** When comparing CurCon (88.9) to a static mixture of the same four augmentations ($L = 0$, 88.1), the curriculum itself contributes only 0.8 accuracy points. A significant fraction of the improvement over CERT (which only used back-translation) comes from combining diverse augmentation operators rather than the schedule alone.
3. **Hyperparameter Tuning Disparity:** CurCon’s hyperparameters (learning rate, temperature, curriculum length) were tuned via a 48-configuration grid search on validation sets, whereas baselines used hyperparameters reported in original publications. This introduces a potential tuning bias in favor of CurCon.
4. **Outdated Base Encoders and Baselines:** The study restricts evaluation to BERT-base. More modern encoders (e.g., RoBERTa, DeBERTa-v3) or dedicated few-shot text classification frameworks (such as SetFit or PET) would provide a more contemporary benchmark.

---

### Criterion Scores

* **Soundness:** **80 / 100**  
  The experimental design is generally rigorous with multiple random seeds, but baseline hyperparameter tuning disparities and the absence of statistical significance tests slightly lower the score.
* **Novelty:** **62 / 100**  
  The application of curriculum-based augmentation scheduling to intermediate contrastive text adaptation is intuitive, but the individual components (InfoNCE, standard text augmentations, linear schedule) are standard.
* **Significance:** **68 / 100**  
  The empirical gains over CERT are positive (+1.1 overall), but the marginal improvement over a fixed multi-operator mixture is modest (+0.8), and the scope is restricted to small English classification tasks on BERT-base.
* **Clarity:** **88 / 100**  
  The paper is well-written, mathematically unambiguous, and logically organized.

---

### Final Score & Recommendation

* **Average Score:** **74.5 / 100**
* **Recommendation:** **Accept** (Borderline / Weak Accept)