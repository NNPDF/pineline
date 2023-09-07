import json
from pathlib import Path

import lhapdf
import numpy as np
import yadism
import yaml

root = Path(__file__).parent

PINECARDS = root / "pinecards"
DATASET = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"
THEORIES = root / "theories"

RESULTS = Path("./master_results")
RESULTS.mkdir(exist_ok=True, parents=True)

PDF = "221012-01-rs-nnpdf40_baseline_repeat_nf4"


def load(dataset):
    theory = yaml.safe_load((THEORIES / "400.yaml").read_text())
    observables = yaml.safe_load((PINECARDS / dataset / "observable.yaml").read_text())

    return theory, observables


def patch(theory, observables):
    #  mb2 = theory["mb"] ** 2
    #  mc2 = theory["mc"] ** 2

    del observables["observables"]["XSHERANCAVG_charm"]
    observables["observables"]["F2_charm"] = []
    # for qq in np.geomspace(mc2,16*mb2,10):
    qq = 5.0
    for xx in np.geomspace(5e-7, 1, 10):
        observables["observables"]["F2_charm"].append({"Q2": qq, "x": xx})

    # These are needed but for some reason not present in the theory
    hfl = "cbt"
    for fl in hfl:
        theory[f"kDIS{fl}Thr"] = 1.0

    # theory["TMC"] = 0
    # observables["prDIS"] = "NC"
    # observables["IC"] = 0

    # theory[f"kDISbThr"] = 4.0
    theory["kbThr"] = 4.0

    # theory["FONLLParts"] = "full"
    # theory["FNS"] = "FONLL-A"
    # theory["NfFF"] = 3
    # theory["PTO"] = 1


def run(theory, observables, pdfname):
    pdf = lhapdf.mkPDF(pdfname)
    values = yadism.run_yadism(theory, observables)
    values = values.apply_pdf(pdf)

    out = []
    for obs, kinresults in values.items():
        for i, kinpoint in enumerate(kinresults):
            out.append([values[obs][i][f] for f in ("result", "x", "Q2")])


def dump(out, results):
    (results / "{DATASET}.json").write_text(json.dumps(out))
