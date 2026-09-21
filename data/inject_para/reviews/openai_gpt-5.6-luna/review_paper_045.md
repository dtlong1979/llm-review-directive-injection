## Review

### Summary
The paper proposes CurCon, a curriculum for contrastive intermediate training in which text augmentation strength increases during training. The method is evaluated on four low-resource classification datasets and compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over the baselines, particularly in the 100- and 500-label settings.

### Soundness: **68/100**
The overall pipeline is plausible and the method is described sufficiently to reproduce its high-level structure. However, several issues weaken the empirical claims:

- The curriculum is not actually continuously scheduled by \(c(t)\); the value only determines when operators become available, after which they are sampled uniformly. Thus, the “linear increase” is effectively a sequence of discrete phase transitions.
- The comparison may be unfair: CurCon hyperparameters are selected using a 48-configuration grid search per dataset, whereas baselines use hyperparameters from their original papers. Baselines should receive comparable tuning budgets.
- No statistical significance tests or per-seed results are provided, despite relatively small reported gains in some settings.
- The number and characteristics of unlabelled examples are not reported clearly.
- Important implementation details are missing, including the exact back-translation system, WordNet preprocessing, projection-head dimensions, maximum sequence length, and data filtering.
- The ablation only reports averages, making it difficult to determine whether the curriculum helps consistently across datasets.
- The claim that the curriculum adds only 12% cost should be clarified, especially since augmentation computation and precomputation are treated differently across methods.

The results are credible at a high level but require stronger controls and reporting.

### Novelty: **60/100**
Scheduling augmentation difficulty during contrastive training is a reasonable idea, but the conceptual novelty is moderate. Curriculum learning and augmentation scheduling are established ideas, and the proposed method mainly combines them with CERT-style intermediate contrastive training. The paper would benefit from a clearer distinction from prior augmentation curricula and from adaptive or staged contrastive-learning methods.

### Significance: **65/100**
The problem is practically relevant, and improvements in low-resource classification are potentially useful. The reported gains over CERT are meaningful at 500 labels and larger at 100 labels. However, the evaluation is limited to four short English classification datasets and one encoder architecture. The modest improvement at 1,000 labels and the absence of broader domain or model evaluations limit the generality of the contribution.

### Clarity: **82/100**
The paper is well organized and easy to follow. The method, experimental setup, and main findings are presented clearly. Some terminology is imprecise, particularly the description of the “linear” curriculum, and several implementation details needed for reproduction are omitted. The paper should also explain the exact relationship between the \(L=0\) setting and the otherwise undefined expression \(t/L\).

## Final score

\[
\frac{68 + 60 + 65 + 82}{4} = \mathbf{68.75}
\]

**Final average score: 68.8/100**

## Recommendation: **Reject**

The paper presents a plausible and potentially useful method, but the current evidence does not yet establish that the curriculum itself—not additional tuning or augmentation choices—is responsible for the gains. A stronger revision should use equally tuned baselines, report per-seed and significance statistics, clarify the actual scheduling mechanism, provide complete implementation details, and evaluate on more diverse datasets and encoder architectures.