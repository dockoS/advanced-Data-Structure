from asyncio import sleep
from cProfile import label
from operator import ne
from textwrap import indent
import networkx as nx
import random
from loguru import logger
import matplotlib.pyplot as plt
edges=[("a","b"),("a","c"),("c","e"),("b","d"),("d","f"),("f","g"),("b","g"),("c","f"),("f","i")]
G=nx.DiGraph()
G.add_edges_from(edges)
#G=nx.random_k_out_graph(5,k=2,alpha=4,self_loops=False)


def depth_breadth_search(G,source,depth=True):
    edges=G.edges()
    nodes=G.nodes()

    color_edges=["b" for _ in range(len(edges))]
    color_nodes=["skyblue" if node!=source else "green" for node in nodes]
    #color_nodes[source]="green"
    pos=nx.spring_layout(G)

    stack=[source]
    while len(stack)!=0:
        if depth:
            index=-1
        else:
            index=0
        current_node=stack[index]
        logger.success(f"node {current_node}")
        stack.remove(current_node)
        for neighbor in G.neighbors(current_node):
            stack.append(neighbor)
            if (current_node,neighbor) in list(edges):
                edge_index=list(edges).index((current_node,neighbor))
            else:
                edge_index=list(edges).index((neighbor,current_node)) 
            color_edges[edge_index]="r"
            nx.draw(G,with_labels=True,pos=pos, node_color=color_nodes, node_size=1500,width=3,edge_color=color_edges)
            plt.pause(1)
            plt.clf()
    logger.error("Program End")    

    plt.text(x=10,y=10,s="End simulation")
    plt.show()
def has_path(G,source,target,depth=True):
    edges=G.edges()
    nodes=G.nodes()

    color_edges=["b" for _ in range(len(edges))]
    color_nodes=["skyblue" if node!=source and node!=target else "green" for node in nodes]
    pos=nx.spring_layout(G)

    stack=[source]
    while len(stack)!=0:
        if depth:
            index=-1
        else:
            index=0
        current_node=stack[index]
        logger.success(f"node {current_node}")
        stack.remove(current_node)
        for neighbor in G.neighbors(current_node):
            stack.append(neighbor)
            if (current_node,neighbor) in list(edges):
                edge_index=list(edges).index((current_node,neighbor))
            else:
                edge_index=list(edges).index((neighbor,current_node)) 
            color_edges[edge_index]="r"
            nx.draw(G,with_labels=True,pos=pos, node_color=color_nodes, node_size=1500,width=3,edge_color=color_edges)
            plt.pause(1)
            plt.clf()
            if current_node==target:
                return True
    
    logger.error("Program End")
    return False    
#depth_breadth_search(G,"a")
#logger.info(has_path(G,"a","f",False))
#nx.draw(G,with_labels=True, node_color='skyblue', node_size=1500,width=3,edge_color=color_edges)
adj_list={
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
G=nx.Graph(adj_list)
def connected_components_count(graph):
    pos=nx.circular_layout(G)
    edges=G.edges()
    color_edges=["b" for _ in range(len(edges))]
    def depth_search(graph,src,color="b"):
        stack=[src]
        visited_nodes=[]
        while(len(stack)!=0):
            current_node=stack[-1]
            stack.remove(current_node)
            for neighbor in graph[current_node]:
                if neighbor  not in visited_nodes:
                    visited_nodes.append(neighbor)
                    stack.append(neighbor)
                if (current_node,neighbor) in list(edges):
                    edge_index=list(edges).index((current_node,neighbor))
                else:
                    edge_index=list(edges).index((neighbor,current_node)) 
                color_edges[edge_index]=color
                nx.draw(G,with_labels=True,pos=pos, node_size=1500,width=3,edge_color=color_edges)
                plt.pause(1)
                plt.clf()
            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
        return visited_nodes
    nodes=graph.nodes()
    color=["r","g"]
    visited_nodes=[]
    cpt=0
    for node in nodes:
        if node not in visited_nodes:
            cpt+=1
            visited_nodes.extend(depth_search(graph,node,color[cpt%len(color)]))
    return cpt


def island_count(grid):
    def get_neighbors(i,j,len_i,len_j):
        neighbors=[( i-1,j) if i>0 else None,(i+1,j) if i<len_i-1 else None, ( i,j-1) if j>0 else None,(i,j+1) if j<len_j-1 else None]
        while(None in neighbors):
            neighbors.remove(None)
        return neighbors
    visited_land=[]
    cpt_land=0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="W" or (i,j) in visited_land:
                continue          
            stack=[]
            print(cpt_land)
            print(i,j)
            stack.append((i,j))
            cpt_land+=1
            while (len(stack)!=0):
          
                current_land=stack[-1]
                stack.remove(current_land)
        
                if current_land not in visited_land:
                    visited_land.append(current_land)
                # logger.error(stack)
                neighbors=get_neighbors(*current_land,len(grid),len(grid[0]))
                
                #break
                for m,n in neighbors:
                    if grid[m][n]=="L" and (m,n) not in visited_land:
                        stack.append((m,n))
                        visited_land.append((m,n))
                
          
    return cpt_land
grid=[
    ["W","L","W","W","W"],
    ["W","L","W","W","W"],
    ["W","W","W","L","W"],
    ["W","W","L","L","W"],
    ["L","W","W","L","L"],
    ["L","L","W","W","W"]
]
grid2=[
    ["W","L","W","W"],
    ["L","L","L","W"],
    ["W","W","W","W"],
    ["W","W","W","W"],

]
logger.success(island_count(grid))
#logger.success(connected_components_count(G))


