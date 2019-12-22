# Definition for a binary tree node.

class Solution(object):
    def __init__(self):
        self.foundit=False
    
    def hasPathSum(self,root,sum):
        self.hasPathsSum(root,sum)
        return self.foundit
        
    def hasPathsSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        sum-=root.val
        if sum<0:
            return
        if root==None:
            return
        if root.left==None and root.right==None and sum==0:
            self.foundit=True
            return True
        if root.left==None and root.right==None and sum!=0:
            return
        self.hasPathsSum(root.left,sum)
        self.hasPathsSum(root.right,sum)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

TreeNode9=TreeNode(5)
TreeNode1=TreeNode(4)
TreeNode2=TreeNode(11)
TreeNode3=TreeNode(7)
TreeNode4=TreeNode(2)
TreeNode5=TreeNode(13)
TreeNode6=TreeNode(8)
TreeNode7=TreeNode(4)
TreeNode8=TreeNode(1)
TreeNode6.left=TreeNode5
TreeNode6.right=TreeNode1
TreeNode1.right=TreeNode8
TreeNode1.left=TreeNode2
TreeNode.left=TreeNode1
TreeNode9.right=TreeNode6
TreeNode9.left=TreeNode1
TreeNode2.right=TreeNode4
TreeNode7.right=TreeNode8
TreeNode7.left=TreeNode2
TreeNode2.left=TreeNode3
sol=Solution()
print(sol.hasPathSum(TreeNode9,22))

