# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self,root):
        self.value=0
        self.helpwithbsttogst(root)
        return root
        
    def helpwithbsttogst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        self.helpwithbsttogst(root.right)
        self.value+=root.val
        root.val=self.value
        self.helpwithbsttogst(root.left)
        
        