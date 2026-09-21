## Review

### Summary

The paper proposes CurCon, a curriculum for contrastive intermediate training in which augmentation strength increases over training. The idea is to begin with token dropout and progressively introduce synonym replacement, span deletion, and back-translation before fine-tuning on a small labelled set. Experiments on four classification datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data in low-resource classification.
- The proposed method is simple and easy to integrate into an existing CERT-style pipeline.
- The evaluation includes multiple datasets, several baselines, multiple random seeds, and an ablation of the curriculum direction.
- The results are internally consistent with the hypothesis that curriculum scheduling is more useful in lower-label regimes.
- The paper is generally well organized and readable.

### Concerns

#### 1. The method is not specified sufficiently precisely

The curriculum definition is incomplete and partly inconsistent:

- The paper defines \(c(t)=\min(1,t/L)\), but this is undefined for \(L=0\), despite using \(L=0\) as the fixed-mixture ablation.
- It states that “the probability of applying each operator is determined by \(c(t)\),” but then only specifies threshold-based availability and uniform sampling among available operators. These are different policies and do not fully define the probability distribution.
- It is unclear whether each of the two contrastive views receives an independently sampled operator, whether operators can be composed, and whether token dropout is always sampled or merely always eligible.
- The curriculum length is tuned, but the selected values and the search range are not reported.
- The claimed ordering of augmentation strength is not clearly justified. Synonym replacement, span deletion, and back-translation can have highly variable semantic and linguistic effects, and “strength” is not measured.

These omissions make the method difficult to reproduce and weaken the interpretation of the ablations.

#### 2. Baseline comparison may be unfair

CurCon’s learning rate, temperature, and curriculum length are selected through a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This is not a controlled comparison, especially in a low-resource setting where performance is sensitive to optimization choices. At minimum, all methods should receive comparable tuning budgets, or the paper should report both published settings and equally tuned settings.

The paper also does not provide enough implementation detail for UDA, CERT, and SimCSE, including their exact augmentation policies, training duration, batch sizes, projection heads, and tuning procedures. It is therefore difficult to determine whether the comparisons are genuinely like-for-like.

#### 3. Statistical evidence is limited

The results report means and standard deviations over five seeds, but no confidence intervals or paired significance tests are provided. The claimed curriculum gain is only 0.8 percentage points over the fixed mixture, and the gains over CERT are 1.1 points on average. Given the small number of seeds and the use of validation-set tuning, the paper should establish whether these differences are statistically reliable.

The ablation table reports only averages, hiding dataset-level variation. Since the core claim concerns the curriculum itself, per-dataset ablation results would be important.

#### 4. Experimental scope is narrow

The method is evaluated only on four short English classification datasets and one encoder family. This is acceptable for an initial study, but the claims should be correspondingly modest. In particular:

- The datasets are relatively standard and may not represent realistic domain shift or difficult low-resource deployment conditions.
- No experiments test different unlabeled-data quantities.
- No comparison is made with simpler alternatives, such as a two-stage schedule, random augmentation scheduling, cosine scheduling, or a tuned fixed augmentation mixture.
- There is no analysis of whether the gains come from the curriculum or simply from exposing the model to a different augmentation distribution or more useful augmentations.

The fixed-mixture ablation is helpful but does not fully isolate these possibilities.

#### 5. Some claims need stronger support

The statement that gains are “largest when fewer labelled examples are available” is supported by only three label budgets and two methods. It would be more convincing with repeated trials, uncertainty estimates, and perhaps a broader range of label counts.

The cost analysis is also underspecified. Since CERT itself uses back-translation, the relevant comparison should report total preprocessing cost, storage cost, wall-clock time, and contrastive-stage time for all methods. It is unclear whether synonym replacement and span deletion are actually performed online for both views and how much of the reported 12% overhead is attributable to each operator.

### Novelty

The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but the conceptual novelty is moderate. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to a CERT-like text contrastive-training pipeline. The contribution is primarily a straightforward combination and empirical validation rather than a substantially new contrastive objective or principled curriculum mechanism.

### Significance

The problem is important and the reported gains are potentially useful, especially in low-label regimes. However, the absolute improvement over CERT is modest, and the main curriculum-specific gain is only 0.8 points over the fixed mixture. Given the limited datasets, incomplete baseline tuning, and lack of significance testing, the evidence is not yet strong enough to establish broad practical significance.

### Clarity

The paper is clearly structured and mostly easy to follow. The tables and high-level training pipeline are understandable. Clarity is reduced by the ambiguous augmentation probabilities, the undefined \(L=0\) formulation, missing hyperparameter details, and insufficient description of baseline implementations.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 55/100 |
| Significance | 55/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{48+55+55+78}{4} = 59.0
\]

## Final recommendation: **Reject**

The paper presents a plausible and clearly motivated idea with promising preliminary results, but the current empirical evidence and methodological specification are not sufficiently rigorous. A substantially revised version should precisely define the schedule, tune baselines fairly, report stronger statistical analysis, include more informative ablations, and clarify data, preprocessing, and computational-cost details.