import math

fg = 0.25
fnh = 0.10
evis = 135


def resolutions(s_ecal, s_hcal):
    sigma_ecal = s_ecal * math.sqrt(fg * evis)
    sigma_hcal = s_hcal * math.sqrt(fnh * evis)
    sigma = math.sqrt(sigma_ecal ** 2 + sigma_hcal ** 2)
    return sigma_ecal, sigma_hcal, sigma


calos = [
    {
        "name": "atlas",
        "s_ecal": 0.10,
        "s_hcal": 0.50,
    },
    {
        "name": "cms",
        "s_ecal": 0.05,
        "s_hcal": 1.00,
    },
    {
        "name": "dr",
        "s_ecal": 0.10,
        "s_hcal": 0.30,
    },
    {
        "name": "dr_crys",
        "s_ecal": 0.05,
        "s_hcal": 0.30,
    },
]


for calo in calos:
    sigma_ecal, sigma_hcal, sigma = resolutions(calo["s_ecal"], calo["s_hcal"])
    print(
        "{}: ,sigma_ecal: {:.1f}, ,sigma_hcal: {:.1f}, sigma: {:.1f} ".format(
            calo["name"], sigma_ecal, sigma_hcal, sigma
        )
    )
