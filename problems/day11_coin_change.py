
# coding: utf-8

# # Coin Change
# 
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# **Example 1**:
# 
# Input: coins = `[1, 2, 5]`, amount = `11`
# 
# Output: `3 `
# 
# Explanation: 11 = 5 + 5 + 1
# 
# **Example 2**:
# 
# Input: coins = `[2]`, amount = `3`
# 
# Output: `-1`
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.

# In[1]:


def coin_change(coins, amount):
    dp = [float("inf")]*(amount+1)
    dp[0] = 0
    for i in range(amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != float("inf") else -1


# In[2]:


# Tests:
coins_list = [[1, 2, 5], [2]]
amount_list = [11, 3]


# In[3]:


def test(coins_list, amount_list):
    for i, coins in enumerate(coins_list):
        print("test No", i , ":\ncoins:", coins, "amount:", amount_list[i], "\nResults:")
        print(coin_change(coins, amount_list[i]))
        print("*"*25, "\n")


# In[4]:


test(coins_list, amount_list)

