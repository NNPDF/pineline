from pathlib import Path

import click
import numpy as np

from .commons import load, compute, dump, DATASET

PDF = "221012-01-rs-nnpdf40_baseline_repeat_nf4"


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

    return theory, observables


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
    t, o = patch(*load(DATASET, root))

    results = root / "results" / "analytical"
    results.mkdir(exist_ok=True, parents=True)
    dump(compute(t, o, PDF), results)
