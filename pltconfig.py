import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 15})

collection = "hcal"
detector = "perfect"

observables = [
    {"name": "mass", "label": r"$m_{vis}/m_{H}$", "title": "normalized visible mass"},
    {"name": "evis", "label": r"$E_{vis}/E_{H}$", "title": "normalized visible energy"},
]

variables = [
    {
        "name": "pcut",
        "histn": "p",
        "label": r"$p_{min}$ [MeV]",
    },
    {
        "name": "thetacut",
        "histn": "theta",
        "label": r"$\theta_{min}^{\circ}$",
    },
]


collections = [
    {
        "name": "gentracks",
        "label": "ch.had",
    },
    {
        "name": "genphotons",
        "label": r"$\gamma$",
    },
    {
        "name": "gennhadrons",
        "label": "n.had",
    },
]


samples = []
final_states = ["ss", "cc", "bb", "gg"]
# final_states = ["ss"]
for fs in final_states:
    samples.append(
        {
            "name": "h{}".format(fs),
            "filename": "out_h{}.root".format(fs),
            "linestyle": "solid",
            "label": r"$H \rightarrow {}$".format(fs),
        },
    )


metrics = [
    {
        "name": "resolution",
        "label": "rel. resolution",
    },
    {
        "name": "response",
        "label": "rel. response",
    },
]


resolution_plots = []
for variable in variables:
    for observable in observables:
        for metric in metrics:
            resolution_plots.append(
                {
                    "name": "{}_{}_{}".format(
                        observable["name"], metric["name"], variable["name"]
                    ),
                    "observable": observable,
                    "variable": variable,
                    "metric": metric,
                    "title_x": variable["label"],
                    "title_y": metric["label"],
                    "yscale": "linear",
                    "leg_loc": "upper left",
                }
            )


# _______________________________________________________________________________
