
# coding: utf-8

# # Combination Sum III
# 
# Find all possible combinations of `k` numbers that add up to a number `n`, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# 
# Note:
# 
# - All numbers will be positive integers.
# - The solution set must not contain duplicate combinations.
# 
# **Example 1**:
# 
# Input: `k` = 3, `n` = 7
# 
# Output: `[[1,2,4]]`
# 
# **Example 2**:
# 
# Input: `k` = 3, `n` = 9
# 
# Output: `[[1,2,6], [1,3,5], [2,3,4]]`

# In[ ]:


def combination_sum3_recursive(k, n):
    
    def helper(start, candidates, target, level, comb, results):

        if target==0 and level==0:
            results.append(comb)

        for i in range(start, len(candidates)):

            if level > 0 and target >= candidates[i]:
                helper(i + 1, candidates, target - candidates[i], level - 1, comb + [candidates[i]], results)
    
    results=[]
    helper(0, [1,2,3,4,5,6,7,8,9], n, k, [], results)
    return results


# In[2]:


def combination_sum3_iter(k, n):
    # Iterative backtracking
    # -----------------------------------
    
    ans = []
    stack = [(0, 1, [])]  # (resulting sum, start, combination)
    while stack:
        res_sum, start, comb = stack.pop()
        if res_sum == n and len(comb) == k:
            ans.append(comb)
            continue

        for i in range(start, 10):
            tmp_sum = res_sum + i
            if tmp_sum > n:
                break
            stack.append((tmp_sum, i + 1, comb + [i]))
            
    return ans


# In[3]:


# Tests:
k_list = [3, 3, 2]
n_list = [7, 9, 8]


# In[4]:


def test(k_list, n_list):
    for i, k in enumerate(k_list):
        print("test No", i , ":\nk:", k, "n:", n_list[i], "\nResults:")
        print(combination_sum3_recursive(k, n_list[i]))
        print("*"*25, "\n")


# In[5]:


test(k_list, n_list)

