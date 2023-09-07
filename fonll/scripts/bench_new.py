import yadism
import yaml
import lhapdf
import json
import copy
from pathlib import Path
import numpy as np
import time
from eko import interpolation

include_nf5 = True
path_pinecards = "/home/roy/github/NNPDF/pinecards/"
dataset_name = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"
path_theorycard = "/home/roy/github/NNPDF/theories/data/theory_cards/400.yaml"

resultfolder = Path("./new_results")
resultfolder.mkdir(exist_ok=True)

pdf_nf3 = "221012-01-rs-nnpdf40_baseline_repeat_nf3"
pdf_nf4 = "221012-01-rs-nnpdf40_baseline_repeat_nf4"
pdf_nf5 = "221012-01-rs-nnpdf40_baseline_repeat_nf5"

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

# theorycard["TMC"] = 0
# observablecard["prDIS"] = "NC"
# theorycard["PTO"] = 2
# theorycard["IC"] = 1
theorycard["FONLLParts"] = "full"

# These are needed but for some reason not present in the theorycard
hfl = "cbt"
for fl in hfl:
    theorycard[f"kDIS{fl}Thr"] = 1.0

theorycards = [copy.deepcopy(theorycard) for _ in range(5)]
theorycards[0]["FNS"] = "FONLL-FFNS"
theorycards[0]["NfFF"] = 3
theorycards[1]["FNS"] = "FONLL-FFN0"
theorycards[1]["NfFF"] = 3
theorycards[2]["FNS"] = "FONLL-FFNS"
theorycards[2]["NfFF"] = 4
theorycards[3]["FNS"] = "FONLL-FFN0"
theorycards[3]["NfFF"] = 4
theorycards[4]["FNS"] = "FONLL-FFNS"
theorycards[4]["NfFF"] = 5

pdfnames = [pdf_nf3, pdf_nf3, pdf_nf4, pdf_nf4, pdf_nf5]

values = []
for enum, (pdfname, tc) in enumerate(zip(pdfnames, theorycards)):
    if include_nf5 or enum < 3:
        pdf = lhapdf.mkPDF(pdfname)
        out = yadism.run_yadism(tc, observablecard)
        values.append(out.apply_pdf(pdf))
end = time.time()


fonll_out = []
for observable_name, kinresults in values[0].items():
    for i, _kinpoint in enumerate(kinresults):
        if include_nf5:
            fonll_out.append(
                [
                    values[0][observable_name][i]["result"],
                    values[1][observable_name][i]["result"],
                    values[2][observable_name][i]["result"],
                    values[3][observable_name][i]["result"],
                    values[4][observable_name][i]["result"],
                ]
            )
        else:
            fonll_out.append(
                [
                    values[0][observable_name][i]["result"],
                    values[1][observable_name][i]["result"],
                    values[2][observable_name][i]["result"],
                ]
            )

with open(f"{str(resultfolder)}/{dataset_name}.json", "w") as f:
    json.dump(fonll_out, f)
