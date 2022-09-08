from encodings import search_function
from faulthandler import disable
import numpy as np
from loguru import logger
import random
import networkx as nx
import  matplotlib.pyplot as plt
from functools import reduce
from matplotlib import  animation
random.seed(10)
def salesman_travelling(nbr_nodes,start_point,size_pop,mut_prob=0.1,nbr_generations=100,threshold=0.01,sexy_init_gene_population=False):
    G=nx.complete_graph(nbr_nodes)
    for e in G.edges:
        G.edges[e]["distance"]=random.randint(10,100)
    def populate():
        global population
        population=[]
        populations=[]

        if start_point>=nbr_nodes:
            raise Exception("Bad starting point or ending point: must be less than the numbre of nodes")
        nodes=list(range(nbr_nodes))
        nodes.remove(start_point)
        if sexy_init_gene_population:
            
            for target in nodes:
                populations.append([path for path in nx.all_simple_paths(G,start_point,target) if len(path)==nbr_nodes])
            end_nodes=np.random.choice(range(nbr_nodes-1),size_pop)
            for node in end_nodes:
                random_path=populations[node][np.random.randint(0,nbr_nodes)]
                rand_path_copy=random_path.copy()
                rand_path_copy.append(start_point)

                population.append(rand_path_copy)
        else:
            for i in range(size_pop):
                individual=np.random.choice(nodes,size=len(nodes),replace=False)
                individual=list(individual)
                individual.append(start_point)
                individual.insert(0,start_point)
                population.append(individual)
            print(population)
            pass


   

    def path_distance(individual):
        distance=0
        for i in range(len(individual)-1):
            distance+=G.adj[individual[i]][individual[i+1]]['distance']
        #distance=reduce((lambda edge1,edge2: G.adj[edge1[0]][edge1[1]]["distance"] +G.adj[edge2[0]][edge2[1]]["distance"] ),tuple_pop)

        return distance
    def paths_distances(population):
        return np.asarray(list(map(path_distance,population)))
    def generer_parents(distances):
        
        probability=(1-distances/sum(distances))*100
        probability=probability/sum(probability)

        parents_tuple=[]
        for i in range(len(distances)//2):
            tuple=np.random.choice(range(len(distances)),size=2,replace=False,p=probability)
            parents_tuple.append(tuple)
        return np.asarray(parents_tuple)

            
    def cross_over():
        global population
        distances=paths_distances(population)
        parents_tuple=generer_parents(distances)
        new_population=[]
        logger.error("before cross over")
        for parents in parents_tuple:
            cross_over_point=np.random.randint(1,len(population)-1)
            child1=list(population[parents[0]])
            child2=list(population[parents[1]])
            # logger.error(f"child1 {child1}")
            # logger.success(f"child2 {child2}")
   

       
            
            for j in range(cross_over_point,len(child1)-1):
                """si on permute les valeurs de la position correspondante  dans
                chaque fils alors les fils auront des valeurs dupliquées .Pour eviter cela nous alons trouver les valeurs 
                dupliquées correspondant dans la partie non modifiée et les permuter
                """
                pos1=child1.index(child2[j])
                pos2=child2.index(child1[j])
                
                child1[j],child2[j]=child2[j],child1[j]
                child1[pos1],child2[pos2]=child2[pos2],child1[pos1]
            #child1[cross_over_point:len(population)-1],child2[cross_over_point:len(population)-1]=child2[cross_over_point:len(population)-1],child1[cross_over_point:len(population)-1]
 
            # logger.error(f"child1 {child1}")
            # logger.success(f"child2 {child2}")
            candidates=[population[parents[0]],population[parents[1]],child1,child2]
            distances=paths_distances(candidates)
            
            new_population.append(candidates[np.argmin(distances)])
            distances[np.argmin(distances)]=10000000000
            new_population.append(candidates[np.argmin(distances)])
        logger.error("After cross over")

        population=np.asarray(new_population)



    def get_shortest_path(population):
        distances=paths_distances(population)
        return population[np.argmin(distances)]
    """On veut pas changer un noeud par le noeud
    de depart ou d'arrivee"""
    def get_nearest_node_to(node):
        nearest_node=min(G.adj[node],key=lambda u:G.adj[node][u]["distance"])
        return nearest_node if nearest_node!=start_point else node
    def mutation():
        """if mutation prob is less than mut_prob then we permute the 
        node with the nearest node of the starting point """
        logger.success("begin mutation")

        for i in range(population.shape[0]):
            
 
            for j in range(1,population.shape[1]-1):
                r=np.random.randn()
                if r<=mut_prob:
                    nearest_node=get_nearest_node_to(population[i][j])
                    if nearest_node!=population[i][j]:
                        index_nearest_node=list(population[i]).index(nearest_node)
                        population[i][index_nearest_node],population[i][j]=population[i][j],population[i][index_nearest_node]
        logger.success("end mutation")
    def draw_shortest_path(shortest_path):
        route_edges = [(shortest_path[n],shortest_path[n+1]) for n in range(len(shortest_path)-1)]
        pos = nx.spring_layout(G)
        #nx.draw_networkx_nodes(G,pos=pos)
        #nx.draw_networkx_labels(G,pos=pos)
        nx.draw(G,pos=pos,edgelist=route_edges,edge_color = 'r',with_labels=True)
        plt.pause(0.001)
        plt.clf()
    generation=0
    history_mean_distance=[]
    history_shortest_path=[]
    previous_mean_distance=np.inf
    populate()
    while (generation<nbr_generations):
        logger.success(f"Begin generation number: {generation}")

        distances=paths_distances(population)
        shortest_path=get_shortest_path(population)
        history_mean_distance.append(np.mean(distances))
        history_shortest_path.append(shortest_path)
        cross_over()
        if np.abs(np.mean(distances)-previous_mean_distance)<=threshold:
            break
        previous_mean_distance=np.mean(distances)
        mutation()
        logger.error(f"the shortest path is {shortest_path}")
        logger.success(f"End generation numbre: {generation}")
        draw_shortest_path(shortest_path)
        generation+=1
    return population,paths_distances(population),history_mean_distance,history_shortest_path
_,_,history_mean_distance,_=salesman_travelling(10,0,30,nbr_generations=1000)
logger.success(history_mean_distance)
generations=range(len(history_mean_distance))
plt.plot(generations,history_mean_distance)
plt.show()
#logger.error(history_path)