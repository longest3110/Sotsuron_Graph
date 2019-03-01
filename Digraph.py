from graphviz import Digraph
import sqlite3

connection = sqlite3.connect('Jukugo.db')
cursor = connection.cursor()

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')

# ルートのノード
root = "学年金"

# ルートのノード生成
G.node(root, shape='box')

for n in tuple(cursor.execute("SELECT right_kanji FROM idioms_master WHERE left_kanji='{0}' ORDER BY RANDOM() LIMIT 10".format(root[-1]))):
	G.node(n[0])
	G.edge(root, n[0])

# print()するとdot形式で出力される
print(G)

# binary_tree.pngで保存
G.render('binary_tree')

connection.commit()
connection.close()