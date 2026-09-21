## Review

### Scores

| Criterion | Score |
|---|---:|
| **Soundness** | 55/100 |
| **Novelty** | 52/100 |
| **Significance** | 58/100 |
| **Clarity** | 78/100 |
| **Final average** | **60.75/100** |

## Summary

The paper presents CurCon, which applies a progressively stronger augmentation policy during unsupervised contrastive intermediate training before low-resource classification fine-tuning. The empirical results are consistently positive across four datasets, and the paper is generally easy to follow. However, several methodological and experimental details limit confidence in the claimed improvements.

## Strengths

- The problem is relevant: exploiting unlabeled in-domain data for low-resource classification is practically important.
- The method is simple and easy to implement.
- The paper evaluates multiple datasets and random seeds.
- Results are reported with standard deviations for the main table.
- The ablations include fixed augmentation, reversed curriculum, and removal of back-translation.
- The observed trend that gains are larger with fewer labels is plausible and potentially useful.

## Main concerns

### 1. The curriculum is not actually well specified as a continuous linear schedule

The paper defines a linear curriculum level \(c(t)\), but augmentation operators become available only at thresholds 0.25, 0.5, and 0.75. Within each interval, the policy appears unchanged, and after the final threshold the operators are sampled uniformly. Thus, the actual schedule is a sequence of discrete jumps rather than a clearly defined linearly increasing augmentation strength.

Moreover, “token dropout is always available” and the other operators become available at thresholds, but the paper does not specify whether token dropout remains more probable than the newly introduced operators or whether all available operators are sampled uniformly. These choices can materially affect performance.

The definition for \(L=0\), \(c(t)=\min(1,t/L)\), is mathematically undefined. The fixed-mixture interpretation should be stated separately.

### 2. Baseline comparisons may be unfair

CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more task-specific tuning. A fair comparison should either tune all methods under the same budget or report both published and equally tuned baselines.

This issue is especially important because the reported gains over CERT are relatively modest: 1.1 average points overall and 0.5 points at 1,000 labels.

### 3. Statistical evidence is incomplete

Although the main table reports standard deviations, the paper does not provide:

- per-seed results,
- confidence intervals,
- significance tests,
- standard deviations for the ablation and label-budget experiments,
- evidence that the improvements over CERT are statistically reliable.

The ablation claims of 0.8 and 1.3 points may therefore be within normal seed variation. Given the small number of seeds, stronger statistical reporting is needed.

### 4. Important implementation details are missing

The method depends on several choices that are insufficiently described:

- exact definition of positive pairs and whether each view receives independent augmentations;
- projection-head architecture and whether it is discarded before fine-tuning;
- maximum sequence length and truncation behavior;
- details of synonym replacement and handling of unavailable WordNet entries;
- the German translation model and decoding setup;
- whether back-translations are generated once per sentence or multiple times;
- data deduplication and overlap handling;
- UDA and CERT implementation details;
- whether the unlabeled pool includes validation or test-related text.

These details matter for reproducibility and could influence the results substantially.

### 5. The novelty is incremental

The core idea—gradually increasing augmentation difficulty during contrastive training—is reasonable, but it is a relatively straightforward combination of curriculum learning and established contrastive intermediate training. The paper does not sufficiently distinguish CurCon from prior work on augmentation schedules, curriculum contrastive learning, or adaptive augmentation policies.

The contribution would be stronger with comparisons against:

- a continuous augmentation-strength schedule;
- a random schedule;
- schedules based on training loss or representation difficulty;
- independently tuned fixed augmentation policies;
- other curriculum designs with the same total augmentation exposure.

### 6. The causal interpretation of the ablation is limited

The fixed-mixture baseline differs from CurCon not only in ordering but potentially in the distribution of augmentations over training. Therefore, the 0.8-point difference does not isolate curriculum order cleanly. A fair ablation should match the total number and type of augmentations while changing only their temporal ordering.

Similarly, the “reversed curriculum” may be harder to interpret if it changes the effective augmentation distribution or causes early training instability.

### 7. Cost claims are somewhat unclear

The paper states that back-translated views are pre-computed, but also reports a 12% increase due to on-the-fly synonym replacement and span deletion. The computational setup should report preprocessing cost, storage cost, and training-time cost separately. It is also unclear whether CERT uses the same precomputation and batch construction procedures.

## Criterion-specific assessment

### Soundness: 55/100

The overall experimental design is plausible and the results are internally numerically consistent. However, the unfair baseline tuning, incomplete method specification, weak statistical analysis, and ambiguity in the curriculum definition prevent high confidence in the conclusions.

### Novelty: 52/100

The proposed combination is sensible, but the conceptual advance is modest. The paper needs a more comprehensive comparison to existing scheduled or curriculum-based augmentation methods and stronger evidence that the benefit comes specifically from the proposed schedule.

### Significance: 58/100

Low-resource text classification is important, and consistent improvements across four datasets could be practically useful. Nevertheless, the gains are moderate, the evaluation is limited to short English texts and BERT-base, and the reliability of the gains is not established sufficiently.

### Clarity: 78/100

The paper is well organized, readable, and communicates the main idea clearly. Clarity is reduced by ambiguities in the exact augmentation probabilities, curriculum implementation, data splits, baseline tuning, and computational-cost accounting.

## Recommendation

**Reject**

The paper has a clear and potentially useful idea, but the current evidence is not sufficiently rigorous to support acceptance. A revised version should use equally tuned baselines, clarify the schedule mathematically and operationally, report statistical significance for all key comparisons, provide complete implementation details, and include stronger schedule-specific ablations.