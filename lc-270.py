# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closestval=abs(target-root.val)
        self.closestnode=root.val
        self.closest_val(root,target)
        return self.closestnode
           
    def closest_val(self,root,target):
        if root is None:
            return
        if abs(target-root.val)<self.closestval:
            self.closestnode=root.val
            self.closestval=abs(target-root.val)
        if root.val>target:
            self.closest_val(root.left,target)
        else:
            self.closest_val(root.right,target)
        
        
        