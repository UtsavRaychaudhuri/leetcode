"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack=[root]
        my_array=[]
        while(stack):
            my_array.append(stack[0].val)
            element=stack.pop(0)
            for i in element.children[::-1]:
                stack.insert(0,i)
        return my_array
            
        