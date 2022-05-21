import ROOT, sys
from ROOT import TFile, TH1F, TGraphErrors, TMultiGraph, TLegend, TF1, gROOT
import math
from collections import OrderedDict
from utils import *

from pltconfig import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# _______________________________________________________________________________
""" main """

datasets = dict()
for sample in samples:
    for variable in variables:
        for observable in observables:
            filename = sample["filename"]
            file = ROOT.TFile(filename)

            x = []
            mu = []
            sig = []

            dataset_name = "{}_{}_{}_{}_{}".format(
                sample["name"],
                observable["name"],
                collection,
                detector,
                variable["name"],
            )
            for key in file.GetListOfKeys():
                histname_prefix = "h{}_{}_{}_{}_".format(
                    observable["name"], collection, detector, variable["name"]
                )
                if histname_prefix in key.GetName():
                    print(key.GetName())
                    hname = key.GetName()
                    hist = file.Get(hname)

                    xval = float(hname.split("_")[-1])
                    x.append(xval)
                    # if x > 0: break

                    ## extract place where maximum is
                    mode = hist.GetXaxis().GetBinCenter(hist.GetMaximumBin())
                    mu.append(mode)

                    ## extract resolution
                    sigma = getEffSigma(hist, wmin=0.0, wmax=2.0, epsilon=0.01)
                    # sigma = getFWHM(hist) / 2.35

                    if mode > 0:
                        sig.append(sigma / mode)
                    else:
                        print("Did not find histogram maximum ...")
                        sig.append(sigma)

            df = pd.DataFrame({variable["name"]: x, "response": mu, "resolution": sig})
            df.name = dataset_name
            datasets[dataset_name] = df


plt.rcParams.update({"font.size": 15})
for plot in resolution_plots:
    fig, ax = plt.subplots()
    for sample in samples:
        sample_name = sample["name"]
        observable_name = plot["observable"]["name"]
        variable_name = plot["variable"]["name"]
        dataset_name = "{}_{}_{}_{}_{}".format(
            sample_name,
            observable_name,
            collection,
            detector,
            variable_name,
        )

        metric_name = plot["metric"]["name"]
        df = datasets[dataset_name]
        print(df)
        x = df[variable_name]
        y = df[metric_name]

        ax.plot(x, y, linestyle=sample["linestyle"], label="{}".format(sample["label"]))

    ax.legend(loc=plot["leg_loc"], frameon=False)
    ax.set_xlabel(plot["title_x"])
    ax.set_ylabel(plot["title_y"])
    ax.grid(linestyle="dashed")

    """
    if "ymin" in plot and "ymax" in plot:
        ax.set_ylim(plot["ymin"], plot["ymax"])
    """

    # ax.set_xscale("log")
    # ax.set_yscale(plot["yscale"])
    fig.tight_layout()
    fig.savefig("figs/{}.pdf".format(plot["name"]))
    fig.savefig("figs/{}.png".format(plot["name"]))

"""
    for plot in plots:
        varname = plot["name"]
        array_y = globals()[varname]
        ax = plot["plot"][1]
        linestyle = "solid"
        if s.d == 80:
            linestyle = "dotted"
        ax.plot(fluence, array_y, linestyle=linestyle, label="{}".format(s.label))


ax.plot(xs, mus, linestyle=linestyle, label="{}".format(label))

ax.legend(loc=plot["leg_loc"], frameon=False)
ax.set_xlabel(title_x)
ax.set_ylabel(plot["title_y"])
ax.grid(linestyle="dashed")

if "ymin" in plot and "ymax" in plot:
    ax.set_ylim(plot["ymin"], plot["ymax"])
ax.set_xscale("log")
ax.set_yscale(plot["yscale"])
fig.tight_layout()
fig.savefig("figs/{}.pdf".format(plot["name"]))
fig.savefig("figs/{}.png".format(plot["name"]))

"""
