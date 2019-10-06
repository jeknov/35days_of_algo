
# coding: utf-8

# # Jump Game
# 
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# **Example 1**:
# 
# Input: `[2,3,1,1,4]`
# 
# Output: true
# 
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# **Example 2**:
# 
# Input: `[3,2,1,0,4]`
# 
# Output: false
#  
#  Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

# In[1]:


# Memoisation version
def jump_game(nums):
    
    def can_jump(nums, ind):
        if memo[ind] != "Unk":
            return memo[ind] == "Good"
        
        furthestJump = min(ind + nums[ind], len(nums) - 1)
        
        for i in range(ind + 1, furthestJump + 1):
            if can_jump(nums, i):
                memo[i] = "Good"
                return True
        
        memo[ind] = "Bad"
        return False
    
    memo = ["Unk"]*len(nums) # memoisation array
    memo[-1] = "Good"   # last element can always access itself
    if nums:
        return can_jump(nums, 0)    


# **Time complexity**: O(n^2). For every element in the array, say `i`, we are looking at the next `nums[i]` elements to its right aiming to find a `Good` index. `nums[i]` can be at most `n`, where `n` is the length of array nums.
# 
# **Space complexity**: O(2n) = O(n). First `n` originates from recursion. Second `n` comes from the usage of the memo table.

# In[2]:


# DP version
def jump_game_dp(nums):
    
    memo = ["Unk"]*len(nums) # memoisation array
    memo[-1] = "Good"   # last element can always access itself
    
    for i in range(len(nums) - 1, -1, -1): # we go from right to left to eliminate recursion
        furthestJump = min(i + nums[i], len(nums) - 1)
        
        for j in range(i + 1, furthestJump + 1):
            if memo[j] == "Good":
                memo[i] = "Good"
                break
    
    return memo[0] == "Good"
    


# **Time complexity**: O(n^2). For every element `i` in the array, say `i`, the next `nums[i]` elements to its right is checked for having `Good` index. `nums[i]` can be at most `n`, where `n` is the length of array `nums`.
# 
# **Space complexity**: O(n). Size of the `memo` table.
# 

# In[3]:


# Greedy version
def jump_game_greedy(nums):
    last_pos = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    
    return last_pos == 0


# **Time complexity**: O(n). It's a single pass through the `nums` array, hence `n` steps, where `n` is the length of array `nums`.
# 
# **Space complexity**: O(1). No extra memory is used.

# In[4]:


# Tests:
nums_list = [[2,3,1,1,4], [3,2,1,0,4]] 


# In[5]:


def test(nums_list):
    for i, nums in enumerate(nums_list):
        print("test No", i , ":\nnums:", nums, "\nResults:")
        print(jump_game_greedy(nums))
        print("*"*25, "\n")


# In[6]:


test(nums_list)

