# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(arr):
    node=TreeNode(arr[0])
    root=node
    q=[node]
    j=1
    while(q):
        node=q.pop()
        if j<len(arr):
            left=TreeNode(arr[j])
            q.append(left)
            node.left=left
        if j+1<len(arr):
            right=TreeNode(arr[j+1])
            q.append(right)
            node.right=right
        j+=2
    return root



class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.left_arr=[]
        self.right_arr=[]
        def dfsleft(root):
            if root is None:
                return
            dfsleft(root.left)
            self.left_arr.append(root.val)
            dfsleft(root.right)
        def dfsright(root):
            if root is None:
                return
            dfsright(root.right)
            self.right_arr.append(root.val)
            dfsright(root.left)
        dfsleft(root)
        dfsright(root)
        if len(self.left_arr)==len(self.right_arr):
            for i in range(len(self.left_arr)):
                if self.left_arr[i]!=self.right_arr[i]:
                    return False
            return True
        return False



sol=Solution()
root=construct_tree([1,2,2,2,None,2])
print(sol.isSymmetric(root))

