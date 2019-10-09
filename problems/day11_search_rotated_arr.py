
# coding: utf-8

# # Search in Rotated Sorted Array
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# **Example 1**:
# 
# Input: nums = `[4,5,6,7,0,1,2]`, target = `0`
# 
# Output: `4`
# 
# **Example 2**:
# 
# Input: nums = `[4,5,6,7,0,1,2]`, target = `3`
# 
# Output: `-1`

# In[1]:


def search_rotated_array(nums, target):
    
    # First, find a rotation index:
    s = 0
    e = len(nums) - 1
    while s < e:
        mid = (s+e)//2
        if nums[s] < nums[e] or nums[mid] < nums[s]:
            e = mid
        else:
            s = mid+1

    rot_ind = s
        
    # Now, 
    if nums[rot_ind] == target:
        return rot_ind
    
    if target > nums[0]:
        s = 0
        e = rot_ind
        flag = "left"
    elif target < nums[0]:
        s = rot_ind
        e = len(nums) - 1
        flag = "right"
    else:
        return 0
    
    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == target:
            if flag == "left":
                return mid
            elif flag == "right":
                return mid + rot_ind
        elif target > nums[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return -1
        


# In[2]:


# Tests:
nums_list = [[4,5,6,7,0,1,2], [4,5,6,7,0,1,2]]
t_list = [0, 3]


# In[3]:


def test(nums_list, t_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "t:", t_list[i], "\nResults:")
        print(search_rotated_array(nums, t_list[i]))
        print("*"*25, "\n")


# In[4]:


test(nums_list, t_list)

