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
        "eff": (0.1, 3.0),
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

# ______________________________________________________________________________

cfg_atlas_perfect = {
    "name": "atlas_perfect",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.145e-04, 2.024e-04, 2.093e-05),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # ptmin, etamax
        "eff": (0.0, 99.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.11, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.50, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
}

# ______________________________________________________________________________

cfg_cms_perfect = {
    "name": "cms_perfect",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.145e-04, 2.024e-04, 2.093e-05),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # ptmin, etamax
        "eff": (0.0, 99.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.05, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 1.00, 0.01),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
}
# ______________________________________________________________________________

cfg_idea_perfect = {
    "name": "idea_perfect",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.145e-04, 2.024e-04, 2.093e-05),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # ptmin, etamax
        "eff": (0.0, 99.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.11, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.30, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
}
# ______________________________________________________________________________

cfg_ideacry_perfect = {
    "name": "ideacry_perfect",
    "tracker": {
        "type": "trk",
        # sqrt(a^2 + pt*b^2 + pt^2*c^2), relative resolution
        "pt_res": (1.145e-04, 2.024e-04, 2.093e-05),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # ptmin, etamax
        "eff": (0.0, 99.0),
    },
    "ecal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.05, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
    "hcal": {
        "type": "calo",
        # sqrt(a^2/energy^2 + b^2/energy + c^2), relative resolution
        "energy_res": (0.0, 0.30, 0.0),
        # just a number in theta, phi for now
        "angular_res": 1.0e-99,
        # emin, etamax
        "eff": (0.0, 99.0),
    },
}
