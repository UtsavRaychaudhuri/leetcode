class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.retu=[]
        self.ret=None
        def ins(node):
            if node is None:
                return
            ins(node.left)
            self.retu.append(node.val)
            if len(self.retu)>=2:
                if self.retu[-2]<self.retu[-1] and self.retu[-2]==p:
                    self.ret=node
            ins(node.right)
        ins(root)
        return self.ret
        

sol=Solution()
from tree_helper import construct_tree
root=construct_tree([2,None,3])
root=sol.inorderSuccessor(root,2)
print(root.val)
