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

# plotBlockHistograms(samples, fraction_vs_p_plots, "fractions_p")
# plotBlockHistograms(samples, fraction_vs_theta_plots, "fractions_theta")


"""
mass_plot = {
    "data": [
        {
            "filename": "out_hgg.root",
            "histname": "hmass_tracker_idea",
            "label": "tracker",
        },
        {
            "filename": "out_hgg.root",
            "histname": "hmass_ecal_idea",
            "label": "tracker + ECAL",
        },
        {
            "filename": "out_hgg.root",
            "histname": "hmass_hcal_idea",
            "label": "tracker + ECAL + HCAL",
        },
    ],
    "name": "mass_components",
    "title_x": r"$M_{vis}$ [GeV]",
    "title_y": "event fraction",
    "yscale": "linear",
    "text": [
        {
            "content": r"$H \rightarrow gg$",
            "location": (0.25, 0.60),
        },
        {
            "content": "IDEA detector",
            "location": (0.01, 1.08),
        },
    ],
    "leg_loc": "upper left",
    "normalize": True,
    "option": "hist",
    # "ymin": 1e-3,
    # "ymax": 0.5,
    "rebin": 2,
}
"""


metrics = [
    {
        "name": "eleft",
        "label": r"$E/E_0$",
        "ymin": 0.5,
        "ymax": 1.0,
    },
    {
        "name": "nleft",
        "label": r"$N/N_0$",
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
            data = []
            for sample in samples:
                data.append(
                    {
                        "filename": sample["filename"],
                        "histname": "h{}".format(name),
                        "label": sample["label"],
                    }
                )

            text = [
                {
                    "content": collection["label"],
                    "location": (0.30, 0.60),
                },
                {
                    "content": "{} after cut".format(metric["label"]),
                    "location": (0.30, 0.50),
                },
            ]

            ## adjust text for photon p mult case
            if (
                metric["name"] == "nleft"
                and collection["label"] == "photons"
                and variable["name"] == "pcut"
            ):
                text[0]["location"] = (0.60, 0.80)
                text[1]["location"] = (0.60, 0.70)

            residual_plots.append(
                {
                    "data": data,
                    "name": name,
                    "title_y": metric["label"],
                    "title_x": variable["label"],
                    "yscale": "linear",
                    "leg_loc": "lower left",
                    "ymin": 0.0,
                    "ymax": 1.2,
                    "text": text,
                    "normfirstbin": True,
                    "option": "hist",
                    # "ymin": 1e-3,
                    # "ymax": 0.5,
                }
            )

# for plot in residual_plots:
#    plotHistograms(plot)

# plotHistograms(mass_plot)

mass_plots_detectors = []
for sample in samples:
    for observable in observables:
        data = []
        name = "detectors_{}_{}".format(observable["name"], sample["name"])
        for detector in detectors:
            # print("h{}_{}_hcal".format(observable["name"], detector["name"]))
            data.append(
                {
                    # "filename": sample["filename"],
                    "filename": sample["filename"],
                    "histname": "h{}_{}_hcal_pcut_0.0".format(
                        observable["name"], detector["name"]
                    ),
                    "label": detector["label"],
                }
            )
            mass_plots_detectors.append(
                {
                    "data": data,
                    "name": name,
                    "title_x": observable["label"],
                    "title_y": "event fraction",
                    "yscale": "linear",
                    "text": [
                        {
                            "content": sample["label"],
                            "location": (0.25, 0.60),
                        },
                        # {
                        #    "content": "IDEA detector",
                        #    "location": (0.01, 1.08),
                        # },
                    ],
                    "leg_loc": "upper left",
                    "normalize": True,
                    "option": "hist",
                    # "ymin": 1e-3,
                    # "ymax": 0.5,
                    "xmin": 100,
                    "xmax": 150,
                    "rebin": 4,
                }
            )
# for plot in mass_plots_detectors:
#    plotHistograms(plot)


mass_plots_detectors_pcut = []
for sample in samples:
    for observable in observables:
        for detector in detectors:
            for collection in collections:
                name = "detectors_{}_{}_{}_{}".format(
                    observable["name"],
                    sample["name"],
                    detector["name"],
                    collection["histname"],
                )
                data = []
                for pcut in pcuts:
                    histname = "h{}_{}_{}_{}".format(
                        observable["name"],
                        detector["name"],
                        collection["histname"],
                        pcut["name"],
                    )
                    data.append(
                        {
                            # "filename": sample["filename"],
                            "filename": sample["filename"],
                            "histname": histname,
                            "label": "{} {}".format(collection["label"], pcut["label"]),
                        }
                    )
                mass_plots_detectors_pcut.append(
                    {
                        "data": data,
                        "name": name,
                        "title_x": observable["label"],
                        "title_y": "event fraction",
                        "yscale": "linear",
                        "text": [
                            {
                                "content": sample["label"],
                                "location": (0.20, 0.50),
                            },
                            {
                                "content": collection["label"],
                                "location": (0.18, 0.35),
                            },
                            {
                                "content": detector["label"],
                                "location": (0.01, 1.08),
                            },
                        ],
                        "leg_loc": "upper left",
                        "normalize": True,
                        "option": "hist",
                        # "ymin": 1e-3,
                        # "ymax": 0.5,
                        "xmin": 110,
                        "xmax": 130,
                        "rebin": 2,
                    }
                )

for plot in mass_plots_detectors_pcut:
    plotHistograms(plot)
