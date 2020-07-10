# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.my_dict={}
        self.max_depth=0
        self.dfs(root,0)
        return self.my_dict[self.max_depth]
    
    def dfs(self,root,depth):
        if root is None:
            return
        if root.left==None and root.right==None and depth>=self.max_depth:
            if depth in self.my_dict:
                self.my_dict[depth]+=root.val
            else:
                self.my_dict[depth]=root.val
        if depth>self.max_depth:
            self.max_depth=depth
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)
        