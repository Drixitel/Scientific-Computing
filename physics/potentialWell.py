# %%
import numpy as np
import matplotlib.pyplot as plt


r = np.linspace(0.0001, 0.16, 100000)
a = 0.074
Uo = 4.5
p = (a / r) ** 12
p2 = (a / r) ** 6

U = Uo * (p - 2 * p2)
plt.close("all")
plt.plot(r, U, "b-")
plt.xlim(0.05, 0.175)
plt.ylim(-10, 20)
plt.xlabel("separation r (nm)")
plt.ylabel("potential energy (eV)")
plt.grid(True)
plt.show()


# %%
