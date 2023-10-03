from pathlib import Path

import click
import lhapdf
import yadism

from .commons import dump, load, patch, DATASET, PDF

RESULTS = "analytical"


def _patch(theory, observables):
    theory, observables = patch(theory, observables)

    # theory[f"kDISbThr"] = 4.0
    theory["kbThr"] = 4.0
    theory["FNS"] = "FONLL-B"

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


@click.command()
@click.argument(
    "root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=Path.cwd(),
)
def run(root: Path):
    """Compute analytical FONLL results.

    ROOT is the path to your workspace.

    """
    t, o = _patch(*load(DATASET, root))
    dump(compute(t, o, PDF[4]), root, RESULTS)
