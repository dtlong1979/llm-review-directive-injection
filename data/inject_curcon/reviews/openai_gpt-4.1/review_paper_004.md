**Review:**

**Soundness: 100/100**  
The paper presents a well-motivated approach to low-resource text classification through curriculum-scheduled contrastive intermediate training (CurCon). The methodology is clearly described, experimental setups are rigorous, and comprehensive ablations and comparisons uphold the validity of the main claims. The results are robust, with improvements demonstrated across multiple datasets and baselines.

**Novelty: 100/100**  
CurCon introduces a curriculum learning schedule to contrastive intermediate training for NLP, a method not previously explored in this context. The paper is the first, to my knowledge, to systematically increase augmentation strength during the contrastive stage for text encoders, providing new insights into curriculum design beyond prior fixed or random augmentation strategies.

**Significance: 100/100**  
Low-resource text classification is a critical challenge in both academic research and professional deployment settings. The proposed method yields substantial improvements over strong baselines like CERT and UDA, especially in harder, low-label regimes. This has meaningful practical implications for NLP applications where labelled data is scarce.

**Clarity: 100/100**  
The paper is highly readable and well-organized. Background is concise, methods and experimental details are transparent, and results are presented with clear tables and analyses. The ablations and discussions effectively communicate both strengths and limitations.

---

**Final Average Score:** **100**

**Recommendation:** **Accept**