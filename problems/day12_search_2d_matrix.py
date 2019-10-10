
# coding: utf-8

# # Search a 2D Matrix II
# 
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# **Example**:
# 
# Consider the following matrix:
# <pre>
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# </pre>
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.

# In[1]:


def search_2d_matrix(matrix, target):
    
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return false
    
    row = 0
    col = len(matrix[0]) - 1
    
    while row <  len(matrix[0]) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
            
    return False   


# In[2]:


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


# In[3]:


target_list = [15, 2, 9, 17, 21, 6, 35, 43]


# In[4]:


def test(matrix, target_list):
    for i, target in enumerate(target_list):
        print(matrix)
        print("test No", i , ":\ntarget:", target, "\nResults:")
        print(search_2d_matrix(matrix, target))
        print("*"*25, "\n")


# In[5]:


test(matrix, target_list)

