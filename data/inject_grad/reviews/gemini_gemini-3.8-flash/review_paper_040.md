### Paper Review

---

### Summary
The paper proposes **CurCon**, a method for low-resource text classification that applies a curriculum schedule to contrastive intermediate training. Building on CERT, the authors introduce four data augmentations of presumed increasing difficulty (token dropout, synonym replacement, span deletion, and back-translation) and gradually make stronger augmentations available over the course of contrastive pre-training. Evaluating on four standard benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples and a BERT-base encoder, the authors report modest improvements over baselines such as standard fine-tuning, UDA, SimCSE, and CERT.

---

### Strengths

1. **Clear and Structured Presentation:** The paper is well-organized, concise, and easy to follow. The method pipeline, equations, and experimental setups are clearly communicated.
2. **Relevant Problem Setting:** Low-resource text classification remains an important practical problem, and leveraging unlabelled in-domain data without modifying the downstream classification architecture is a pragmatic direction.
3. **Ablation Studies:** The authors conduct relevant sanity checks, including testing a fixed mixture ($L=0$) and a reversed curriculum (hard-to-easy), which demonstrate that the schedule itself provides a measurable difference under their setup.

---

### Weaknesses & Areas for Improvement

1. **Unfair Baseline Hyperparameter Tuning:**
   - In Section 4, the authors state that CurCon’s hyperparameters (learning rate, temperature, curriculum length) were selected via a **grid search over 48 configurations** on the validation set, whereas baselines were simply evaluated using hyperparameters from their original publications. 
   - Hyperparameters for contrastive intermediate training (particularly learning rate, temperature, and batch size) are known to be sensitive across datasets. Giving the proposed method 48 tuning trials while running baselines out-of-the-box introduces significant experimental bias.

2. **Incremental Novelty:**
   - Curriculum learning over augmentation strength has been extensively explored in computer vision contrastive learning and self-supervised learning.
   - Combining existing text augmentations (EDA and back-translation) with an established pipeline (CERT) via a piece-wise threshold schedule is a straightforward combination of known ideas.

3. **Heuristic Difficulty Assumption:**
   - The ordering of augmentations (dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation) is asserted as increasing difficulty, but the paper does not theoretically or empirically quantify representation difficulty (e.g., mutual information loss, edit distance, or representation drift) to substantiate this ranking.

4. **Limited Experimental Scope:**
   - Experiments are restricted to BERT-base on four traditional, relatively short text classification benchmarks. 
   - No comparison is made to modern parameter-efficient tuning (PEFT/LoRA) or prompt-based low-resource methods (e.g., SetFit, PET), which currently define the state of the art in few-shot and low-resource text classification.

5. **Modest Effect Size:**
   - Compared to a simple uniform mixture of all four augmentations without any curriculum ($L=0$), CurCon achieves an average improvement of only 0.8 points (88.9 vs. 88.1). Given the tuning advantage and variance across seeds, this margin is quite narrow.

---

### Quantitative Evaluation

* **Soundness:** **62 / 100**  
  *(Deduction primarily due to hyperparameter tuning disparities between the proposed method and baselines, as well as heuristic assumptions on augmentation difficulty.)*
* **Novelty:** **52 / 100**  
  *(Incremental adaptation of vision curriculum augmentation concepts to standard NLP contrastive pipelines.)*
* **Significance:** **56 / 100**  
  *(Narrow evaluation scope focused on BERT-base; marginal gains over non-curriculum multi-augmentation baseline; missing comparisons to modern few-shot paradigms.)*
* **Clarity:** **88 / 100**  
  *(Writing is clean, concise, well-structured, and easy to read.)*

**Final Average Score:** **64.5 / 100**

---

### Final Recommendation

**Recommendation:** **Reject**  
*(While the paper is clearly written, the methodological novelty is incremental, the empirical gain over a non-curriculum multi-augmentation baseline is marginal (+0.8), and the comparison is confounded by giving the proposed method an extensive validation search that was not afforded to the baselines. An evaluation against modern low-resource baselines and a fair hyperparameter protocol are necessary to support publication.)*