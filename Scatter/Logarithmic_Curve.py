import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


def func(x, a, b, c):
		return a * np.log(b * x) + c

data = pd.read_csv("data.csv")
columns = list(data.columns)
labels = {'vertex':"辺の本数 [本]", 'answer':"解の個数 [個]", 'in_vetex_max':"入次数の最大値 [本]", 'out_vertex_max':"出次数の最大値 [本]", 'multiple':"多重辺の本数 [本]", 'time_ave':"解答時間 [秒]", 'respondent':"完答率 [%]"}

ylabel = 'respondent'
y = np.array(data[ylabel])
for c in columns:
	fig = plt.figure(c)
	x = np.array(data[c])

	x2 = np.linspace(np.amin(x), np.amax(x), 100)
	popt, pcov = curve_fit(func, x, y)

	plt.scatter(x, y)
	plt.xlabel(labels[c])
	plt.ylabel(labels[ylabel])
	plt.plot(x2, func(x2, *popt), color='black')

	fig.savefig('graph/Logarithmic_Curve/{0}.png'.format(c))