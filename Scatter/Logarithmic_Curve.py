import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def func(x, a, b, c):
		return a * np.log(b * x) + c

data = pd.read_csv("data.csv")
columns = list(data.columns)

y = np.array(data['time_ave'])
for c in columns:
	fig = plt.figure(c)
	x = np.array(data[c])

	x2 = np.linspace(np.amin(x), np.amax(x), 100)
	popt, pcov = curve_fit(func, x, y)

	plt.scatter(x, y)
	plt.plot(x2, func(x2, *popt), color='black')

	fig.savefig('graph/{0}.png'.format(c))