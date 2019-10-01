
# coding: utf-8

# # Subsets
# 
# Given a set of distinct integers, `nums`, return all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# **Example**:
# 
# Input: nums = `[1,2,3]`
# 
# Output:
# `[
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]`

# In[1]:


def subsets(nums):
    
    def helper(nums, subset, ind, results):
        results.append(subset[:])
        for i in range(ind, len(nums)):
            helper(nums, subset+[nums[i]], i+1, results)
        
    results = []
    helper(nums, [], 0, results)
    return results


# In[2]:


# Tests:
nums_list = [[1, 2, 3], [2, 4, 7], [1, 2]]


# In[3]:


def test(nums_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "\nResults:")
        print(subsets(nums))
        print("*"*25, "\n")


# In[4]:


test(nums_list)


# In[ ]:






