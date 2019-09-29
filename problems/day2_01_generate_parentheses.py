
# coding: utf-8

# # Generate Parentheses
# 
# Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given `n` = 3, a solution set is:
# 
# `
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]`

# In[1]:


def generate_parentheses(n):
    '''
    n - int, number of pairs of parentheses
    '''
    
    def helper(seq, l, s):
        '''
        seq - str, generated sequence of parentheses
        l - int, number of unused left parentheses "("
        s - int, balance that increases by 1 when "(" is added to the sequence and decreases by 1 when ")" is added.
        '''
        if l == 0:
            return [seq + ")" * s]
        elif s == 0:
            return helper(seq + "(", l - 1, s + 1)
        return helper(seq + "(", l - 1, s + 1) + helper(seq + ")", l, s - 1)
        
    return helper("", n, 0)


# In[2]:


# Tests:
n_list = [2,3,4,5]


# In[3]:


def test(n_list):
    for i, n in enumerate(n_list):
        print("test No", i , ":\nnumber of parentheses:", n, "\nResults:")
        print(generate_parentheses(n))
        print("*"*25, "\n")


# In[4]:


test(n_list)

