# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum=0
    
    def rangeSumBST(self, root, L, R):
        self.rangesumBST(root,L,R)
        return self.sum
    
    def rangesumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return
        if L<=root.val<=R:
            self.sum+=root.val
        self.rangesumBST(root.left,L,R)
        self.rangesumBST(root.right,L,R)
        