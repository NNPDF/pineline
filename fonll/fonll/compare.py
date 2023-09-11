import json
from pathlib import Path
from dataclasses import dataclass

import click
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import seaborn as sns
from tabulate import tabulate

from .analytical import RESULTS as ARES
from .commons import dataset
from .numerical import RESULTS as NRES


INCLUDE_NF5 = False
COLUMNS = ["Q2", "x", "new", "old", "percent_diff"]
Q2CUT = 3.49
OUT = "images"


def load(analytical, numerical):
    def _l(f):
        return np.array(json.loads(f.read_text()))

    return Data(_l(analytical), _l(numerical))


@dataclass
class Data:
    ana: npt.NDArray
    num: npt.NDArray

    @property
    def x(self):
        return self.ana[:, 1]

    @property
    def q2(self):
        return self.ana[:, 2]

    @property
    def uniqx(self) -> npt.NDArray:
        return np.unique(self.x)

    @property
    def uniqq2(self) -> npt.NDArray:
        return np.unique(self.q2)

    @property
    def shape(self):
        return len(self.uniqq2), len(self.uniqx)

    @property
    def anares(self):
        return self.ana[:, 0]

    @property
    def numres(self) -> npt.NDArray:
        return sum((-1) ** n * self.num[:, n] for n in range(5 if INCLUDE_NF5 else 3))

    @property
    def table(self):
        tab = [COLUMNS]
        for q2, xx, new, old in zip(self.q2, self.x, self.numres, self.anares):
            if q2 < Q2CUT:
                continue
            tab.append([q2, xx, new, old, ((new / old) - 1.0) * 100])
        return tab

    @property
    def ratio(self):
        ratio = (np.float64(self.numres) / self.anares).reshape(self.shape)
        ratio = np.flip(ratio, axis=0)
        return pd.DataFrame(
            ratio,
            columns=np.around(self.uniqx, 6),
            index=np.around(np.flip(self.uniqq2), 1),
        )


# ++++++++++++++++ 1d sf plot +++++++++++++++++++++++++++++++++++++++++
def sf_plot(d: Data, dest: Path):
    plt.figure()
    #  single_x = np.where(d.x == d.uniqx[-1])[0]
    # single_x=np.array([i for i in range(len(x))])
    # plt.plot(q2[single_x],d.num[:,0][single_x],"o",color="C2", label="FFNS3",alpha=0.5)
    # plt.plot(q2[single_x],d.num[:,1][single_x],"v",color="C3", label="FFN03",alpha=0.5)
    # plt.plot(q2[single_x],d.num[:,2][single_x],"^",color="C4", label="FFNS4",alpha=0.5)
    # plt.plot(q2[single_x],d.num[:,3][single_x],">",color="C5", label="FFN04",alpha=0.5)
    # plt.plot(q2[single_x],d.num[:,4][single_x],"<",color="C6", label="FFNS5",alpha=0.5)
    # plt.plot(q2[single_x],d.anares[single_x],"s", color="C0", label="aFONLL",alpha=0.5)
    # plt.plot(q2[single_x],d.numres[single_x],"P",color="C1", label="nFONLL",alpha=0.5)
    # plt.axvline(x = 5, label = 'POS scale', color='blue')
    # plt.axvline(x = 387.3, label = r'$(4m_b)^2$', color='black')

    plt.plot(d.x, d.num[:, 0], "o", color="C2", label="FFNS3", alpha=0.5)
    plt.plot(d.x, d.num[:, 1], "v", color="C3", label="FFN03", alpha=0.5)
    plt.plot(d.x, d.num[:, 2], "^", color="C4", label="FFNS4", alpha=0.5)
    # plt.plot(x,d.num[:,3],">",color="C5", label="FFN04",alpha=0.5)
    # plt.plot(x,d.num[:,4],"<",color="C6", label="FFNS5",alpha=0.5)
    plt.plot(d.x, d.anares, "s", color="C0", label="aFONLL", alpha=0.5)
    plt.plot(d.x, d.numres, "P", color="C1", label="nFONLL", alpha=0.5)
    # plt.axvline(x = 5/(5+4*4.92**2), label = r'$\frac{Q^2}{Q^2+4m_b}$', color='black')

    #  plt.xscale("log")
    # plt.yscale("log")
    plt.yscale("symlog", linthresh=1e-10)
    # plt.title(f"x={x[single_x][0]}")
    # plt.title(f"Q2={q2[0]} GeV2")
    # plt.xlabel(r"$x$")
    plt.legend()
    plt.savefig(dest / "sf.png")
    plt.savefig(dest / "sf.pdf")


