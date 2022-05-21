from configuration import *
from detector import *
import numpy as np
import copy
from collections import OrderedDict
import random


def em_res(energy):
    return np.sqrt((energy * 0.01) ** 2 + energy * 0.11 ** 2)


def had_res(energy):
    return np.sqrt((energy * 0.01) ** 2 + energy * 0.30 ** 2)


def log_normal(mean, sigma, size):

    b = np.sqrt(np.log((1.0 + (sigma / mean) ** 2)))
    a = np.log(mean) - 0.5 * b ** 2

    evs = np.ones(size)

    for i in range(evs.size):
        if mean > 0.0:
            evs[i] = np.exp(a + b * np.random.normal(0.0, 1.0))

    return evs


def trunc_gauss(mean, sigma, size):

    lst = []
    while len(lst) <= size:
        dice = random.gauss(mean, sigma)
        if dice > 0.0:
            lst.append(dice)

    evs = np.array(lst)
    return evs


## input particle energy
energy = 1.0
em_res = em_res(energy)
had_res = had_res(energy)
sig = energy / had_res

emin = 0.1
sigmin = 3.0

print("energy: ", energy)
print("energy: ", energy, "em res: ", em_res, "em_sigma: ", energy / em_res)
print("had res: ", had_res, "had_sigma: ", energy / had_res)


mu, sigma = energy, had_res  # mean and standard deviation
nev = 100
logn = log_normal(mu, sigma, nev)
gauss = np.random.normal(mu, sigma, nev)
trgauss = trunc_gauss(mu, sigma, nev)

import matplotlib.pyplot as plt

# simulate pion gun
counter = 0
for i in range(nev):
    erec_logn = logn[i]
    # erec_gaus = gauss[i]
    # erec_trga = trgauss[i]
    delta = erec_logn - energy
    sign = delta / had_res
    print("------------------------------------------------------------")
    print(
        "erec: ",
        erec_logn,
        "had res: ",
        had_res,
        "delta:",
        delta,
        "had_sigma: ",
        energy / had_res,
    )
    if delta > emin and sign > sigmin:
        counter += 1

print(counter)


"""
plt.hist(
    [logn, gauss, trgauss], 50, density=True, align="mid", histtype=u"step", linewidth=2
)


plt.axis("tight")
plt.show()
"""
