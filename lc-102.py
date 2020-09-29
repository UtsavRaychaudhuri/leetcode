# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import tree_helper
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[[root.val]]
        q=collections.deque([])
        q.append(root)
        q.append(-1)
        arr=[]
        while(q):
            node=q.popleft()
            if node==-1:
                if len(q)==0:
                    break
                res.append(arr)
                arr=[]
                q.append(-1)
                continue
            if node.left is not None:
                q.append(node.left)
                arr.append(node.left.val)
            if node.right is not None:
                arr.append(node.right.val)
                q.append(node.right)
        return res

sol=Solution()
root=tree_helper.construct_tree([1,2,3,4,5,6,7])
print(sol.levelOrder(root))