from graphviz import Digraph
import sqlite3

connection = sqlite3.connect('Jukugo.db')
cursor = connection.cursor()

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')

# ルートのノード
root = "学"

node_list = list(root)

# ルートのノード生成
G.node(root)

last_node = list(root)


for _ in range(3):
	tmp = list()
	for r in last_node:
		for n in tuple(cursor.execute("SELECT right_kanji FROM idioms_master WHERE left_kanji='{0}' ORDER BY RANDOM() LIMIT 3".format(r[-1]))):
			if not n[0] in node_list:
				tmp.append(n[0])
				G.node(n[0])
				G.edge(r, n[0])
				node_list.append(n[0])
	
	last_node = tmp


# print()するとdot形式で出力される
print(G)
print(node_list)

# binary_tree.pngで保存
G.render('binary_tree')

connection.commit()
connection.close()