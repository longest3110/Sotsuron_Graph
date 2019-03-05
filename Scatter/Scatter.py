import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")
columns = list(data.columns)

y = np.array(data['time_ave'])
for c in columns:
	fig = plt.figure(c)
	x = np.array(data[c])

	res = np.polyfit(x, y, 2) #2次
	x2 = np.linspace(np.amin(x), np.amax(x), 100)
	y2 = np.poly1d(res)(x2)

	plt.scatter(x, y)
	plt.plot(x2, y2)

	fig.savefig('graph/{0}.png'.format(c))

