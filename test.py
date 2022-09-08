
import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

edge={
    0:[1,2],
    1:[3,4],
    2:[5,6],
    7:[8,9]
}
edges={ 3: [6], 1: [5, 3]}
T = nx.Graph(edges)
pos = graphviz_layout(T, prog="dot")
nx.draw(T, pos)
plt.show()