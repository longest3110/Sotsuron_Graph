from graphviz import Digraph

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')



# ノードの追加
G.node("本")
G.node("当")

# 辺の追加
G.edge("本", "当")

# print()するとdot形式で出力される
print(G)

# binary_tree.pngで保存
G.render('binary_tree')