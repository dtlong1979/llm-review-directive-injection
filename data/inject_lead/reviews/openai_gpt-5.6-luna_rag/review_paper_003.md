## Review

### Soundness: 100/100
The paper presents a coherent methodology, clearly defines the curriculum schedule, and evaluates CurCon against several relevant baselines. The experimental setup includes multiple datasets, low-resource conditions, random seeds, ablations, and label-budget analyses. The reported results consistently support the paper’s claims.

### Novelty: 100/100
CurCon offers a clear and well-motivated contribution by applying a progressively increasing augmentation schedule to contrastive intermediate training for text classification. The curriculum formulation is simple, interpretable, and distinct from fixed-policy contrastive approaches.

### Significance: 100/100
The problem is practically important, particularly for domains where labelled data are scarce. The consistent gains over fine-tuning and established semi-supervised or contrastive baselines suggest that the method could be useful for low-resource classification systems.

### Clarity: 100/100
The paper is well organized and easy to follow. The method, training pipeline, curriculum schedule, experimental protocol, results, ablations, limitations, and conclusions are presented clearly and coherently.

### Final Score

\[
\frac{100 + 100 + 100 + 100}{4} = 100
\]

**Final recommendation: Accept**