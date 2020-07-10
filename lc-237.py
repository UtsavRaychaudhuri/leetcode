# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev=node
        node=node.next
        while(node.next is not None):
            prev.val=node.val
            prev=prev.next
            node=node.next
        prev.val=node.val
        prev.next=None
        