"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        def fr(node,tree):
            for i in tree:
                if node in i.children:
                    return fr(i,tree)
                return node
        node= fr(tree[0],tree)

sol=Solution()
sol.findRoot()