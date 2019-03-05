import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")
columns = list(data.columns)

y = np.array(data['time_ave'])
for c in columns:
	fig = plt.figure(c)
	x = np.array(data[c])
	plt.scatter(x, y)
	fig.savefig('graph/{0}.png'.format(c))

