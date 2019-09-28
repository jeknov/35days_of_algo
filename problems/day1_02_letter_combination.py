
# coding: utf-8

# # Letter Combinations of a Phone Number
# 
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
# <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png">
# 
# **Example**:
# 
# Input: `"23"`
# 
# Output: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`
# 
# **Note**:
# 
# Although the above answer is in lexicographical order, your answer could be in any order you want.

# In[1]:


def letter_combination(digits):
    digit_map = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

    def generate_combinations(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in digit_map[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                generate_combinations(combination + letter, next_digits[1:])
            
    output = []
    if digits:
        generate_combinations("", digits)
        
    return output


# In[2]:


# Tests:
digits_list = ["23", "32", "427"]


# In[3]:


def test(digits_list):
    for i, digits in enumerate(digits_list):
        print("test No", i , ":\ndigits:", digits, "\nResults:")
        print(letter_combination(digits))
        print("*"*25, "\n")


# In[4]:


test(digits_list)


# 
# 
# **Time complexity** : `O(3^N x 4^M)` where `N` is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and `M` is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and `N+M` is the total number digits in the input.
