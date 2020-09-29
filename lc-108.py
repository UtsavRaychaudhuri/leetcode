# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def arrtobst(nums,i,j):
            if i==j:
                return 
            mid=(j+i)//2
            node=TreeNode(nums[mid])
            node.left=arrtobst(nums,i,mid)
            node.right=arrtobst(nums,mid+1,j)
            return node
        return arrtobst(nums,0,len(nums))

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)


sol=Solution()
root = sol.sortedArrayToBST([-10,-3,0,5,9])
sol.inorder(root)
print(root)