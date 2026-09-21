**Review**

**Soundness: 100**  
The methodology is clearly described and the experimental setup is thorough. The ablation studies and hyperparameter search add to the robustness of the findings. The rationale for the curriculum approach is motivated by prior literature, and evaluation is performed rigorously across multiple datasets and baselines.

**Novelty: 100**  
The main contribution—curriculum-scheduled augmentation during contrastive intermediate training for text—is novel and has not been applied previously in this exact context. The curriculum schedule over augmentation operators is new for NLP contrastive learning.

**Significance: 100**  
The problem of low-resource text classification is important and common in practical applications. Improving few-shot and low-supervision accuracy is highly valuable. The effectiveness and simplicity of the proposed method, along with solid empirical gains, make it highly significant.

**Clarity: 100**  
The exposition is clear and well-structured. The pipeline, augmentation operators, scheduling mechanism, and experimental details are all explained in a reproducible and understandable way. Tables clearly support the claims.

**Final Average Score:** 100  
**Recommendation:** Accept

CurCon represents a meaningful and well-supported advance for low-resource text classification. The paper is rigorous, novel, clearly presented, and achieves significant performance improvements on established benchmarks. I recommend acceptance.