# ++++++++++++++++ heatmap with values +++++++++++++++++++++++++++++++++++++++++
def heatmap(ratio, dest: Path):
    plt.figure(figsize=(2 * 10, 2 * 6))
    sns.heatmap(
        (ratio - 1) * 100,
        annot=True,
        shading="auto",
        cmap=plt.colormaps["RdBu_r"],
        norm=colors.CenteredNorm(vcenter=0.0, halfrange=50),
        fmt=".3g",
        cbar_kws={"label": "(nFONLL - aFONLL) / aFONLL %"},
    )
    plt.xlabel(r"$x$")
    plt.ylabel(r"$Q^2$")
    plt.title(r"$F_{2}$")
    plt.savefig(dest / "heatmap.pdf")
    plt.savefig(dest / "heatmap.png")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def four_plot(d: Data, dest: Path):
    fig = plt.figure(figsize=(13, 10))

    def colormesh(ax, value, **kwargs):
        return ax.pcolormesh(
            d.uniqx,
            d.uniqq2,
            value.reshape(d.shape)[:-1, :-1],
            shading="auto",
            **kwargs
        )

    def aspect(ax, title):
        ax.set_ylabel(r"$Q^2$")
        ax.set_xlabel(r"$x$")
        #  ax.set_xscale("log")
        #  ax.set_yscale("log")
        ax.set_title(title)

    ax0 = fig.add_subplot(2, 2, 3)
    ax1 = fig.add_subplot(2, 2, 2)
    ax2 = fig.add_subplot(2, 2, 1)
    ax3 = fig.add_subplot(2, 2, 4)

    im0 = colormesh(
        ax0,
        d.numres / d.anares,
        cmap=plt.colormaps["RdBu_r"],
        norm=colors.CenteredNorm(vcenter=1.0, halfrange=0.25),
    )
    aspect(ax0, "numerical fonll / analytical fonll")

    im1 = colormesh(
        ax1,
        np.log10(d.anares),
        cmap=plt.colormaps["magma"],
    )
    aspect(ax1, "analytical fonll structure function")

    im2 = colormesh(
        ax2,
        np.log10(d.numres),
        cmap=plt.colormaps["magma"],
    )
    aspect(ax2, "numerical fonll structure function")

    im3 = colormesh(
        ax3,
        d.anares - d.numres,
        cmap=plt.colormaps["PuOr"],
        norm=colors.CenteredNorm(
            vcenter=0.0, halfrange=3 * np.std(d.anares - d.numres)
        ),
    )
    aspect(ax3, "analytical fonll - numerical fonll")

    _ = fig.colorbar(im0, ax=ax0, extend="both")
    cb1 = fig.colorbar(im1, ax=ax1)
    cb2 = fig.colorbar(im2, ax=ax2)
    _ = fig.colorbar(im3, ax=ax3)
    cb2.mappable.set_clim(*cb1.mappable.get_clim())

    fig.tight_layout()

    fig.savefig(dest / "four.pdf")
    fig.savefig(dest / "four.png")


@click.command()
@click.argument(
    "root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=Path.cwd(),
)
def compare(root: Path):
    """Compare FONLL results.

    ROOT is the path to your workspace.

    """
    data = load(dataset(root, ARES), dataset(root, NRES))
    print(tabulate(data.table))

    (root / OUT).mkdir(exist_ok=True, parents=True)
    sf_plot(data, root / OUT)
    heatmap(data.ratio, root / OUT)
    four_plot(data, root / OUT)
