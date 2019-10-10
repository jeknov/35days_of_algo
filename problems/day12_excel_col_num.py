
# coding: utf-8

# # Excel Sheet Column Number
# 
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# 
# For example:
# <pre>
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# </pre>
# 
# **Example 1**:
# 
# Input: "A"
# 
# Output: 1
# 
# **Example 2**:
# 
# Input: "AB"
# 
# Output: 28
# 
# **Example 3**:
# 
# Input: "ZY"
# 
# Output: 701

# In[1]:


def excel_col_num(s):
    if not s or s == "":
        return -1
    
    sum = 0
    
    for letter in s:
        sum *= 26
        sum += ord(letter) - ord("A") + 1
    
    return sum


# In[2]:


s_list = ["A", "AB", "ZY"]


# In[3]:


def test(s_list):
    for i, s in enumerate(s_list):
        print("test No", i , ":\ns:", s, "\nResults:")
        print(excel_col_num(s))
        print("*"*25, "\n")


# In[4]:


test(s_list)

