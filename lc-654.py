# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recurse(nums,low,high):
            if low>=high:
                return None
            max_num=max(nums[low:high])
            node=TreeNode(max_num)
            node.left=recurse(nums,low,nums.index(max_num)-1)
            node.right=recurse(nums,nums.index(max_num)+1,high)
            return node
        return recurse(nums,0,len(nums))

sol=Solution()
sol.constructMaximumBinaryTree([3,2,1,6,0,5])