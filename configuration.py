# ______________________________________________________________________________

cfg_idea = {
    "name": "idea",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.145e-04, 2.024e-04, 2.093e-05),
        # just a number in theta, phi for now
        "angular_res": 0.001,
        # ptmin, etamax
        "eff": (0.1, 3.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.11, 0.01),
        # just a number in theta, phi for now
        "angular_res": 0.01,
        # emin, etamax
        "eff": (0.1, 3.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.30, 0.01),
        # just a number in theta, phi for now
        "angular_res": 0.01,
        # emin, etamax
        "eff": (0.6, 3.0),
    },
}

# ______________________________________________________________________________

cfg_perfect = {
    "name": "perfect",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.0e-99, 1.0e-99, 1.0e-99),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # ptmin, etamax
        "eff": (0.0, 99.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (1.0e-99, 1.0e-99, 1.0e-99),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (1.0e-99, 1.0e-99, 1.0e-99),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
}
