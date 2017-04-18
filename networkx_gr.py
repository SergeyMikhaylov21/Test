#https://www.cs.upc.edu/~rferrericancho/linguistic_and_cognitive_networks.html
#http://konect.uni-koblenz.de/

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5, 6])
G.remove_node(2)

G.add_edge(1, 3)
G.add_edges_from([(1, 4), (4, 5), (5, 6)])

G.nodes() #количество узлов
G.edges() #количество ребер
G.neighbors(1)
G.degree(1) #число соседей узла (степень узла)

for node in G.nodes():
    print(node, G.degree(node))

G.add_edge(3, 5, weight = 4)

nx.write_gexf(G, 'graph.gexf')

G1 = nx.read_gexf('graph.gexf')

pos = nx.spring_layout(G) #spring - один из способов укладки графа
nx.draw_networkx_nodes(G, pos, node_color = 'red', node_size = 50)
nx.draw_networkx_edges(G, pos, edge_color = 'green')
nx.draw_networkx_labels(G, pos, font_size = 10)
plt.axis('Off')
plt.show() #plt.savefig('graph.png')

nx.diameter(G) #связность элементов графа между собой (один из критериев). Длина пути между крайними узлами
G.number_of_nodes()
G.number_of_edges()
nx.density(G) #плотность графа
nx.average_clustering(G) #чем ближе к единице, тем менее граф кластеризуемый

deg = nx.degree_centrality(G)
for node_id in sorted(deg, key = deg.get, reverse = True):
    print(node_id, deg[node_id])
    

