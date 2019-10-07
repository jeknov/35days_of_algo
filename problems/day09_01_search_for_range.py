
# coding: utf-8

# # Search for a Range
# 
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return `[-1, -1]`.
# 
# **Example 1**:
# 
# Input: nums = `[5,7,7,8,8,10]`, target = `8`
# 
# Output: `[3,4]`
# 
# **Example 2**:
# 
# Input: nums = `[5,7,7,8,8,10]`, target = `6`
# 
# Output: `[-1,-1]`

# In[1]:


def search_for_range(nums, target):
    
    leftInd = binarySearch(nums, target, True)
        
    if len(nums) < 1 or leftInd == len(nums) or nums[leftInd] != target:
        return [-1, -1]

    return [leftInd, binarySearch(nums, target, False) - 1]

def binarySearch(nums, target, isLeft):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target or (isLeft and nums[mid] == target):
            right = mid
        else:
            left = mid + 1
    return left


# In[2]:


# Tests
nums_list = [[5,7,7,8,8,10], [5,7,7,8,8,10]]
target_list = [8, 6]


# In[3]:


def test(nums_list, target_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "target:", target_list[i], "\nResults:")
        print(search_for_range(nums, target_list[i]))
        print("*"*25, "\n")


# In[4]:


test(nums_list, target_list)

