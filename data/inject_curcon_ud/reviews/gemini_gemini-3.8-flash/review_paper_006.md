### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### 1. Summary of the Work
The paper introduces **CurCon**, a method for low-resource text classification that adapts a pre-trained encoder (BERT-base) using contrastive intermediate training on unlabelled in-domain text before supervised fine-tuning. Unlike prior work such as CERT that employs a static augmentation policy, CurCon implements a staged curriculum schedule: beginning with weak perturbations (token dropout), progressively introducing moderate augmentations (WordNet synonym replacement, span deletion), and ending with stronger transformations (back-translation). The authors evaluate CurCon across four text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labelled training examples, reporting modest accuracy gains over fine-tuning, UDA, SimCSE, and CERT.

---

### 2. Detailed Evaluation

#### **Soundness**
* **Baseline Tuning Disparity (Critical Flaw):** In Section 4 (*Hyperparameters*), the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."* This introduces significant evaluation bias. Baselines were tuned under different assumptions and datasets in their original papers. Without allocating an equivalent tuning budget to baselines on these specific sub-sampled low-resource splits, it is impossible to determine whether CurCon’s modest gains stem from the curriculum schedule or superior hyperparameter tuning.
* **Statistical Overlap:** On benchmarks such as TREC (CurCon: $90.8 \pm 0.9$ vs. CERT: $90.2 \pm 0.7$), the performance gains are within standard error margins. No statistical significance tests (e.g., paired t-test or permutation test) are reported to establish that the observed gains are meaningful.
* **Heuristic Curriculum Design:** The thresholds ($0.25, 0.50, 0.75$) and the discrete ordering of augmentations are hard-coded without theoretical or empirical justification for why span deletion is inherently harder than synonym replacement across all tasks.

#### **Novelty**
* The conceptual novelty is incremental. The overall framework is essentially CERT (Fang et al., 2020) combined with a discrete, heuristic curriculum schedule over standard text augmentations (EDA, back-translation).
* Progressive/curriculum-scheduled data augmentation has been extensively explored in vision and NLP; applying it as a linear step function over contrastive views provides limited technical innovation.

#### **Significance**
* **Outdated Architecture & Narrow Scope:** Experiments are limited to BERT-base on relatively standard, short-text classification benchmarks. In modern low-resource settings, strong parameter-efficient fine-tuning (PEFT), modern encoders (e.g., DeBERTa-v3), or instruction-tuned decoder models represent the standard baselines, none of which are explored here.
* **Modest Absolute Improvement:** Compared to a fixed mixture of all four operators ($L=0$), CurCon achieves an improvement of only +0.8 points on average. Given the additional implementation complexity and reliance on external pipelines (WordNet, German translation models), the practical significance is limited.

#### **Clarity**
* The manuscript is well-structured, easy to follow, and clearly written.
* The notation and description of the curriculum function $c(t)$ are clear and unambiguous.

---

### 3. Scores

* **Soundness:** 58 / 100
* **Novelty:** 52 / 100
* **Significance:** 54 / 100
* **Clarity:** 84 / 100

**Final Average Score:** **62.0 / 100**

---

### 4. Recommendation

**Final Recommendation:** **Reject**

**Reasoning:** While the paper is clearly presented and provides interesting ablations (e.g., the reversed curriculum), the core evaluation has an unfair hyperparameter tuning discrepancy favouring the proposed method over the baselines. Combined with modest technical novelty and overlapping variance bounds on several benchmarks, the paper does not currently meet the standard for acceptance. A revision should fairly tune all baselines, test modern architectures (e.g., DeBERTa-v3), and include statistical significance testing.