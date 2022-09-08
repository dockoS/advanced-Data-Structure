from operator import ge
from tkinter import HORIZONTAL
from webbrowser import get
from loguru import logger
import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
class BinomialTree:
    def __init__(self,data,index):
        self.data = data
        self.children=[]
        self.order=0
        self.index=index
        
        

class BinomialHeap:
    def __init__(self):
        self.heaps=[]
        self.max_order=0
        self.index_max=0
    
    def merge(self):
        def do_merge(order,time=0.5):
            self.build_graph(0.1)
            if len(stored_degree_heap[order])==2:
                heap1,heap2=stored_degree_heap[order]
                if heap1.data<heap2.data:
                    heap1.children.append(heap2)
                    heap1.order=order+1
                    stored_degree_heap[order+1].append(heap1)
                    
                else:
                    heap2.children.append(heap1)
                    heap2.order=order+1
                    stored_degree_heap[order+1].append(heap2)
                stored_degree_heap[order]=[]
                do_merge(order+1,0.2)
                return True
            else :
                return False        
        stored_degree_heap={i:[] for i in range(self.max_order+2)}
        for heap in self.heaps:
            stored_degree_heap[heap.order].append(heap)
            do_merge(heap.order)
        sub_heaps=[heap for heap in stored_degree_heap.values() if heap!=[] ]
        self.heaps=[sub_heap[0] for sub_heap in sub_heaps]
        if stored_degree_heap[self.max_order+1]!=[]:
            self.max_order+=1
    def insert(self,val,index):
        heap=BinomialTree(val,index)
        self.heaps.append(heap)
        self.merge()
    
    def build(self,arr):
        for i in range(len(arr)):
            self.insert(arr[i],i)
    def extract_min(self):
        min_candidates=[heap.data for heap in self.heaps]
        ind_min=np.argmin(min_candidates)
        heap_min=self.heaps[ind_min]
        
        children=heap_min.children
        self.heaps.remove(heap_min)
        self.heaps.extend(children)
        self.build_graph()
        self.merge()
        return heap_min.data
    def build_graph(self,time=0.5):
        def get_adj(heap,adj={}):
            print(heap.data)
            tab=[]
            for i in range(len(heap.children)):
                tab.append(heap.children[i].data)
                get_adj(heap.children[i],adj)
            adj[heap.data]=tab
            return adj
        for heap in self.heaps:
            adj=get_adj(heap)
            #adj_list.append(adj)
        adj=dict(sorted(adj.items(), key=lambda item: len(item[1]),reverse=True))
        G=nx.Graph(adj)
       
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos,with_labels=True,node_size=1500,width=3,node_color=node_colors)
        plt.pause(.5)
        plt.clf()
        
        
class BinomialTreeNavigation:
    def __init__(self,data,index):
        self.data = data
        self.children=[]
        self.pointerRightSibling=None
        self.pointerParent=None
        self.pointerLeftMostChild=None
        
    def getRank(self):
        return len(self.children)
    
        
