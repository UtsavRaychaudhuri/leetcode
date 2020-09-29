# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_dict={v:i for i,v in enumerate(inorder)}
        seen=set()
        def bt(ino,post,i,j):
            if i>j or len(post)==0:
                return None
            num=post.pop()
            node=TreeNode(num)
            idx=inorder_dict[num]
            node.right=bt(ino,post,idx+1,j)
            node.left=bt(ino,post,i,idx-1)
            return node
        return bt(inorder,postorder,0,len(inorder)-1)
    
sol=Solution()
root = sol.buildTree(inorder = [9,3,15,20,7],
postorder = [9,15,7,20,3])
print(root)