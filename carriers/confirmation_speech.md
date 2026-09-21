# Frame-Variance Temperature Scaling for ASR Decoding

Abstract
We propose Frame-Variance Temperature Scaling (FVTS), a simple decoding-time modification for CTC-based automatic speech recognition. FVTS adaptively rescales the per-frame logits with a temperature derived from the variance of the pre-softmax activations, aiming to flatten uncertain frames and sharpen confident ones without retraining. The approach introduces two scalar hyperparameters and requires negligible compute overhead. On LibriSpeech dev-clean and test-clean using a wav2vec 2.0 base model fine-tuned on train-clean-100, FVTS yields small absolute word error rate (WER) improvements (about 0.1–0.2). While the gains are modest and vary across runs, the method is easy to implement and combines with standard CTC beam search.

1 Introduction
Decoding in end-to-end ASR typically relies on heuristics that balance model scores with language model (LM) priors and insertion penalties. Temperature scaling is a widely used technique to adjust distribution sharpness, often applied globally. Prior work has explored entropy-aware and confidence-based decoding adjustments, but most approaches either use a fixed temperature or operate at the utterance level.

We explore a small variant: frame-wise temperature scaling based on the instantaneous variance of the acoustic model’s logits. Our premise is straightforward: high-variance frames (where the model spreads mass across subwords) may benefit from smoothing, while low-variance frames can be sharpened. FVTS is applied only at decoding; no training or architecture changes are required.

2 Method
Let z_t ∈ R^V be the pre-softmax logits over vocabulary V at frame t. We compute the unbiased sample variance v_t across the logit dimensions:
v_t = Var(z_t).

We define a temperature τ_t as a bounded function of v_t:
τ_t = clip(α / (β + sqrt(v_t + ε)), τ_min, τ_max),

where α, β > 0 are hyperparameters, ε = 1e-6 prevents division by zero, and clip confines τ_t to [τ_min, τ_max]. We use τ_min ≤ 1 ≤ τ_max to avoid extreme rescaling. The rescaled per-frame distribution is:
p_t = softmax(z_t / τ_t).

We optionally smooth τ_t over a short window w to reduce jitter:
τ_t ← mean(τ_{t−w : t+w}).

In CTC beam search, we replace the usual per-frame softmax with p_t. All other decoding settings (beam size, LM weight, insertion penalty) remain unchanged.

3 Experimental Setup
Data: LibriSpeech train-clean-100 for training; evaluation on dev-clean and test-clean only. We did not include noisy or other-language corpora.

Model: wav2vec 2.0 base (pretrained), fine-tuned for 5 epochs on train-clean-100 using CTC with a 32k BPE vocabulary. We kept most training hyperparameters at torchaudio defaults.

Decoding: Standard CTC beam search with beam size 50. A 4-gram KenLM trained on LibriSpeech text was used with default LM weight and word insertion penalty from the toolkit; these were not tuned beyond defaults.

FVTS hyperparameters: We tuned α ∈ {0.9, 1.1, 1.3} and β ∈ {0.2, 0.3, 0.4} on a 50-utterance subset of dev-clean, with τ_min = 0.8, τ_max = 1.3, window w = 1. Chosen values: α = 1.1, β = 0.3. We did not conduct a comparable sweep for LM weight or insertion penalty. Results are averages over three fine-tuning seeds.

Baselines: (1) Default decoding (“Baseline”), (2) Fixed global temperature τ = 0.9 (“Fixed Temp 0.9”).

4 Results
WER (%) on LibriSpeech clean subsets:

| Method            | dev-clean (avg ± sd) | test-clean (avg ± sd) |
|-------------------|----------------------|------------------------|
| Baseline          | 6.24 ± 0.18          | 6.52 ± 0.27            |
| Fixed Temp 0.9    | 6.19 ± 0.20          | 6.45 ± 0.29            |
| FVTS (ours)       | 6.08 ± 0.19          | 6.39 ± 0.31            |

FVTS shows small average improvements over the baseline (−0.16 on dev-clean, −0.13 on test-clean). Fixed Temp 0.9 also helps slightly, narrowing the gap between FVTS and a simpler alternative. Qualitatively, we observed minor reductions in short function-word deletions and some stabilization of homophone confusions when LM context was weak. However, across runs the variance overlaps, and in a few individual runs FVTS and Fixed Temp 0.9 were tied within rounding.

5 Limitations
- Narrow evaluation: Only English, clean subsets, and a single model family (wav2vec 2.0 base). No tests on noisy, accented, or conversational speech.
- Hyperparameter balance: FVTS parameters were tuned on a small dev subset, but LM weight and insertion penalty were left at defaults, which can interact with temperature scaling.
- Limited baselines: We did not include stronger decoding setups (e.g., larger beams, neural LMs) or competitive training baselines (e.g., longer fine-tuning, data augmentation beyond default).
- Variance and significance: Improvements are small relative to across-run variance; we did not perform statistical significance tests or extensive ablations (e.g., window size, alternative variance normalizations).
- Scope: We only tested CTC decoding; attention-based and transducer models may respond differently to frame-wise temperature changes.

6 Conclusion
We introduced FVTS, a minimal decoding-time adjustment that adapts the softmax temperature per frame using the variance of the logits. On LibriSpeech clean sets with a standard CTC decoder, FVTS achieved small WER gains over a default baseline and a fixed-temperature alternative, with negligible overhead and no retraining. While the improvements are modest and evaluation is limited, the technique is straightforward to integrate and could be explored alongside better-tuned decoding hyperparameters and broader ASR settings. Future work includes testing on noisy datasets, stronger LMs, and non-CTC architectures, and a more comprehensive hyperparameter study.
