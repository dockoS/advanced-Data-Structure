from operator import le
from turtle import right
from loguru import logger
def reverse_string(string):
    if len(string)==0:
        return ""
    return string[-1]+reverse_string(string[:-1])
string="the simple engineer"    


def palindrome(str):
    if len(str)==0 or len(str)==1:
        return True
    if str[0]==str[-1]:
        return palindrome(str[1:-1])
    else:
        return False
    

#print(str[:-1])
#print(palindrome("racecar"))

def decimal_to_binary(number):
    if number==1:
        return ""
    return decimal_to_binary(number//2)+str(number%2)
def recursiveSum(N):
    if N==1:
        return 1
    return N+recursiveSum(N-1)

def binary_search(arr,left,right,val):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==val:
        return mid
    if val>arr[mid]:
        return binary_search(arr,mid+1,right,val)
    else:
        return binary_search(arr,left,mid-1,val)


arr=[1,3,5,7,8,10]
#print(binary_search(arr,0,len(arr)-1,11))
def merge_sort(array,start,end):

    if start==end and start<len(array):
        return [array[start]]
    if start==end and start==len(array):
        return [array[-1]]
    #sorted_array=array[start]
    mid=(start+end)//2
    merge_sort(array,start,mid)
    merge_sort(array,mid+1,end)
    return sorting_array(array,start,mid,end)

    
def sorting_array(array,start,mid,end):
    left=array[start:mid+1]
    right=array[mid+1:end+1]
    sorted_array=array[start:end+1].copy()
    point_left=0
    point_right=0
    
    while(point_left!=len(left) and point_right!=len(right)):
        if left[point_left]<right[point_right]:
            sorted_array[point_left+point_right]=left[point_left]   
            point_left+=1
        else:
            sorted_array[point_left+point_right]=right[point_right]   
            point_right+=1
        if point_left==len(left):
            sorted_array[point_left+point_right:]=right[point_right:]
        if point_right==len(right):
            sorted_array[point_right+point_left:]=left[point_left:]
        # logger.error(f"sorted={sorted_array}")
        # print(f"left={point_left} right={point_right}")
    array[start:end+1]=sorted_array
    return array
array=[7,3,2,5,4,5]
#print(merge_sort(arr,0,len(arr)-1))

# linked list= 2->4->5->3->7
# output 7->3->5->4->2
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None


def linked_list_reversal(head):
    if head==None or head.next==None:
        return head
    p=linked_list_reversal(head.next)
    head.next.next=head
    head.next=None
    return p

A=Node(1)
a=Node(2)
b=Node(3)
c=Node(4)
A.next=a
a.next=b
b.next=c

B=Node(7)
a1=Node(11)
b1=Node(20)
c1=Node(25)
B.next=a1
a1.next=b1
b1.next=c1
#head2=linked_list_reversal(head)

# while (head2!=None):
#     print(head2.value)
#     head2=head2.next

def merge_two_linked_list(A,B):
    #Bases cases
    if (A==None):
        return B
    if (B==None):
        return A
     # recursion call
    
    if A.value<B.value:
        A.next=merge_two_linked_list(A.next,B)
        return A
    else:
        B.next=merge_two_linked_list(A,B.next)
        return B
print(merge_two_linked_list(A,B))
