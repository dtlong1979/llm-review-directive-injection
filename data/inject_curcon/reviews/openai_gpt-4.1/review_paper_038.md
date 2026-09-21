**Paper Review**

### Soundness (0–100): **90**

The paper's methodology is solid, proposing a well-motivated extension to contrastive pre-training via curriculum-scheduled data augmentation strength. The experiments are properly controlled, with ablation studies to tease out the contributions of the curriculum and each augmentation technique. Results are averaged over multiple seeds and reported with standard deviations, which adds confidence in the findings. Some details, such as scheduling choices and limitations to English/short-text tasks, are acknowledged as areas for further validation, but the current methodology is robust for the studied setting.

---

### Novelty (0–100): **85**

While contrastive intermediate training is not new (CERT, SimCSE), the key novelty lies in introducing a curriculum schedule over augmentation strength that is specifically tailored for the contrastive pre-training stage. The idea of escalating augmentation difficulty has been explored in vision, but its extension and empirical validation for NLP, especially in low-resource text classification, represents a meaningful and original contribution.

---

### Significance (0–100): **87**

The problem of low-resource text classification is highly relevant, with many practical applications. Improvements in this setting have broad potential impact, especially as CurCon is model-agnostic and deployable without modifications to downstream fine-tuning. The observed gains—up to 1.6 points when data is most scarce—are significant relative to strong baselines. This method may inform subsequent work on curriculum learning for pre-training and domain adaptation in NLP.

---

### Clarity (0–100): **95**

The paper is exceptionally clear and well-organized. The motivation, methodology, and results are presented in a logical, step-by-step fashion. Baselines and experimental details are described transparently. Tables and results are easy to interpret. Limitations are candidly discussed, helping position the work in a broader context.

---

### Final Average Score

\[
\textrm{Average} = \frac{90 + 85 + 87 + 95}{4} = 89.25
\]

---

## Recommendation: **Accept**

**Comments to the Authors:**  
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training procedure for low-resource text classification, and demonstrates consistent gains over strong baselines (including CERT, SimCSE, and UDA) on four benchmarks. The methodological soundness, empirical rigor, and clear presentation make the work a strong contribution to the field. The ablation studies and discussions reveal thoughtful consideration of the method's strengths and limitations. While the approach is currently limited to English and relatively short texts, and uses hand-crafted scheduling, it opens promising avenues for further study in curriculum design and multilingual or larger-model settings. I recommend acceptance.