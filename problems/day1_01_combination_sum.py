
# coding: utf-8

# # Combination Sum
# 
# Given a set of candidate numbers (`candidates`) (without duplicates) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.
# 
# The same repeated number may be chosen from candidates unlimited number of times.
# 
# Note:
# 
# - All numbers (including `target`) will be positive integers.
# - The solution set must not contain duplicate combinations.
# 
# **Example 1**:
# 
# Input: candidates = `[2,3,6,7]`, target = `7`,
# 
# A solution set is:
# `
# [
#   [7],
#   [2,2,3]
# ]`
# 
# **Example 2**:
# 
# Input: candidates = `[2,3,5]`, target = `8`,
# 
# A solution set is:
# `
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]`

# In[1]:


def comb_sum(candidates, target):
    recursive_sum(candidates, target, 0, [])
    
def recursive_sum(candidates, target, index, sublist):
    if target == 0:
        print(sublist)
        return 
    if target < 0:
        return
    for i in range(index, len(candidates)):
        sublist.append(candidates[i])
        recursive_sum(candidates, target - candidates[i], i, sublist)
        sublist.pop()  


# In[2]:


candidates_list = [[2,3,6,7], [2,3,5]]
targets = [7, 8]


# In[3]:


def test(candidates_list, targets):
    for i, candidates in enumerate(candidates_list):
        print("test No", i , ":\ncandidates:", candidates, "target:", targets[i], "\nResults:")
        comb_sum(candidates, targets[i])
        print("*"*25, "\n")


# In[4]:


res = test(candidates_list, targets)

