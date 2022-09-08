import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.drawing.nx_pydot import graphviz_layout
# G=nx.complete_graph(10)
# #G.add_nodes_from(range(20))
# for e in G.edges:
#     G.edges[e]["distance"]=np.random.randint(10,100)
# adj0=G.adj[0]
# print(adj0)
# minimum=min(adj0,key=lambda u:adj0[u]["distance"])
# print(minimum)
adj={ 20: [40], 10: [35], 9: [12],  2: [7, 3, 15], 7: [9, 8],
      
     3: [6], 35: [], 40: [], 12: [],
     8: [], 6: [], 15: []}

#adj=dict(sorted(adj.items(), key=lambda item: len(item[1])))
print(adj)
G=nx.Graph(adj)


#G = nx.petersen_graph()
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos,with_labels=True,node_size=1500,width=3)
# for path in nx.all_simple_paths(G,0,6):
#     if len(path)==10:
#         print(path)
# color=[]
#nx.draw(G,with_labels=1)

plt.show()