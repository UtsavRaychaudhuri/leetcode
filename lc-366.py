# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import tree_helper

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d=collections.defaultdict(list)
        def dfs(root):
            if root is None:
                return -1
            j=max(dfs(root.left),dfs(root.right))+1
            d[j].append(root.val)
            return j
        dfs(root)
        res=[]
        for i,j in d.items():
            res.append(j)
        return res

sol=Solution()
root=tree_helper.construct_tree([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8])
sol.findLeaves(root)