class BinomialHeapNavigation:
    def __init__(self):
        self.heaps=[]
        self.max_order=0
        self.index_max=0
    def getMax_Order(self):
        return max([heap.getRank() for heap in self.heaps ])
    def merge(self,graphic=False):
        def add_new_child(parent,child):
            parent.pointerLeftMostChild=child
            child.pointerParent=parent
            if len(parent.children)==0:
                parent.children.append(child)
            else:
                child.pointerRightSibling=parent.children[0]
                parent.children.insert(0,child)
        def do_merge(order,time=1):
            if (graphic):
                self.build_graph()
            if len(stored_degree_heap[order])==2:
                parent,child=stored_degree_heap[order]
                if parent.data>child.data:
                    parent,child=child,parent
                add_new_child(parent,child)
                stored_degree_heap[order+1].append(parent)
                stored_degree_heap[order]=[]
                do_merge(order+1)
                return True
            else :
                return False
        stored_degree_heap={i:[] for i in range(self.getMax_Order()+2)}
        for heap in self.heaps:
            stored_degree_heap[heap.getRank()].append(heap)
            do_merge(heap.getRank())
        self.heaps=[heap[0] for heap in stored_degree_heap.values() if heap!=[] ]
 
    def insert(self,val,index,graphic=False):
        heap=BinomialTreeNavigation(val,index)
        self.heaps.append(heap)
        self.merge(graphic)
    
    def build(self,arr,graphic=False):
        for i in range(len(arr)):
            self.insert(arr[i],i,graphic)
    def extract_min(self,graphic=False):
        min_candidates=[heap.data for heap in self.heaps]
        ind_min=np.argmin(min_candidates)
        heap_min=self.heaps.pop(ind_min)
        children=heap_min.children
        for child in children:
            child.pointerParent=None
        children.reverse()
        self.heaps.extend(children)
        if graphic:
            self.build_graph()
        self.merge()
        return heap_min.data
    def get_heap(self,data):
        for heap in self.heaps:
            stack=[heap]
            while stack!=[]:
                current_node=stack.pop()
                print(current_node.pointerParent)
                if current_node.data==data:
                    return current_node
                for child in current_node.children:
                    stack.append(child)
        return None
            

    def decrease_key(self,data,new_data,graphic=False):
        if data<=new_data:
            return self.heaps
        heap_to_decrease=self.get_heap(data)
        if heap_to_decrease==None:
            logger.error("value not found")
            return self.heaps
        if graphic:
            self.build_graph(to_decrease=data,)
        heap_to_decrease.data=new_data
        if graphic:
            self.build_graph(0.1,to_decrease=new_data)
        while (heap_to_decrease.pointerParent!=None and heap_to_decrease.data<heap_to_decrease.pointerParent.data):  
            heap_to_decrease.data,heap_to_decrease.pointerParent.data=heap_to_decrease.pointerParent.data,heap_to_decrease.data
            heap_to_decrease=heap_to_decrease.pointerParent
            if graphic:
                self.build_graph(0.1,to_decrease=new_data)
        return self.heaps
            
    def deletion(self,data,graphic=False):
        self.decrease_key(data,0,graphic)
        self.extract_min()
        
    def build_graph(self,time=0.5,node_to_color=None,to_decrease=None):
        def get_adj(heap,adj={}):
            tab=[]
            for i in range(len(heap.children)):
                tab.append(heap.children[i].data)
                get_adj(heap.children[i],adj)
            adj[heap.data]=tab
            return adj
        for heap in self.heaps:
            adj=get_adj(heap)
            #adj_list.append(adj)
        adj=dict(sorted(adj.items(), key=lambda item: len(item[1]),reverse=True))
        print(adj)
        G=nx.DiGraph(adj)
        node_colors=[]
        for node in G:
            
            if node_to_color==node:
                node_colors.append('red')
            elif to_decrease==node:
                node_colors.append('green')
            else:
                node_colors.append("#1f78b4")
        #G = nx.petersen_graph()
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos,with_labels=True,node_size=1500,width=3,node_color=node_colors)
        plt.pause(.5)
        plt.clf()

    
        
        


class FibonacciTree:
    def __init__(self,data,index):
        self.data = data
        self.children=[]
        self.pointerRightSibling=None
        self.pointerLeftSibling=None
        self.pointerParent=None
        self.pointerLeftMostChild=None
        self.marked=False
        self.index=index
        
    def getRank(self):
        return len(self.children)
    
        
