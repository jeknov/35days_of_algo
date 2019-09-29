
# coding: utf-8

# # Permutations
# 
# Given a collection of distinct integers, return all possible permutations.
# 
# **Example**:
# 
# Input: `[1,2,3]`
# 
# Output:
# `[
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]`

# In[1]:


def permutations(arr):
    '''
    arr - List[int]  
    rtype - res, List[List[int]]
    '''
    
    def permute(arr, perm, res):
        if len(arr) == 0:
            res.append(perm)
            
        for i in range(len(arr)):
            sublist = arr[:i] + arr[i+1:]
            permute(sublist, perm + [arr[i]], res)           
    
    res = []
    permute(arr, [], res)
    return res


# In[2]:


# Tests:
arr_list = [[1,2,3], [2,3,4,5]]


# In[3]:


def test(arr_list):
    for i, n in enumerate(arr_list):
        print("test No", i , ":\ntest list:", n, "\nResults:")
        print(permutations(n))
        print("*"*25, "\n")


# In[4]:


test(arr_list)


# **Time complexity**: O(n!)
