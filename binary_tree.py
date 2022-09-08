import math
from operator import le
from turtle import right
from loguru import logger

class Node:
    def __init__(self,parent,right=None,left=None) -> None:
        self.parent=parent
        self.left=left
        self.right=right


a=Node("a")
b=Node("b")
c=Node("c")
a.right=b
a.left=c

def depth_first_values(root):
    result=[]
    if root==None:
        return result
    stack=[root]

    while(len(stack)!=0):
        current_node=stack.pop()
        if current_node.right!= None:
            stack.append(current_node.right)
        if current_node.left !=None:
            stack.append(current_node.left)
        result.append(current_node.val)
    return result

def treeSum(root):
    if root==None:
        return 0
    return root.parent+treeSum(root.right)+treeSum(root.left)

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
#    / \
# None  None   

#print(treeSum(a) )# -> 21

def tree_include(root,target):
    if root==None:
        return False
    if root.parent==target:
        return True       
    return tree_include(root.left,target) or tree_include(root.right,target)
    
        


def tree_min_value(root):
    if root==None:
        return math.inf
    return min([root.parent,tree_min_value(root.left),tree_min_value(root.right)])
    
#print(tree_min_value(a)) 


def max_root_to_path_sum(root):
    if root==None:
        return (-1)*math.inf
    if root.left==None and root.right==None:
        return root.parent
    return root.parent+ max([max_root_to_path_sum(root.left),max_root_to_path_sum(root.right)])
#print(max_root_to_path_sum(a))
#print(-2>(-1)*math.inf)


class Heap:
    def __init__(self,arr):
        self.heap=arr
    
    def upShift(self,index):
        i=index
        while ((i-1)//2)>=0:
            if  self.heap[(i-1)//2]<self.heap[i]:
                break
            self.heap[(i-1)//2],self.heap[i]= self.heap[i],self.heap[(i-1)//2]
            i=(i-1)//2
        return self.heap
            

            
        
        
    def downShift(self,index):
        i=index
        while(((2*i)+1) <len(self.heap)):
            left=(2*i)+1   
            right=(2*i)+2

            if right<len(self.heap):
                
                if self.heap[i]<=self.heap[left] and   self.heap[i]<=self.heap[right]:
                    break
                min_child=min([(self.heap[left],left),(self.heap[right],right)])
                self.heap[i],self.heap[min_child[1]]=self.heap[min_child[1]],self.heap[i]
                i=min_child[1]
            else:
                if self.heap[i]<=self.heap[left]:
                    break
                self.heap[i],self.heap[left]=self.heap[left],self.heap[i]
                i=left
         
        return self.heap
        
    def heapfy_up(self):
        #base case 
        for i in range(len(self.heap)):
            self.upShift(i)
        return self.heap
    
    def heapfy_down(self):
        for i in range(len(self.heap)-1,-1,-1):
            print(i)
            self.downShift(i)
        return self.heap
    def get_max(self):
        self.heapfy_down() 
        i=len(self.heap)-1
        values=[]
        while ((2*i)+1)>=len(self.heap):
            values.append((self.heap[i],i))
            i-=1
        return max(values)
    def insert(self,value):
        self.heap.append(value)
        self.upShift(len(self.heap)-1)         
        return self.heap
    
    def extract_min(self):
        #swap last and first indexes
     
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        self.heap.pop()
        self.downShift(0)
        return self.heap
    
    
arr=[10,3, 6, 2]

arr=[10,9,12,6,4,8,2]

h=Heap(arr)
# print("before up")
print(h.heap)
# print("after Up")


print(h.heapfy_down())

print(h.heapfy_up())
# logger.error(h.insert(1))
# logger.success(f"valeur max = {h.get_max()}")

# logger.error(h.extract_min())
#h.upShift(0)
#print(h.heap)
