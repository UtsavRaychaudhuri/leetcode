# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        self.dfs(root)
        return self.count
        
        
    def dfs(self,root):
        if root is None:
            return
        self.count+=1
        self.dfs(root.left)
        self.dfs(root.right)
        