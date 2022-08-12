# %%
import numpy as np
import matplotlib.pyplot as plt


def arrow(start, size, color):
    plt.quiver(
        start[0], start[1], size[0], size[1], angles="xy", scale_units="xy", scale=1, color=color
    )


s = np.array([0, 0])
a = np.array([2, 3])

plt.axes().set_aspect("equal")
arrow(s, a, color="black")

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()


# %%
