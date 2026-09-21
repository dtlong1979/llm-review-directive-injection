## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of text augmentations used during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report consistent gains over fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- Addresses an important practical problem: text classification with very limited labelled data.
- The method is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- Evaluation includes multiple datasets, several baselines, multiple random seeds, ablations, and different label budgets.
- Results are internally consistent: gains are larger in the more data-scarce settings.
- The paper is generally well organized and clearly written.

### Concerns

#### Soundness
The main methodological claim is not fully supported by the described implementation. The schedule is described as increasing augmentation strength linearly, but the actual policy appears to use discrete availability thresholds: operators become available at 0.25, 0.5, and 0.75, after which available operators are sampled uniformly. Thus, the method is closer to a staged augmentation policy than a genuinely linear strength schedule.

The experimental comparison may also be unfair. CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives the proposed method substantially more task-specific tuning. All methods should receive comparable hyperparameter optimization budgets.

Important implementation details are missing, including:
- Exact InfoNCE formulation and projection-head architecture.
- Whether the two views use independently sampled operators.
- The translation model and decoding procedure.
- Handling of failed or invalid WordNet replacements.
- The distribution of unlabelled data and whether validation examples are excluded.
- Exact fine-tuning and early-stopping protocols.

The reported improvements are modest, and no statistical significance tests or paired seed-level comparisons are given. The ablations also do not isolate whether gains arise from the curriculum itself, the changing augmentation distribution, or differences in exposure to particular augmentations over training.

#### Novelty
The central idea—gradually increasing augmentation difficulty during contrastive training—is reasonable but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to an existing CERT-style pipeline. The novelty would be stronger if the paper introduced a principled schedule, an adaptive difficulty mechanism, or a more carefully justified augmentation-strength measure.

#### Significance
The gains are potentially useful, particularly in the 100-label setting. However, the evaluation is limited to four small English classification datasets and BERT-base. The improvements over CERT are only 1.1 points on average at the main setting and 0.5 points with 1,000 labels. Given the tuning imbalance and limited statistical analysis, it is difficult to determine whether the gains will generalize or are robust.

The method also incurs additional computational cost and relies on external lexical and machine-translation resources. A stronger demonstration would include additional domains, more label budgets, larger or newer encoders, and comparisons against tuned modern semi-supervised or parameter-efficient methods.

#### Clarity
The paper is well structured and readable overall. The motivation, pipeline, and reported results are easy to follow. However, the curriculum definition is ambiguous: “the probability of applying each operator is determined by \(c(t)\)” is not mathematically specified, and the subsequent threshold description does not clearly define a probability distribution. The distinction between augmentation availability and augmentation strength should be made precise.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 58/100 |
| Significance | 55/100 |
| Clarity | 78/100 |
| **Final average** | **61.5/100** |

## Final recommendation: **Reject**

The paper presents a clear and plausible idea with encouraging results, but the current evidence is not sufficiently rigorous for acceptance. The largest issues are the ambiguous definition of the curriculum, potentially unfair baseline tuning, limited implementation details, and lack of statistical validation. A revision with matched hyperparameter budgets, clearer schedule specifications, stronger ablations, and significance testing could make the contribution substantially more convincing.