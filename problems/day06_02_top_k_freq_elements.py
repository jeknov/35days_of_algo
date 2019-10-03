
# coding: utf-8

# # Top K Frequent Elements
# 
# Given a non-empty array of integers, return the k most frequent elements.
# 
# **Example 1**:
# 
# Input: `nums` = `[1,1,1,2,2,3]`, `k` = 2
# 
# Output: `[1,2]`
# 
# **Example 2**:
# 
# Input: `nums` = `[1]`, `k` = 1
# 
# Output: `[1]`
# 
# Note:
# 
# - You may assume k is always valid, 1 ≤ `k` ≤ number of unique elements.
# - Your algorithm's time complexity must be better than `O(n*logn)`, where `n` is the array's size.

# In[1]:


def top_k_freq_elements(nums, k):
    
    if len(nums) == 1: # if nums contains one element only, this element is the most frequent one
        return nums
    
    hashmap = {}
    count = 0
    for each in nums:
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1
            
    if len(hashmap) == len(nums): # means that list contains each element once
        return list(hashmap.keys())[:k]    # any top-k elements can be returned in this case
    else:
        return sorted(hashmap, key=hashmap.get, reverse = True)[:k] # hashmap is sorted and top-k elements returned


# In[2]:


# Tests:
nums_list = [[1,2,1,2,1,3,3,4,5,6], [4,3,6,2,7,5], [1]]
k_list = [3, 3, 1]


# In[3]:


def test(nums_list, k_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "k:", k_list[i], "\nResults:")
        print(top_k_freq_elements(nums, k_list[i]))
        print("*"*25, "\n")


# In[4]:


test(nums_list, k_list)