class FibonacciHeap:
    def __init__(self):
        self.heaps=[]
        self.pointerMin=None
        self.indexPointerMin=None
        self.marked_node=[]
        
    def getMax_Order(self):
        return max([heap.getRank() for heap in self.heaps ])
    def merge(self,graphic=False):
        def add_new_child(parent,child):
        
            if child.pointerLeftSibling!=None:
                child.pointerLeftSibling.pointerRightSibling=child.pointerRightSibling
            if child.pointerRightSibling!=None:
                child.pointerRightSibling.pointerLeftSibling=child.pointerLeftSibling
                
            child.pointerLeftSibling=None
            child.pointerParent=parent
            parent.pointerLeftMostChild=child
            child.pointerParent=parent
            if len(parent.children)==0:
                child.pointerRightSibling=None
                parent.children.append(child)
            else:
                child.pointerRightSibling=parent.children[0]
                parent.children[0].pointerLeftSibling=child
                parent.children.insert(0,child)
        def do_merge(order,time=0.5):
            if graphic:
                self.build_graph(0.1,self.pointerMin.data,marked=self.marked_node)
            if len(stored_degree_heap[order])==2:
                parent,child=stored_degree_heap[order]
                if parent.data>child.data:
                    parent,child=child,parent
                add_new_child(parent,child)
                
                stored_degree_heap[order]=[]
                stored_degree_heap[order+1].append(parent)
                
                do_merge(order+1,0.2)
                return True
            else :
                return False
        stored_degree_heap={i:[] for i in range(self.getMax_Order()+10)}
        for heap in self.heaps:
            stored_degree_heap[heap.getRank()].append(heap)
            do_merge(heap.getRank())
     
        self.heaps=[heap[0] for heap in stored_degree_heap.values() if heap!=[] ]
        self.indexPointerMin=self.heaps.index(self.pointerMin)
    def insert(self,val,index,graphic):
        heap=FibonacciTree(val,index)
        if self.heaps==[]:
            self.heaps.append(heap)
            self.pointerMin=heap
            self.indexPointerMin=0
        else:
            last_heap=self.heaps[-1]
            last_heap.pointerRightSibling,heap.pointerLeftSibling=heap,last_heap
            if self.pointerMin.data>heap.data:
                self.pointerMin=heap
                self.indexPointerMin=len(self.heaps)
            self.heaps.append(heap)
        if (graphic):
            self.build_graph(0.5,self.pointerMin.data)
    
    def build(self,arr,graphic=False):
        for i in range(len(arr)):
            self.insert(arr[i],i,graphic)
    def extract_min(self,graphic=False):
        min_heap=self.heaps.pop(self.indexPointerMin)
        if self.pointerMin.pointerLeftSibling!=None:
            self.pointerMin.pointerLeftSibling.pointerRightSibling=self.pointerMin.pointerRightSibling
        if self.pointerMin.pointerRightSibling!=None:
            self.pointerMin.pointerRightSibling.pointerLeftSibling=self.pointerMin.pointerLeftSibling
        min_children=self.pointerMin.children
      
        for child in min_children:
            child.pointerParent=None
        #min_children.reverse()
        
        self.heaps.extend(min_children)
        self.indexPointerMin=np.argmin([heap.data for heap in self.heaps])
        self.pointerMin=self.heaps[self.indexPointerMin]
        #self.build_graph(0.5,self.pointerMin.data)
        self.merge(graphic)
        return min_heap
    def get_heap(self,data):
        candidate_heap=None
        for heap in self.heaps:
            if heap.pointerLeftSibling==None:
                candidate_heap=heap
                break
        stack=[candidate_heap]
        while stack!=[]:
        
            current_node=stack.pop()
            if current_node.data==data:
                return current_node
            neighbors=[node for node in [current_node.pointerLeftMostChild,current_node.pointerRightSibling] if node!=None]
            for child in neighbors:
                stack.append(child)
        return None
            

    def decrease_key(self,data,new_data,graphic=False):
        if data<=new_data:
            return self.heaps
        heap_to_decrease=self.get_heap(data)
        if heap_to_decrease==None:
            logger.error(f"{data} value not found")
            return self.heaps
    
    
        #self.build_graph(0.1,new_data)
        if graphic:
            self.build_graph(time=2,node_to_color=self.pointerMin.data,to_decrease=heap_to_decrease.data,marked=self.marked_node)
        heap_to_decrease.data=new_data
        if graphic:
            self.build_graph(time=2,node_to_color=self.pointerMin.data,to_decrease=heap_to_decrease.data,marked=self.marked_node)
        
        if heap_to_decrease.pointerParent!=None and heap_to_decrease.data>=heap_to_decrease.pointerParent.data:
            return self.heaps
        def cut_node(node):
            
            node.marked=False
            if node.pointerParent==None:
                if node.data<self.pointerMin.data:
                    self.pointerMin=node
                    self.indexPointerMin=self.heaps.index(node)
            else:
                
                if node.data in self.marked_node:
                    self.marked_node.remove(node.data)
                    
                if node.pointerLeftSibling!=None:
                    node.pointerLeftSibling.pointerRightSibling=node.pointerRightSibling
                if node.pointerRightSibling!=None:
                    node.pointerRightSibling.pointerLeftSibling=node.pointerLeftSibling
                
                self.heaps[-1].pointerRightSibling,node.pointerLeftSibling=node,self.heaps[-1] 
                node.pointerRightSibling=None
                self.heaps.append(node)
                
                if node.data<self.pointerMin.data:
                    self.pointerMin=node
                    self.indexPointerMin=len(self.heaps)-1
                parent=node.pointerParent
                node.pointerParent=None
                index_node=parent.children.index(node)
                parent.children.remove(node)
                if index_node==0 and len(parent.children)>0:
                    parent.pointerLeftMostChild=parent.children[0]
                if index_node==0 and len(parent.children)==0:
                    parent.pointerLeftMostChild=None
                
                if parent.marked:
                    cut_node(parent)
                elif parent.pointerParent!=None:
            
                    parent.marked=True
                    self.marked_node.append(parent.data)
            if graphic:
                self.build_graph(time=2,node_to_color=self.pointerMin.data,marked=self.marked_node)
               
        cut_node(heap_to_decrease)       
        return self.heaps
            
    def deletion(self,data):
        self.decrease_key(data,0)
        self.extract_min()
        
    
        
        
        
        
        pass
    def build_graph(self,time=2,node_to_color=None,to_decrease=None,marked=[]):
        def get_adj(heap,adj={}):
            tab=[]
            for i in range(len(heap.children)):
                tab.append(heap.children[i].data)
                get_adj(heap.children[i],adj)
            adj[heap.data]=tab
            return adj
        for heap in self.heaps:
            adj=get_adj(heap)
            #adj_list.append(adj)
        adj=dict(sorted(adj.items(), key=lambda item: len(item[1]),reverse=True))
        G=nx.DiGraph(adj)
        node_colors=[]
        for node in G:
            if node==to_decrease:
                node_colors.append("green")
            elif node_to_color==node:
                node_colors.append('red')
            elif node in marked:
                node_colors.append("yellow")
            else:
                
                node_colors.append("#1f78b4")
        
        #G = nx.petersen_graph()
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos,with_labels=True,node_size=1500,width=2,node_color=node_colors)
        plt.pause(.5)
        plt.clf()

    
    
    
    
    
