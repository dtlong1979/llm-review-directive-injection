# -*- coding: utf-8 -*-
"""Analyse the rigorous DDS validation: Wilson 95% CIs for recall/FP/adaptive per
detector x criterion, and end-to-end decision restoration per reviewer."""
import json, pathlib, math
from collections import defaultdict
OUT = pathlib.Path(r"D:/dev/Promt injection in review papers/experiments/dds_rigor")

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = (z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
    return (round(p, 3), round(max(0, c-h), 3), round(min(1, c+h), 3))

def suiteA():
    rows = json.loads((OUT/"suiteA_rows.json").read_text(encoding="utf-8"))
    agg = defaultdict(lambda: defaultdict(lambda: [0, 0]))  # (det,crit)->set->[caught,total]
    for r in rows:
        a = agg[(r["detector"], r["crit"])][r["set"]]
        a[1] += 1; a[0] += 1 if r["caught"] else 0
    print("== SUITE A: recall / false-positive / adaptive (k/n, Wilson 95% CI) ==")
    print(f"{'detector':26s} {'crit':8s} {'recall':>18s} {'false-pos':>18s} {'adaptive':>18s}")
    for (det, crit) in sorted(agg):
        def cell(setn):
            k, n = agg[(det, crit)][setn]
            p, lo, hi = wilson(k, n)
            return f"{k}/{n} [{lo:.2f},{hi:.2f}]"
        print(f"{det:26s} {crit:8s} {cell('recall'):>18s} {cell('fp'):>18s} {cell('adaptive'):>18s}")

def suiteB():
    p = OUT/"suiteB_rows.json"
    if not p.exists(): print("\n(SuiteB not finished)"); return
    rows = json.loads(p.read_text(encoding="utf-8"))
    print("\n== SUITE B: end-to-end (injected decision -> DDS-sanitised decision) ==")
    byrev = defaultdict(lambda: {"inj_acc":0,"san_acc":0,"san_rej":0,"removed":0,"n":0})
    for r in rows:
        b = byrev[r["reviewer"]]; b["n"] += 1
        b["inj_acc"] += r["inj"] == "accept"
        b["san_acc"] += r["san"] == "accept"
        b["san_rej"] += r["san"] == "reject"
        b["removed"] += bool(r["payload_removed"])
    for rev, b in byrev.items():
        print(f"  {rev:34s} injected Accept {b['inj_acc']}/{b['n']} -> sanitised Accept {b['san_acc']}/{b['n']} "
              f"(Reject {b['san_rej']}/{b['n']}); payload removed {b['removed']}/{b['n']}")

if __name__ == "__main__":
    suiteA(); suiteB()
