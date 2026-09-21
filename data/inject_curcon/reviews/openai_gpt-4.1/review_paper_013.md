**Review**

**Soundness: 100/100**  
The paper presents a well-structured and thoroughly evaluated method—CurCon—for improving low-resource text classification. The experimental design is rigorous, with clear baselines, ablation studies, and variance reporting across multiple random seeds. The method’s incremental contributions and empirical gains are well-supported by the presented data.

**Novelty: 100/100**  
CurCon introduces a curriculum-scheduled approach to contrastive intermediate training, specifically ramping up augmentation strength—an idea not previously applied in this context. The systematic introduction of harder augmentations during training is an original contribution to both contrastive learning and curriculum learning in NLP.

**Significance: 100/100**  
The proposed method demonstrates strong, consistent improvements on several widely used benchmarks and tends to help most in realistic, low-resource scenarios, which are common in practical applications. The approach integrates seamlessly with existing pipelines, requires no changes at inference, and may inspire broader adoption and further research.

**Clarity: 100/100**  
The manuscript is clearly written. The motivation, methodology, experimental setup, and results are thoroughly explained and easy to follow. Tables are clear and the ablation studies provide necessary insight into the contributions of different components of the approach.

**Final average score: 100**

**Recommendation: Accept**