import numpy as np
arr=[15, 2, 3, 6, 7, 8
    , 9,12,40,20,10]
      #,35,1,26,41,52,33,17,48]
arr=[15, 2, 3, 6, 7, 8, 9,12,40,20,10,35,1,26,41,52,33,17,48]
#arr=np.random.choice(range(1,100),90,replace=False)
#binomial Heap


debut=time.time()
binomial_heaps=BinomialHeapNavigation()   
binomial_heaps.build(arr,True)
#binomial_heaps.extract_min(graphic=True)
# binomial_heaps.extract_min(graphic=True)
# binomial_heaps.extract_min(graphic=True)
# binomial_heaps.extract_min(graphic=True)
# binomial_heaps.extract_min(graphic=True)

# # heaps.extract_min(graphic=True)


# binomial_heaps.decrease_key(12,1,True)

# binomial_heaps.decrease_key(40,11,True)


binomial_heaps.decrease_key(41,5,True)

binomial_heaps.decrease_key(33,6,True)
binomial_heaps.extract_min(graphic=True)
# binomial_heaps.decrease_key(48,11,True)
# binomial_heaps.decrease_key(8,1,True)


fin_Sim_binomial=time.time()
#time.sleep(5)

# Fibonacci Heap
# fibonacci_heaps=FibonacciHeap()   
# fibonacci_heaps.build(arr,True)
# fibonacci_heaps.extract_min(graphic=True)
# fibonacci_heaps.extract_min(graphic=True)
# fibonacci_heaps.extract_min(graphic=True)
# fibonacci_heaps.extract_min(graphic=True)
# #fibonacci_heaps.extract_min(graphic=True)


# # heaps.extract_min(graphic=True)


# fibonacci_heaps.decrease_key(12,1,True)
# # logger.error(fibonacci_heaps.marked_node)
# fibonacci_heaps.decrease_key(40,11,True)
# # logger.error(heaps.marked_node)

# fibonacci_heaps.decrease_key(41,5,True)
# # # logger.error(heaps.marked_node)
# # fibonacci_heaps.decrease_key(52,7,True)
# # # logger.error(heaps.marked_node)

# fibonacci_heaps.decrease_key(33,6,True)
# fibonacci_heaps.extract_min(graphic=True)


# fin_Sim_fibonacci=time.time()


#logger.success(f" simulation binomial= {fin_Sim_binomial-debut} et simulation fibionacci= {fin_Sim_fibonacci-fin_Sim_binomial}")
# logger.error(heaps.marked_node)
#heaps.merge(True)





plt.show()
