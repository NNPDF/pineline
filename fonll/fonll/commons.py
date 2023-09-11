import json
from pathlib import Path

import numpy as np
import yaml

THEORIES = "theories"
PINECARDS = "pinecards"
DATASET = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"

PDF = {
    3: "221012-01-rs-nnpdf40_baseline_repeat_nf3",
    4: "221012-01-rs-nnpdf40_baseline_repeat_nf4",
    5: "221012-01-rs-nnpdf40_baseline_repeat_nf5",
}


def load(dataset, root):
    theory = yaml.safe_load((root / THEORIES / "400.yaml").read_text())
    observables = yaml.safe_load(
        (root / PINECARDS / dataset / "observable.yaml").read_text()
    )

    return theory, observables


def patch(theory, observables):
    #  mb2 = theory["mb"] ** 2
    #  mc2 = theory["mc"] ** 2

    del observables["observables"]["XSHERANCAVG_charm"]
    observables["observables"]["F2_charm"] = []
    #  for qq in np.geomspace(mc2, 16 * mb2, 10):
    for qq in np.arange(3.0, 15.0):
        #  qq = 5.0
        #  for xx in np.geomspace(5e-7, 1, 10):
        for xx in np.arange(0.02, 0.8, 0.03):
            observables["observables"]["F2_charm"].append({"Q2": qq, "x": xx})

    # These are needed but for some reason not present in the theory
    hfl = "cbt"
    for fl in hfl:
        theory[f"kDIS{fl}Thr"] = 1.0

    # theory["TMC"] = 0
    # observables["prDIS"] = "NC"
    # observables["IC"] = 0

    # theory["FONLLParts"] = "full"
    # theory["FNS"] = "FONLL-A"
    # theory["NfFF"] = 3
    # theory["PTO"] = 1

    return theory, observables


def dataset(root: Path, subdir: str):
    res = root / "results" / subdir
    res.mkdir(exist_ok=True, parents=True)
    return res / f"{DATASET}.json"


def dump(out, root, subdir):
    (dataset(root, subdir)).write_text(json.dumps(out))
