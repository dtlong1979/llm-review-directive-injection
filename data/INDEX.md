# Data index

Each folder holds the model outputs behind one part of the paper.

| Folder | Supports |
|---|---|
| `inject_curcon` | Table 2 (cross-vendor map, text classification carrier) |
| `inject_sepsis` | Table 2 (map, clinical carrier); its `_def` runs support Table 4 |
| `inject_graphrec` | Table 2 (map, recommender carrier); its `_def` runs support Table 4 |
| `inject_extra` | Table 3 (six-field confirmation set) |
| `inject_grad` | Figure 1a and Table 8 (payload phrasing gradient) |
| `inject_lead` | Figure 1b and Table 9 (inline positions) |
| `inject_boundary` | Figure 1b and Table 9 (attached positions); system column of Table 5 |
| `inject_pdf_sub` | Figure 1b and Table 9 (PDF, visible vs invisible text) |
| `inject_para` | Table 10 (matched-paraphrase ablation) |
| `inject_curcon_ud` | Table 5 (user-prompt warning) |
| `inject_curcon_san` | Table 6 (detect-and-delete sanitiser) |
| `inject_curcon_2p` | Table 7 (two-pass bottleneck) |
| `inject_warn_usr` | Section 5.1 (identical warning, user role) |
| `inject_warn_sys` | Section 5.1 (identical warning, system role) |

Within each folder, `reviews/<model>/review_<input>` is the raw output for one call,
`key.csv` gives each input's condition, and `results.csv` aggregates the decisions.
