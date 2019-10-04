
# coding: utf-8

# # Kth Largest Element in an Array
# 
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 
# **Example 1**:
# 
# Input: `[3,2,1,5,6,4]` and `k` = `2`
# 
# Output: `5`
# 
# **Example 2**:
# 
# Input: `[3,2,3,1,2,4,5,5,6]` and `k` = `4`
# 
# Output: `4`
# 
# Note: 
# 
# You may assume `k` is always valid, 1 ≤ `k` ≤ array's length.

# In[1]:


def kth_largest(nums, k):
    return sorted(nums)[-k]


# In[2]:


# Tests:
nums_list = [[3,2,3,1,2,4,5,5,6], [3,2,1,5,6,4]]
k_list = [4, 2]


# In[3]:


def test(nums_list, k_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "k:", k_list[i], "\nResults:")
        print(kth_largest(nums, k_list[i]))
        print("*"*25, "\n")


# In[4]:


test(nums_list, k_list)

