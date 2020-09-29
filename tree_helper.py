class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def construct_tree(arr):
    node=TreeNode(arr[0])
    root=node
    q=deque([node])
    j=1
    while(q):
        node=q.popleft()
        if j<len(arr):
            if arr[j] is not None:
                left=TreeNode(arr[j])
                q.append(left)
                node.left=left
        if j+1<len(arr):
            if arr[j+1] is not None:
                right=TreeNode(arr[j+1])
                q.append(right)
                node.right=right
        j+=2
    return root