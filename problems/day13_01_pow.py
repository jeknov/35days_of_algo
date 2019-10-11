
# coding: utf-8

# # Pow(x, n)
# 
# Implement pow(x, n), which calculates x raised to the power n (x**n).
# 
# **Example 1**:
# 
# Input: 2.00, 10
# 
# Output: 1024.00
# 
# **Example 2**:
# 
# Input: 2.10, 3
# 
# Output: 9.261
# 
# **Example 3**:
# 
# Input: 2.00, -2
# 
# Output: 0.25
# 
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# 
# Note:
# 
# -100.0 < x < 100.0
# 
# n is a 32-bit signed integer, within the range `[−231, 231 − 1]`

# In[ ]:


def pow(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        x = 1 / x
        n = -n
    
    temp = pow(x, n//2)
    
    if n%2 == 0:
        return pow(x, n//2) * pow(x, n//2)
    if n%2 == 1:
        return pow(x, n//2) * pow(x, n//2) * x


# In[2]:


x_list = [2, 2.1, 2]
n_list = [10, 3, -2]


# In[3]:


def test(x_list, n_list):
    for i, x in enumerate(x_list):
        print("test No", i , ":\nx:", x, "n:", n_list[i], "\nResults:")
        print(pow(x, n_list[i]))
        print("*"*25, "\n")


# In[4]:


test(x_list, n_list)

