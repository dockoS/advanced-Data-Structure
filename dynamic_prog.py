from loguru import logger
import numpy as np
import time
# [2,5,3,0,10,8]
# ouptpu=3 =2->3->8
# il faut que la valeur a la position de i soit inferieure a la valeur qui se trouve a la position 
# index pour qu'on le prend comme fin d'un sub problem
def longest_inscreasing_subseq(array,index):
    def count_LIS(sub_array):
        def get_neigbors(node_pos):
            neigbors=[]
            if node_pos==len(sub_array)-1:
                return neigbors
            for node in all_edges[node_pos]:
                neigbors.append(node)
            return neigbors
        def get_max_lenght_LIS():
            count_paths=[]
            for i in range(len(sub_array)-1):
                count_path=0
                if len(sub_array)-1 not in get_neigbors(i):
                    count_paths.append(0)
                    continue
                logger.info(f"pos= {i} node={sub_array[i]}")
                logger.info(f"neighbor= {get_neigbors(i)}")
                
                stack=[i]
                
                while len(stack)!=0:
                    count_path+=1
                    current_node=stack.pop()
                    for k in get_neigbors(current_node):   
                        stack.append(k)
                    if(len(sub_array)-1) in stack:
                        count_paths.append(count_path)
                        break
                      
                if len(stack)==0:
                    count_paths.append(0)          
            return max(count_paths)
        all_edges=[]
        for j in range(len(sub_array)-1):
            edges=[]
            for k in range(j+1,len(sub_array)):
                if sub_array[j]<sub_array[k]:
                    edges.append(k)
             
            all_edges.append(edges)
    
        return get_max_lenght_LIS()
        #lenght_paths=[]
        
                
                
    
            
    sub_LIS=[]
    for i in range(1,index+1):
        if array[i]<=array[index]:
            sub_array=array[:i+1]
            logger.success(f"sub prob {sub_array}")
            sub_LIS.append(count_LIS(sub_array))
        logger.error(sub_LIS)
    return 1+max(sub_LIS)
        
#array=[3,1,8,2,5]
#logger.success(longest_inscreasing_subseq(array,4))

def LIS(array,index_target,target):
    #base case
    if index_target==0:
        return 1
    tab=[]
    for k in range(index_target-1,-1,-1):
        if array[k]<=target:
            tab.append(LIS(array,k,array[k]))
    return 1+max(tab) if tab!=[] else 1


def LIS_memorization(array,index_target,target,memorization_cache={}):
    if  index_target not in memorization_cache.keys():
        #base case
        if index_target==0:
            memorization_cache[0]=1
        else:
            #smallest step
            tab=[]
            for k in range(index_target-1,-1,-1):
                if array[k]<=target:
                    tab.append(LIS_memorization(array,k,array[k],memorization_cache))
            value=1+max(tab) if tab!=[] else 1
            memorization_cache[index_target]=value
    return memorization_cache[index_target]


arr=[3,7,4,6,2,8]
#logger.success(LIS_iterative(arr,len(arr)-1))
#logger.error(LIS(arr,len(arr)-1,8))
array=np.random.randint(0,50,size=(10))


#array=[80, 72 ,25,  7, 55,  3, 17, 52, 50, 95]
def LIS_sequences(array,index_target,target,sequence_element=[[]],memorization_cache={}):
    #base case
    def get_sequence_max():
        j=len(sequence_element)-1
        if sequence_element[j]==[]:
            return []
        sequences=[array[j]]
        while(j>0 and max(sequence_element[j])!=-1):
            j=sequence_element[j].index(max(sequence_element[j]))
            sequences.append(array[j])
        sequences.reverse()
        return sequences
    
    if index_target not in memorization_cache.keys():
        if index_target==0:
                memorization_cache[0]= 1,[array[0]]
        else:
            tab=[-1]*(index_target)
            for k in range(index_target-1,-1,-1):
                if array[k]<=target:
                    tab[k]=LIS_sequences(array,k,array[k],sequence_element,memorization_cache)[0]
            sequence_element[index_target]=tab
            memorization_cache[index_target]=1+max(tab) if max(tab) !=-1 else 1,get_sequence_max() #,list(map(lambda x:array[x],sequence_element))
    return memorization_cache[index_target]
#array=[ 1, 12,  6, 34,  7,  3, 43, 43,  1, 43]
# time_deb=time.time()
# logger.error(f"LIS recursive  memorization ={LIS_memorization(array,len(array)-1,array[len(array)-1])}")
# time_rec_fin=time.time()
# time_rec=time_rec_fin-time_deb
#logger.error(f"LIS recursive sequence ={LIS_sequences(array,len(array)-1,array[len(array)-1],[[]]*len(array))}")
# time_ite=time.time()-time_rec_fin
# print(array)

# logger.success(f"rec memo time is : {time_rec} and time rec simple= {time_ite}")
def get_sequence_max(text1,text2,sequence_element):
    j=len(sequence_element)-1
    if sequence_element[j]==[]:
        return []
    if text2[j] in text1:
        sequences=[text2[j]]
    else:
        sequences=[]
    while(j>0 and max(sequence_element[j])!=-1):
        j=sequence_element[j].index(max(sequence_element[j]))
        sequences.append(text2[j])
    sequences.reverse()
    return sequences

def lengthCommonSubsequence(text1,text2,index_text2,sequence_element=[[]],memorization_cache={}):
    if index_text2 not in  memorization_cache.keys():
        if index_text2==0 :
            if text2[index_text2] in text1:
                memorization_cache[0]=1,[text2[0]]
            else:
                memorization_cache[0]=0,[]
        else:
            tab=[-1]*(index_text2)
            for k in range(index_text2-1,-1,-1):
                occ_in_text1=[i for i,val in enumerate(text1) if val==text2[k]]
                if text2[k] in text1 and text1.index(text2[k])<=max(occ_in_text1):
                    tab[k]=lengthCommonSubsequence(text1,text2,k,sequence_element,memorization_cache)[0]
            sequence_element[index_text2]=tab
            print(tab)
            if text2[index_text2] in text1:
                memorization_cache[index_text2]=1+ max(tab) if max(tab)!=-1 else 0s,"".join(get_sequence_max(text1,text2,sequence_element))
            else:
                memorization_cache[index_text2]=max(tab) if max(tab)!=-1 else 0,"".join(get_sequence_max(text1,text2,sequence_element))
    return memorization_cache[index_text2]

def longestCommonSubsequence(text1: str, text2: str):  
    small_text,longest_text=text2,text1
    if len(small_text)>len(longest_text):
        small_text,longest_text=longest_text,small_text
    return lengthCommonSubsequence(longest_text,small_text,len(small_text)-1,[[]]*len(small_text),{})




text1="abc"
text2="def"   
text2="bl"
text1="yby"

text1="psnw"
text2="vozsh"
#text2="yclbb"
#text1="ycslcùmsy"
#text1="ezupkr"
#text2="ubmrapg"
#text1="abcde"
#text2="ace"
#text2="abcba"
#text1="abcbcba"
#text2="aacsdaabaabvc"
#text1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#print(lengthCommonSubsequence(text1,text2,len(text2)-1,[[]]*len(text2)))
    #atomic step:
print(longestCommonSubsequence(text1,text2))
#print(len(text1))
