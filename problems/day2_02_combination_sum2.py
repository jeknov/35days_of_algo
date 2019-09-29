
# coding: utf-8

# # Combination Sum II
# 
# Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in candidates where the candidate numbers sums to target.
# 
# Each number in candidates may only be used **once** in the combination.
# 
# Note:
# 
# All numbers (including `target`) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# **Example 1**:
# 
# Input: candidates = `[10,1,2,7,6,1,5]`, target = 8,
# 
# A solution set is:
# `[
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]`
# 
# **Example 2**:
# 
# Input: candidates = `[2,5,2,1,2]`, target = 5,
# 
# A solution set is:
# `[
#   [1,2,2],
#   [5]
# ]`

# In[28]:


def comb_sum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    candidates.sort()

    helper(res, candidates, target, [])

    return res

def helper(res, candidates, target, sublist):
    if target == 0 and sorted(sublist) not in res:
        res.append(sorted(sublist))
        return

    if candidates and target > 0:
        for index, val in enumerate(candidates):
            if target >= val:
                helper(res, candidates[index+1:], target-val, sublist+[val])
            else:
                break


# In[25]:


# Tests:
candidates_list = [[2,5,2,1,2], [10,1,2,7,6,1,5], [1,2,3]]
targets = [5, 8, 4]


# In[29]:


def test(candidates_list, targets):
    for i, candidates in enumerate(candidates_list):
        print("test No", i , ":\ncandidates:", candidates, "target:", targets[i], "\nResults:")
        print(comb_sum2(candidates, targets[i]))
        print("*"*25, "\n")


# In[30]:


test(candidates_list, targets)

