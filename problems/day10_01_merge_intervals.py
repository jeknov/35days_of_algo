
# coding: utf-8

# # Merge Intervals
# 
# Given a collection of intervals, merge all overlapping intervals.
# 
# **Example 1**:
# 
# Input: `[[1,3],[2,6],[8,10],[15,18]]`
# 
# Output: `[[1,6],[8,10],[15,18]]`
# 
# Explanation: Since intervals `[1,3]` and `[2,6]` overlaps, merge them into `[1,6]`.
# 
# **Example 2**:
# 
# Input: `[[1,4],[4,5]]`
# 
# Output: `[[1,5]]`
# 
# Explanation: Intervals `[1,4]` and `[4,5]` are considered overlapping.

# In[1]:


def merge_intervals(arr):
    
    arr.sort()
    
    merged_arr = []
    
    for i in range(len(arr)):
        if not merged_arr or merged_arr[-1][1] < arr[i][0]:
            merged_arr.append(arr[i])
        else:
            merged_arr[-1][1] = max(merged_arr[-1][1], arr[i][1])         
            
    return merged_arr


# In[2]:


# Tests:
arr_list = [[[1,4],[2,3],[2,10],[15,18]], 
           [[15,18],[1,3],[2,6],[8,10]],
           [[1,4],[4,5]]]


# In[3]:


def test(arr_list):
    for i, arr in enumerate(arr_list):
        print("test No", i , ":\narr:", arr, "\nResults:")
        print(merge_intervals(arr))
        print("*"*25, "\n")


# In[4]:


test(arr_list)

