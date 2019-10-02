
# coding: utf-8

# # Sum of Two Integers
# 
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# 
# **Example 1**:
# 
# Input: a = 1, b = 2
# 
# Output: 3
# 
# **Example 2**:
# 
# Input: a = -2, b = 3
# 
# Output: 1

# In[1]:


def sum_two_integers(a, b):
    mask = 0xFFFFFFFF
    MAX = 0x7FFFFFFF
    while b != 0:
        carry = a & b
        a = a ^ b & mask
        b = carry << 1 & mask
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
    return a if a <= MAX else ~(a ^ mask)


# In[2]:


# Tests:
a_list = [1, -2, 124, 43, -3, -5]
b_list = [2, 3, 18,   57, 2,  -10]


# In[3]:


def test(a_list, b_list):
    for i, a in enumerate(a_list):
        print("test No", i , ":\na:", a, "b:", b_list[i], "\nResults:")
        print(sum_two_integers(a, b_list[i]))
        print("*"*25, "\n")


# In[4]:


test(a_list, b_list)

