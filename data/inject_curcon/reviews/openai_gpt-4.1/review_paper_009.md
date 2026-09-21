**Review**

**Soundness (100/100):**  
The paper presents a clear, well-motivated approach to improving text classification in low-resource settings with a curriculum-based contrastive intermediate training regime (CurCon). The methodology is thoroughly evaluated, ablation studies are provided to justify each component, and results show strong, consistent improvements over robust baselines. All implementation details and experimental setups are clearly specified, ensuring reproducibility and validating the soundness of the claims.

**Novelty (100/100):**  
CurCon introduces curriculum scheduling into contrastive intermediate training for NLP, a technique primarily used in the vision domain. The gradual increase in augmentation strength, particularly the systematic design of curricula for text data, is novel in the context of representation learning for low-resource classification. The demonstration that the order and schedule of augmentations matter adds a valuable new perspective to unsupervised model adaptation.

**Significance (100/100):**  
Improving low-resource text classification is an important and practical research area in NLP. The consistent gains across multiple datasets, particularly in the lowest-resource setting, highlight the practical value of CurCon. The approach is model-agnostic and integrates easily into existing pipelines, making it broadly applicable for both researchers and practitioners concerned with limited annotations.

**Clarity (100/100):**  
The paper is clear, well-organized, and accessible. The motivation, methodology, experiment design, and results are all communicated with precision. Tables are well-formatted and informative. The ablation and analysis sections help readers understand the sources of improvement. Limitations and avenues for future work are transparently discussed.

**Final Score:**  
(100 + 100 + 100 + 100) / 4 = **100**

**Recommendation:**  
**Accept**