
# coding: utf-8

# # Unique Paths
# 
# A robot is located at the top-left corner of a `m` x `n` grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# ![title](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: `m` and `n` will be at most 100.
# 
# **Example 1**:
# 
# Input: `m` = `3`, `n` = `2`
# 
# Output: `3`
# 
# ***Explanation***:
# 
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# **Example 2**:
# 
# Input: `m` = `7`, `n` = `3`
# 
# Output: `28`

# In[1]:


def unique_paths(m, n):
    
    path_matrix = [[1] * m] * n
    
    for i in range(1, n):
        for j in range(1, m):
            path_matrix[i][j] = path_matrix[i - 1][j] + path_matrix[i][j - 1]
    return path_matrix[n - 1][m - 1]
        


# In[2]:


# Tests:

m_list = [3, 7]
n_list = [2, 3]


# In[3]:


def test(m_list, n_list):
    for i, m in enumerate(m_list):
        print("test No", i , ":\nm:", m, "n:", n_list[i], "\nResults:")
        print(unique_paths(m, n_list[i]))
        print("*"*25, "\n")


# In[4]:


test(m_list, n_list)

