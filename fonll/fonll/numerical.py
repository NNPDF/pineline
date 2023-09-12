import copy
from pathlib import Path

import click
import lhapdf
import yadism

from .commons import dump, load, patch, DATASET, PDF

include_nf5 = False
FLAVORS = [3, 3, 4, 4, 5]
RESULTS = "numerical"


def _patch(theory, observables):
    theory, observables = patch(theory, observables)
    theory["FONLLParts"] = "full"

    theories = []
    for scheme, nf in [("FFNS", 3), ("FFN0", 3), ("FFNS", 4), ("FFN0", 4), ("FFNS", 5)]:
        th = copy.deepcopy(theory)
        th["FNS"], th["NfFF"] = f"FONLL-{scheme}", nf
        theories.append(th)
    return theories, observables


def compute(theories, observables):
    values = []
    for i, (nf, tc) in enumerate(zip(FLAVORS, theories)):
        pdfname = PDF[nf]
        if include_nf5 or i < 3:
            pdf = lhapdf.mkPDF(pdfname)
            out = yadism.run_yadism(tc, observables)
            values.append(out.apply_pdf(pdf))

    out = []
    for obs, kinresults in values[0].items():
        for i, _kinpoint in enumerate(kinresults):
            out.append(
                [
                    values[j][obs][i]["result"]
                    for j in range(len(FLAVORS) if include_nf5 else 3)
                ]
            )

    return out


@click.command()
@click.argument(
    "root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=Path.cwd(),
)
def run(root: Path):
    """Compute numerical FONLL results.

    ROOT is the path to your workspace.

    """
    t, o = _patch(*load(DATASET, root))
    dump(compute(t, o), root, RESULTS)
