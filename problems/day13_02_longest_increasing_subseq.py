
# coding: utf-8

# # Longest Increasing Subsequence
# 
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# 
# **Example**:
# 
# Input: `[10,9,2,5,3,7,101,18]`
# 
# Output: `4` 
# 
# Explanation: The longest increasing subsequence is `[2,3,7,101]`, therefore the length is `4`. 
# 
# Note:
# 
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in `O(n^2)` complexity.
# 
# Follow up: Could you improve it to `O(n*logn)` time complexity?

# In[41]:


# Approaching the task using recursion and memoisation:

def count_lis(nums):
    
    def lis(nums, prev, currpos, memo):
        #print("memo:", memo)
        if currpos == len(nums):
            return 0
        
        taken = 0
        if prev < nums[currpos]:
            if (prev, currpos) in memo:
                taken = memo[(prev, currpos)]
            else:
                taken = 1 + lis(nums, nums[currpos], currpos + 1, memo)
                memo[(prev, currpos)] = taken
        

        nottaken = lis(nums, prev, currpos + 1, memo)
        memo[(prev, currpos)] = max(taken, nottaken)
        return memo[(prev, currpos)]
    
    memo = {}
    return lis(nums, float("-inf"), 0, memo)


# With memoisation, the time complexity is O(n^2)

# In[73]:


# Approaching the task using DP

def count_lis_dp(nums):
    if nums == []:
        return 0
    else:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)


# In[76]:


nums_list = [[1,3,6,7,9,4,10,5,6], [10,9,2,5,3,7,101,18], [], [0]]


# In[84]:


def test(nums_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , "\nnums:", nums, "\nResults:")
        print(count_lis_dp(nums))
        print("*"*25, "\n")


# In[85]:


test(nums_list)

