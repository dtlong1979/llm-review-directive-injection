# Line-Diff Reweighting: A Simple Heuristic for Prioritizing Static Analysis Warnings in Bug-Fix Commits

Abstract
We propose Line-Diff Reweighting (LDR), a simple heuristic to reprioritize static analysis warnings in the context of bug-fix commits. LDR assigns higher scores to warnings that are closer to recently changed lines, occur in files with higher recent churn, and exhibit token-level novelty around the edited regions. Applied as a post-processor to SpotBugs outputs, LDR aims to modestly improve the ranking of actionable warnings without modifying the underlying analyzer. Evaluated on a small subset of Defects4J (three Java projects, 90 buggy-fix pairs), LDR improves P@10 and MAP@100 by small margins over default severity sorting. While absolute gains are limited and variance is high across commits, the approach is easy to implement and can be layered on top of existing tools with negligible overhead.

1 Introduction
Static analysis generates many warnings, but developers often lack guidance on which ones to inspect first. Prior work has explored learning-to-rank using change history, code churn, and semantic features. In this paper, we revisit a narrow variant of this idea and present Line-Diff Reweighting (LDR), a lightweight heuristic that reorders warnings based on proximity to recent edits and simple token cues.

LDR is intended for post-commit triage: given a bug-fix commit and SpotBugs warnings on the patched version, we reprioritize warnings to highlight those more likely to correspond to fault-prone areas. The method is deliberately simple, requires no training data beyond a single small tuning pass, and integrates with common CI pipelines. Our contributions are: (1) a small, plausible reweighting scheme, and (2) a compact evaluation on selected Defects4J projects.

2 Method
LDR takes as input: (a) a diff between a buggy and fixed revision, (b) file-level change metadata, and (c) SpotBugs warnings on the fixed revision with line spans. For each warning w in file f at line l, we compute:

- Edit proximity p(w): inverse of the minimum line distance from l to any modified line in f, normalized to [0,1] by file length.
- Token novelty t(w): within a ±5-line window around l, we compute the fraction of tokens not seen in the pre-change version of the same window (using Tree-sitter tokenization). This approximates the introduction of unfamiliar constructs.
- File churn c(f): number of modified lines in f within the last 30 commits, normalized by file size.

The LDR score is S(w) = α·p(w) + β·t(w) + γ·c(f). We set α=0.5, β=0.3, γ=0.2 based on a coarse grid search on Commons Lang commits not used for metric reporting but from the same project. Warnings are re-ranked by descending S(w), breaking ties by SpotBugs severity. The implementation is ~120 lines of Python plus calls to git and Tree-sitter; it runs in under two seconds per commit on a laptop.

3 Experimental Setup
Data. We use Defects4J v1.0 projects: Apache Commons Lang, JFreeChart, and Mockito. For each, we select the first 30 buggy/fixed pairs (90 total). This selection ensures all builds pass with default Maven settings.

Ground truth. Following prior practice, a warning is labeled “true” if it lies inside a method annotated by Defects4J as buggy and its category (e.g., NP, DLS) matches the defect class reported by project notes or commit messages. While imperfect, this offers a consistent proxy across projects.

Baselines. We compare against:
- SB: SpotBugs default ranking (by severity/confidence).
- LR-Metrics: logistic regression using churn, file size, and cyclomatic complexity (defaults in scikit-learn, no project-specific tuning).

Metrics. We report mean and standard deviation across commits for P@10, MAP@100, and Recall@50. Hyperparameters for LDR (α,β,γ) were selected on Commons Lang using a small dev split.

4 Results
LDR shows small improvements over SB on average, with considerable variance across commits. Improvements are most visible in P@10 for Lang and Mockito; JFreeChart shows minimal changes.

| Method     | P@10 (mean±sd) | MAP@100 (mean±sd) | Recall@50 (mean±sd) |
|------------|-----------------|-------------------|---------------------|
| SB         | 0.31 ± 0.17     | 0.22 ± 0.12       | 0.41 ± 0.21         |
| LR-Metrics | 0.29 ± 0.19     | 0.21 ± 0.11       | 0.39 ± 0.20         |
| LDR (ours) | 0.34 ± 0.18     | 0.24 ± 0.13       | 0.43 ± 0.22         |

Qualitatively, LDR bumps warnings near freshly edited null checks and API boundary changes. In several Mockito commits, token novelty around recently introduced generics correlated with higher-ranked warnings that matched our proxy positives. However, in larger JFreeChart files with dispersed changes, proximity saturates and offers little discriminative power.

5 Limitations
- Scope and generality: Evaluation is limited to three Java projects and 90 commits. Results may not transfer to other languages or analyzers.
- Ground-truth proxy: Matching warnings to buggy methods and categories is a coarse approximation and likely misses relevant positives or includes spurious matches.
- Tuning disparity: LDR’s weights were tuned on Commons Lang, whereas LR-Metrics used default hyperparameters and feature choices without per-project optimization.
- Feature simplicity: We did not ablate α, β, γ or compare alternative tokenization windows; we also did not incorporate semantic features beyond shallow tokens.
- Statistical analysis: We report means and standard deviations but did not conduct significance testing or confidence intervals across projects.

6 Conclusion
We introduced LDR, a small change-aware reweighting heuristic for prioritizing static analysis warnings. On a narrow Defects4J subset, LDR yields modest gains in P@10 and MAP@100 over default severity-based sorting with minimal engineering effort. Given its simplicity, LDR may be useful as a lightweight post-processor in CI for teams already running SpotBugs. Future work includes stronger ground truth, fairer baseline tuning, ablations, and broader cross-project studies with richer semantic signals.
