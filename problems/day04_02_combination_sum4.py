
# coding: utf-8

# # Combination Sum IV
# 
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# 
# **Example**:
# 
# nums = `[1, 2, 3]`
# 
# target = 4
# 
# The possible combination ways are:
# <pre>
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# </pre>
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.

# In[1]:


def comb_sum4(nums, target):
    if len(nums) == 0:
        return 0
    if target  == 0:
        return 1
    res = 0
    for i in range(len(nums)):
        if target >= nums[i]:
            res += comb_sum4(nums, target - nums[i])
    return res


# In[2]:


# Tests:
nums_list = [[1, 2, 3], [2, 4, 7], [1, 2]]
target_list = [4, 7, 6]


# In[3]:


def test(nums_list, target_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "target:", target_list[i], "\nResults:")
        print(comb_sum4(nums, target_list[i]))
        print("*"*25, "\n")


# In[4]:


test(nums_list, target_list)

