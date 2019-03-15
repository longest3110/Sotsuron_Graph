import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Qualitative_data.csv")
columns = list(data.columns)

ylabel = '解答時間 [秒]'
y = np.array(data[ylabel])
for c in ['最初が確定', '最後が確定', '全域サイクルを含む']:
	fig = plt.figure(c)
	x = np.array(data[c])

	plt.scatter(x, y)
	plt.xlabel(c)
	plt.ylabel(ylabel)
	plt.xlim(-1, 2)

	if c != '全域サイクルを含む':
		plt.xticks([0, 1], ['していない', 'している'])
	else:
		plt.xticks([0, 1], ['含まない', '含む'])

	fig.savefig('graph/Qualitative/{0}.png'.format(c))

