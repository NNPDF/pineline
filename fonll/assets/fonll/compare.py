import json
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import seaborn as sns
from tabulate import tabulate


def load(*args):
    return [np.array(json.load(f)) for f in args]


def table():
    x = master[:, 1]
    q2 = master[:, 2]
    uniqx = np.unique(x)
    uniqq2 = np.unique(q2)

    master_result = master[:, 0]
    new_result = new
    fonll_result = (
        new_result[:, 0] - new_result[:, 1] + new_result[:, 2]
        if not include_nf5
        else new_result[:, 0]
        - new_result[:, 1]
        + new_result[:, 2]
        - new_result[:, 3]
        + new_result[:, 4]
    )

    to_table = [["Q2", "x", "new", "old", "percent_diff"]]
    for q2, xx, new, old in zip(q2, x, fonll_result, master_result):
        if q2 < 3.49:
            continue
        to_table.append([q2, xx, new, old, ((new / old) - 1.0) * 100])
    print(tabulate(to_table))

    ratio = (
        (np.float64(fonll_result) / master_result).reshape(len(uniqx), len(uniqq2)).T
    )
    ratio = np.flip(ratio, axis=0)
    pd_ratio = pd.DataFrame(
        ratio, columns=np.around(uniqx, 6), index=np.around(np.flip(uniqq2), 1)
    )


# ++++++++++++++++ 1d sf plot +++++++++++++++++++++++++++++++++++++++++
def sf_plot():
    plt.figure()
    single_x = np.where(x == uniqx[-1])[0]
    # single_x=np.array([i for i in range(len(x))])
    # plt.plot(q2[single_x],new_result[:,0][single_x],"o",color="C2", label="FFNS3",alpha=0.5)
    # plt.plot(q2[single_x],new_result[:,1][single_x],"v",color="C3", label="FFN03",alpha=0.5)
    # plt.plot(q2[single_x],new_result[:,2][single_x],"^",color="C4", label="FFNS4",alpha=0.5)
    # plt.plot(q2[single_x],new_result[:,3][single_x],">",color="C5", label="FFN04",alpha=0.5)
    # plt.plot(q2[single_x],new_result[:,4][single_x],"<",color="C6", label="FFNS5",alpha=0.5)
    # plt.plot(q2[single_x],master_result[single_x],"s", color="C0", label="aFONLL",alpha=0.5)
    # plt.plot(q2[single_x],fonll_result[single_x],"P",color="C1", label="nFONLL",alpha=0.5)
    # plt.axvline(x = 5, label = 'POS scale', color='blue')
    # plt.axvline(x = 387.3, label = r'$(4m_b)^2$', color='black')

    plt.plot(x, new_result[:, 0], "o", color="C2", label="FFNS3", alpha=0.5)
    plt.plot(x, new_result[:, 1], "v", color="C3", label="FFN03", alpha=0.5)
    plt.plot(x, new_result[:, 2], "^", color="C4", label="FFNS4", alpha=0.5)
    # plt.plot(x,new_result[:,3],">",color="C5", label="FFN04",alpha=0.5)
    # plt.plot(x,new_result[:,4],"<",color="C6", label="FFNS5",alpha=0.5)
    plt.plot(x, master_result, "s", color="C0", label="aFONLL", alpha=0.5)
    plt.plot(x, fonll_result, "P", color="C1", label="nFONLL", alpha=0.5)
    # plt.axvline(x = 5/(5+4*4.92**2), label = r'$\frac{Q^2}{Q^2+4m_b}$', color='black')

    plt.xscale("log")
    # plt.yscale("log")
    plt.yscale("symlog", linthresh=1e-10)
    # plt.title(f"x={x[single_x][0]}")
    # plt.title(f"Q2={q2[0]} GeV2")
    # plt.xlabel(r"$x$")
    plt.legend()
    plt.savefig("test2.png")
    plt.savefig("test2.pdf")


# ++++++++++++++++ heatmap with values +++++++++++++++++++++++++++++++++++++++++
def heatmap():
    plt.figure(figsize=(2 * 10, 2 * 6))
    sns.heatmap(
        pd_ratio,
        annot=True,
        shading="auto",
        cmap=plt.colormaps["bwr"],
        norm=colors.CenteredNorm(vcenter=1.0, halfrange=0.5),
        fmt=".3f",
        cbar_kws={"label": "nFONLL / aFONLL"},
    )
    plt.xlabel(r"$x$")
    plt.ylabel(r"$Q^2$")
    plt.title(r"$F_{2}$")
    plt.savefig("test.pdf")
    plt.savefig("test.png")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def other_plot():
    fig = plt.figure(figsize=(13, 10))

    ax0 = fig.add_subplot(2, 2, 3)
    ax1 = fig.add_subplot(2, 2, 2)
    ax2 = fig.add_subplot(2, 2, 1)
    ax3 = fig.add_subplot(2, 2, 4)
    X, Y = np.meshgrid(uniqx, uniqq2)

    im0 = ax0.pcolormesh(
        X,
        Y,
        (fonll_result / master_result).reshape(len(uniqx), len(uniqq2)).T,
        shading="auto",
        cmap=plt.colormaps["bwr"],
        norm=colors.CenteredNorm(vcenter=1.0, halfrange=0.25),
    )
    ax0.set_ylabel(r"$Q^2$")
    ax0.set_xlabel(r"$x$")
    ax0.set_xscale("log")
    ax0.set_yscale("log")
    ax0.set_title("numerical fonll / analytical fonll")

    im1 = ax1.pcolormesh(
        X,
        Y,
        np.log(master_result.reshape(len(uniqx), len(uniqq2))).T,
        shading="auto",
    )
    ax1.set_ylabel(r"$Q^2$")
    ax1.set_xlabel(r"$x$")
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_title("analytical fonll structure function")

    im2 = ax2.pcolormesh(
        X,
        Y,
        np.log(fonll_result.reshape(len(uniqx), len(uniqq2))).T,
        shading="auto",
    )
    ax2.set_ylabel(r"$Q^2$")
    ax2.set_xlabel(r"$x$")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_title("numerical fonll structure function")

    im3 = ax3.pcolormesh(
        X,
        Y,
        ((master_result - fonll_result).reshape(len(uniqx), len(uniqq2))).T,
        shading="auto",
        cmap="plasma",
    )
    ax3.set_ylabel(r"$Q^2$")
    ax3.set_xlabel(r"$x$")
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    ax3.set_title("analytical fonll - numerical fonll")

    cb0 = fig.colorbar(im0, ax=ax0, extend="both")
    cb1 = fig.colorbar(im1, ax=ax1)
    cb2 = fig.colorbar(im2, ax=ax2)
    cb3 = fig.colorbar(im3, ax=ax3)
    cb2.mappable.set_clim(*cb1.mappable.get_clim())

    fig.tight_layout()

    fig.savefig("test1.pdf")
    fig.savefig("test1.png")


def compare():
    include_nf5 = False
    dataset = "HERA_NC_318GEV_EAVG_SIGMARED_CHARM"

    #  new, master = load(f"new_results/{dataset}.json", f"master_results/{dataset}.json")
