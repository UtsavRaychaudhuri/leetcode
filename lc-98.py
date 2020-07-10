# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.my_array=[]
    
    def isValidBST(self,root):
        self.isCheckValidBST(root)
        return self.my_array==sorted(self.my_array) and len(self.my_array)==len(set(self.my_array))
    
    def isCheckValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return
        self.isCheckValidBST(root.left)
        self.my_array.append(root.val)
        self.isCheckValidBST(root.right)
        
        