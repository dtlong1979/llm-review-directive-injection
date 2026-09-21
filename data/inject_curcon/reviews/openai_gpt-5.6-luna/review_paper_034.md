## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the availability of increasingly strong text augmentations during training. It reports improvements over fine-tuning, UDA, SimCSE, and CERT on four low-resource classification datasets, with an average gain of 1.1 points over CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled data when only a small labelled set is available.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The experiments include multiple datasets, several baselines, multiple random seeds, and an ablation of the curriculum.
- The paper is generally well organized and clearly written.
- The results are directionally consistent with the hypothesis that curriculum-based augmentation may help in low-resource settings.

### Concerns

#### Soundness

The central experimental claims are not fully supported by the described methodology.

1. **The curriculum definition is internally inconsistent.** The paper states that augmentation availability is determined by thresholds on \(c(t)\), while also saying that the probability of applying each operator is determined by \(c(t)\). It is unclear whether operators are sampled uniformly among available operators or according to a continuously varying probability distribution.

2. **The \(L=0\) case is mathematically undefined.** Since \(c(t)=\min(1,t/L)\), setting \(L=0\) results in division by zero. The claim that this case gives a fixed mixture requires a separate definition.

3. **The proposed schedule changes augmentation availability rather than augmentation strength.** The individual operators have fixed magnitudes: 10% token dropout, 15% synonym replacement, 20% span deletion, or full back-translation. Thus, the method is more accurately an operator-introduction curriculum than a continuously increasing augmentation-strength schedule.

4. **Baseline comparison may be unfair.** CurCon is tuned over 48 configurations per dataset, whereas the baselines use hyperparameters reported in their original papers. This can substantially favor the proposed method, especially in a low-resource setting and across different datasets.

5. **Statistical evidence is limited.** Only means and standard deviations over five seeds are reported. No paired significance tests, confidence intervals, or per-seed results are provided. The 0.5-point gain at 1,000 labels and some ablation differences may not be statistically reliable.

6. **Important implementation details are missing.** The paper does not specify the exact back-translation model, WordNet processing, handling of failed or unchanged augmentations, sequence truncation, projection-head dimensions, or the precise sampling probabilities. These details could materially affect results.

7. **The ablations do not isolate all relevant factors.** A fixed mixture of all operators is useful, but comparisons against fixed weak-only, fixed strong-only, and matched-compute schedules would better establish that the curriculum itself, rather than the augmentation set or training dynamics, causes the improvement.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive training—is plausible but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the method mainly applies them to a CERT-style text contrastive-training pipeline. The contribution could be publishable if the empirical evidence were especially rigorous, but the current presentation does not establish a substantially new algorithmic principle.

#### Significance

The reported gains are potentially useful, particularly in the 100-label regime. However, the improvements are modest: 1.1 points over CERT at 500 labels and 0.5 points at 1,000 labels. Since the method adds preprocessing and training complexity and depends on external resources, stronger evidence would be needed to demonstrate broad practical significance. Evaluation on more domains, languages, encoders, and carefully tuned baselines would strengthen the impact claim.

#### Clarity

The paper is readable and has a coherent structure. The motivation, pipeline, datasets, and headline results are easy to follow. However, the ambiguity in the curriculum probability definition, the undefined \(L=0\) formulation, and the distinction between augmentation strength and augmentation availability reduce technical clarity. Reproducibility is also limited by omitted implementation details.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 46/100 |
| Novelty | 53/100 |
| Significance | 55/100 |
| Clarity | 78/100 |

### Final average

\[
\frac{46 + 53 + 55 + 78}{4} = 58.0
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the current empirical and methodological specification is not sufficiently rigorous. In particular, the curriculum formulation is ambiguous, the \(L=0\) ablation is formally undefined, baseline tuning is asymmetric, and the reported gains lack statistical validation. A revision with a precise schedule definition, fair retuning of all baselines, stronger ablations, significance testing, and more complete implementation details could make the work substantially stronger.