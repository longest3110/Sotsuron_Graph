import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")
columns = list(data.columns)
labels = {'vertex':"辺の本数 [本]", 'answer':"解の個数 [個]", 'in_vetex_max':"入次数の最大値 [本]", 'out_vertex_max':"出次数の最大値 [本]", 'multiple':"多重辺の本数 [本]", 'time_ave':"解答時間 [秒]", 'respondent':"完答率 [%]"}


for ylabel in 'time_ave', 'respondent':
	y = np.array(data[ylabel])
	for c in columns:
		fig = plt.figure(ylabel + c)
		x = np.array(data[c])

		plt.scatter(x, y)
		plt.xlabel(labels[c])
		plt.ylabel(labels[ylabel])

		fig.savefig('graph/{0}_{1}.png'.format(ylabel, c))

