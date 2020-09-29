# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import tree_helper
from ast import literal_eval
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data=[]
        def dfs(root):
            if root is None:
                return
            data.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return str(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr=literal_eval(data)
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
        root=construct_tree(arr)
        return root

        

# Your Codec object will be instantiated and called as such:
codec = Codec()
root=tree_helper.construct_tree([1,None,2])
str=codec.serialize(root)
codec.deserialize(str)