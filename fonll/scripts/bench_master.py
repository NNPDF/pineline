import yadism
import yaml
import lhapdf
import json
from pathlib import Path
import numpy as np

path_pinecards = "/home/roy/github/NNPDF/pinecards/"
dataset_name = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"
path_theorycard = "/home/roy/github/NNPDF/theories/data/theory_cards/400.yaml"

resultfolder = Path("./master_results")
resultfolder.mkdir(exist_ok=True)

pdf_nf4 = "221012-01-rs-nnpdf40_baseline_repeat_nf4"

with open(path_pinecards + dataset_name + "/observable.yaml", "r") as f:
    observablecard = yaml.safe_load(f)

with open(path_theorycard, "r") as f:
    theorycard = yaml.safe_load(f)

mb2 = theorycard["mb"] ** 2
mc2 = theorycard["mc"] ** 2


del observablecard["observables"]["XSHERANCAVG_charm"]
observablecard["observables"]["F2_charm"] = []
# for qq in np.geomspace(mc2,16*mb2,10):
qq=5.0
for xx in np.geomspace(5e-7, 1, 10):
    observablecard["observables"]["F2_charm"].append(
        {"Q2": qq, "x": xx}
    )


# These are needed but for some reason not present in the theorycard
hfl = "cbt"
for fl in hfl:
    theorycard[f"kDIS{fl}Thr"] = 1.0

# theorycard["TMC"] = 0
# observablecard["prDIS"] = "NC"
# observablecard["IC"] = 0

# theorycard[f"kDISbThr"] = 4.0
theorycard[f"kbThr"] = 4.0

# theorycard["FONLLParts"] = "full"
# theorycard["FNS"] = "FONLL-A"
# theorycard["NfFF"] = 3
# theorycard["PTO"] = 1


pdf = lhapdf.mkPDF(pdf_nf4)
values = yadism.run_yadism(theorycard, observablecard)
values = values.apply_pdf(pdf)

out = []
for observable_name, kinresults in values.items():
    for i, kinpoint in enumerate(kinresults):
        out.append(
            [
                values[observable_name][i]["result"],
                values[observable_name][i]["x"],
                values[observable_name][i]["Q2"],
            ]
        )

with open(f"{str(resultfolder)}/{dataset_name}.json", "w") as f:
    json.dump(out, f)
