
# coding: utf-8

# # Word Search
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where *"adjacent"* cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# Example:
# 
# board =
# <pre>
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# </pre>
# 
# Given word = `"ABCCED"`, return true.
# 
# Given word = `"SEE"`, return true.
# 
# Given word = `"ABCB"`, return false.

# In[1]:


def word_search(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, index): 
            """
            i - row
            j - col
            index - index of a letter in the word
            """
            if index == len(word): # if all letters are found, we stop dfs -> the word is found
                return True
            
            if not (0 <= i < len(board) and 0 <= j < len(board[i])): # check for boundaries
                return False
            
            if board[i][j] != word[index]: # if letter is not found, we stop dfs -> the word isn't found
                return False

            orig = board[i][j]    # to check that th same letter cell is not used more than once
            board[i][j] = None
            for ni, nj in (i+1, j), (i-1, j), (i, j+1), (i, j-1): # go through the neighbours ni and nj
                if dfs(ni, nj, index + 1):
                    return True
            board[i][j] = orig
            return False
        

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == word[0]:
                    if dfs(i, j, 0):     # if the word was found
                        return True
        
        return False   # if we went through the whole board but dfs didn't find the word
    


# In[2]:


# Tests:
word_list = ["ABCCED", "SEE", "ABFDEE", "ABCB", "ABFDASF"]


# In[3]:


def test(word_list):
    for i, word in enumerate(word_list):
        print("test No", i , ":\nword:", word, "\nResults:")
        board =[  ['A','B','C','E'],  ['S','F','C','S'],  ['A','D','E','E']]
        print(word_search(board, word))
        print("*"*25, "\n")


# In[4]:


test(word_list)

