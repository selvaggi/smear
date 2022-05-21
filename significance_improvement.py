import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 15})

x = np.logspace(-3, 1, 100)

fig, ax = plt.subplots()

alpha = 2.0

alphas = [1.05, 1.1, 1.2, 1.5]

for alpha in alphas:
    y_alpha = 100.0 * np.sqrt(alpha * (1.0 + x) / (1.0 + alpha * x)) - 100
    ax.plot(x, y_alpha, label=r"$\alpha - 1 = {:.2f}$".format(alpha - 1))

ax.legend(loc="upper right", frameon=False)
ax.set_xlabel("S/B")
ax.set_ylabel("gain in precision (%)")
ax.grid(linestyle="dashed")
ax.set_xscale("log")
ax.set_ylim(-2.0, 30.0)
fig.tight_layout()
fig.savefig("figs/gain_precision.pdf")
fig.savefig("figs/gain_precision.png")
