
# coding: utf-8

# # Simulate 5-sided die 
# 
# You have a function `rand7()` that generates a random integer from 1 to 7. Use it to write a function `rand5()` that generates a random integer from 1 to 5.

# In[1]:


import random

def rand7():
    return random.randrange(1,7,1)


# In[2]:


rand7()


# In[3]:


def rand5():
    result = 7 # or any arbitrarily large
    while result > 5:
        result = rand7()
    return result


# In[4]:


# Test:
for i in range(10):
    print(rand5())


# **Time complexity**:
# In the worst-case scenario, time complexity is O($\infty$)
# 
# **Space complexity**:
# O(1)
