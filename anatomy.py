import ROOT, sys
from ROOT import TFile, TH1F, TGraphErrors, TMultiGraph, TLegend, TF1, gROOT
import math
from collections import OrderedDict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import *
from pltconfig import *


metrics = ["eleft", "nleft"]

fraction_vs_p_plots = [
    {
        "name": "energy fraction",
        "histname": "hfracp_gentracks",
        "title_y": "charged energy fraction",
        "title_x": r"$p_{min}$ [GeV]",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": "ch.had",
        "ymin": 0.0,
        "ymax": 1.0,
    },
    {
        "name": "energy fraction",
        "histname": "hfracp_genphotons",
        "title_y": "photon energy fraction",
        "title_x": r"$p_{min}$ [GeV]",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": r"$\gamma$",
        "ymin": 0.0,
        "ymax": 1.0,
    },
    {
        "name": "energy fraction",
        "histname": "hfracp_gennhadrons",
        "title_y": "neutral hadron energy fraction",
        "title_x": r"$p_{min}$ [GeV]",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": "n.had",
        "ymin": 0.0,
        "ymax": 1.0,
    },
]

fraction_vs_theta_plots = [
    {
        "name": "energy fraction",
        "histname": "hfractheta_gentracks",
        "title_y": "charged energy fraction",
        "title_x": r"$\theta_{min}^{\circ}$",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": "ch.had",
        "ymin": 0.0,
        "ymax": 1.0,
    },
    {
        "name": "energy fraction",
        "histname": "hfractheta_genphotons",
        "title_y": "photon energy fraction",
        "title_x": r"$\theta_{min}^{\circ}$",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": r"$\gamma$",
        "ymin": 0.0,
        "ymax": 1.0,
    },
    {
        "name": "energy fraction",
        "histname": "hfractheta_gennhadrons",
        "title_y": "neutral hadron energy fraction",
        "title_x": r"$\theta_{min}^{\circ}$",
        "yscale": "linear",
        "leg_loc": "lower left",
        "label": "n.had",
        "ymin": 0.0,
        "ymax": 1.0,
    },
]

"""
for plot in anatomy_plots:
    plotRootHistograms(samples, plot)
"""

plotBlockHistograms(samples, fraction_vs_p_plots, "fractions_p")
plotBlockHistograms(samples, fraction_vs_theta_plots, "fractions_theta")


metrics = [
    {
        "name": "eleft",
        "label": "energy [GeV]",
        "ymin": 0.5,
        "ymax": 1.0,
    },
    {
        "name": "nleft",
        "label": "multiplicty",
        "ymin": 0.5,
        "ymax": 1.0,
    },
]


residual_plots = []
for metric in metrics:
    for variable in variables:
        for collection in collections:
            name = "{}{}_{}".format(
                metric["name"], variable["histn"], collection["name"]
            )
            residual_plots.append(
                {
                    "name": name,
                    "histname": "h{}".format(name),
                    "title_y": metric["label"],
                    "title_x": variable["label"],
                    "yscale": "linear",
                    "leg_loc": "upper right",
                    "ymin": 0.5,
                    "ymax": 1.0,
                }
            )

for plot in residual_plots:
    plotRootHistograms(samples, plot)
