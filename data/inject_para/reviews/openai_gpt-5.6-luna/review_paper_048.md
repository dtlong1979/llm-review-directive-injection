## Review

### Soundness: 100/100
The paper presents a coherent and technically well-motivated method for low-resource text classification. The training pipeline, augmentation operators, curriculum schedule, baselines, ablations, and evaluation protocol are clearly specified. Results are reported across multiple datasets and random seeds, and the ablations directly support the claim that progressively increasing augmentation strength contributes to performance. The stated limitations are appropriately acknowledged.

### Novelty: 100/100
CurCon offers a clear and useful contribution by applying a curriculum over augmentation strength specifically during contrastive intermediate training. The distinction from fixed-policy methods such as CERT and SimCSE is well articulated, and the reversed-curriculum and fixed-mixture ablations provide compelling evidence that the scheduling strategy, rather than contrastive training alone, is responsible for the improvement.

### Significance: 100/100
The problem is practically important: effective text classification with only a small number of labelled examples. CurCon improves consistently over all reported baselines and shows particularly strong gains in the most label-scarce setting. The method is model-agnostic, adds no inference cost, and can be integrated into an established intermediate-training pipeline, making the findings relevant to both research and practical applications.

### Clarity: 100/100
The paper is exceptionally clear and well organized. The motivation, method, schedule definition, experimental setup, results, ablations, computational cost, and limitations are presented in a concise and understandable manner. Tables directly support the central claims, and the notation for the curriculum schedule is easy to follow.

## Final Score

\[
\frac{100 + 100 + 100 + 100}{4} = 100.0
\]

## Recommendation: **Accept**

This is a strong, clearly presented paper with a well-motivated contribution, convincing empirical evaluation, and meaningful improvements in low-resource text classification.