
# coding: utf-8

# # Sort Colors
# 
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this problem.
# 
# **Example**:
# 
# Input: `[2,0,2,1,1,0]`
# Output: `[0,0,1,1,2,2]`
# 
# **Follow up**:
# 
# A rather straight forward solution is a two-pass algorithm using counting sort.
# 
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 
# Could you come up with a one-pass algorithm using only constant space?

# In[1]:


def sort_colors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    r = 0
    w = 0
    b = len(nums) - 1
    
    while w < len(nums):
        if w > b:
            break
        if nums[w] == 0:
            nums[r], nums[w] = nums[w], nums[r]
            r += 1
            w += 1
        elif nums[w] == 1:
            w += 1
        elif nums[w] == 2:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
    
    return nums


# In[2]:


# Tests:
nums_list = [[2,0,2,1,1,0], [2, 2, 1, 0, 1, 1, 0, 0, 0, 2], []]


# In[3]:


def test(nums_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "\nResults:")
        print(sort_colors(nums))
        print("*"*25, "\n")


# In[4]:


test(nums_list)

