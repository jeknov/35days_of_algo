
# coding: utf-8

# # Happy Number
# 
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# 
# **Example**: 
# 
# Input: 19
# 
# Output: true
# 
# Explanation:
# <pre>
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# </pre>

# In[1]:


def is_happy(n):
    memo = set()
    while n not in memo:
        memo.add(n)
        n = sum(int(i)**2 for i in str(n))
    print(memo, "\n")
    return 1 in memo


# In[2]:


n_list = [7, 13, 19, 23, 31, 79, 97, 6, 0, 8, 124]


# In[3]:


def test(n_list):
    for i, n in enumerate(n_list):
        print("test No", i , ":\nn:", n, "\nResults:")
        print(is_happy(n))
        print("*"*25, "\n")

