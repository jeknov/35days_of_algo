
# coding: utf-8

# # Binary Tree Inorder Traversal
# 
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# Input: `[1,null,2,3]`
# <pre>
#    1
#     \
#      2
#     /
#    3
# </pre>
# 
# Output: `[1,3,2]`
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?

# ### 1. Recursive solution:

# In[1]:


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        
        for val in self.inorderTraversal(root.left):
            yield val
            
        yield root.val
        
        for val in self.inorderTraversal(root.right):
            yield val


# ### 2. Iterative solution:

# In[2]:


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        curr = root
        
        while curr != None or (not len(stack) == 0):
            while curr != None:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

