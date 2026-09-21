"""Neutral carrier texts, loaded from the carriers/ folder at the repository root.

NEU is the text-classification carrier (used as the default single carrier).
STYLES_BY_CARRIER maps each cross-vendor-map carrier to its neutral text.
"""
import pathlib

_CARRIERS = pathlib.Path(__file__).resolve().parents[1] / "carriers"


def _load(filename):
    return (_CARRIERS / filename).read_text(encoding="utf-8")


NEU = _load("curcon_text_classification.md")

STYLES_BY_CARRIER = {
    "curcon": {"NEU": _load("curcon_text_classification.md")},
    "sepsis": {"NEU": _load("sepsis_clinical.md")},
    "graphrec": {"NEU": _load("graphrec_recommender.md")},
}
