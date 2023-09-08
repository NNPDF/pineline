import json

import lhapdf
import yadism
import yaml

THEORIES = "theories"
PINECARDS = "pinecards"
DATASET = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"


def load(dataset, root):
    theory = yaml.safe_load((root / THEORIES / "400.yaml").read_text())
    observables = yaml.safe_load(
        (root / PINECARDS / dataset / "observable.yaml").read_text()
    )

    return theory, observables


def compute(theory, observables, pdfname):
    pdf = lhapdf.mkPDF(pdfname)
    values = yadism.run_yadism(theory, observables)
    values = values.apply_pdf(pdf)

    out = []
    for obs, kinresults in values.items():
        for i, kinpoint in enumerate(kinresults):
            out.append([values[obs][i][f] for f in ("result", "x", "Q2")])

    return out


def dump(out, results):
    (results / f"{DATASET}.json").write_text(json.dumps(out))
