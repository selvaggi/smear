import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 15})


observables_norm = [
    {
        "name": "mass_norm",
        "label": r"$m_{vis}/m_{H}$",
        "title": "normalized visible mass",
    },
    {
        "name": "evis_norm",
        "label": r"$E_{vis}/E_{H}$",
        "title": "normalized visible energy",
    },
]

observables = [
    {"name": "mass", "label": r"$M_{vis} [GeV]$", "title": "visible mass"},
    {"name": "evis", "label": r"$E_{vis}$ [GeV]", "title": "visible energy"},
]

variables = [
    {
        "name": "pcut",
        "histn": "p",
        "label": r"$p_{min}$ [GeV]",
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
        "label": "charged hadrons",
        "histname": "tracker",
    },
    {
        "name": "genphotons",
        "label": "photons",
        "histname": "ecal",
    },
    {
        "name": "gennhadrons",
        "label": "neutral hadrons",
        "histname": "hcal",
    },
]

detectors = [
    {
        "name": "idea_perfect",
        "label": "IDEA",
    },
    {
        "name": "ideacry_perfect",
        "label": "IDEA + crystals",
    },
    {
        "name": "atlas_perfect",
        "label": "ATLAS",
    },
    {
        "name": "cms_perfect",
        "label": "CMS",
    },
]


pcuts = [
    {
        "name": "pcut_0.0",
        "label": r"$p_{min}$ > 0 MeV",
    },
    {
        "name": "pcut_100.0",
        "label": r"$p_{min}$ > 100 MeV",
    },
    {
        "name": "pcut_200.0",
        "label": r"$p_{min}$ > 200 MeV",
    },
    {
        "name": "pcut_300.0",
        "label": r"$p_{min}$ > 300 MeV",
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

# _______________________________________________________________________________
