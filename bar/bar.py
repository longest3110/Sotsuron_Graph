import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure("test")

left = np.array([1, 2, 3, 4, 5])
height = np.array([100, 200, 300, 400, 500])
plt.bar(left, height)

fig.savefig('test.png')