import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(9, 63):
    G.add_node(i)

with open('C:/Users/student/Desktop/system_dolphins.txt', encoding='utf-8') as dolph:
    lines = dolph.readlines()
    for line in lines:
        newline = line.strip()
        dline = newline.split('\t')
        G.add_edge(dline[0], dline[1])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = 'red', node_size = 100)
nx.draw_networkx_edges(G, pos, edge_color = 'green')
nx.draw_networkx_labels(G, pos, font_size = 15)
plt.axis('Off')


deg = nx.degree_centrality(G)
for node_id in sorted(deg, key = deg.get, reverse = True):
    print(node_id, deg[node_id])

try:
    print('Диаметр: ' + str(nx.diameter(G)))
except:
    print('Вообще не связанный граф :(')
print('Количество узлов: ' + str(G.number_of_nodes()))
print('Количество ребер: ' + str(G.number_of_edges()))
print('Плотность графа: ' + str(nx.density(G)))
print('Средний уровень кластеризации: ' + str(nx.average_clustering(G)))
plt.show()
