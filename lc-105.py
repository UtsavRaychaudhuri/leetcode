# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def bt(pre,ino,i):
            if i>=len(pre):
                return
            node=TreeNode(pre[i])
            if i+1>=len(pre):
                return node
            node.left=TreeNode(pre[i+1])
            node.right=bt(pre,ino,i+2)
            return node
        return bt(preorder,inorder,0)

sol=Solution()
root = sol.buildTree(preorder = [1,2],
inorder = [1,2])
print(root)
        