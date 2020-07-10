# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.node=ListNode()
        self.returnnode=self.node
    def reverseList(self, head: ListNode) -> ListNode:
        self.reverselist(head)
        return self.returnnode.next
        
    def reverselist(self,head):
        if head is None:
            return
        self.reverseList(head.next)
        self.node.next=ListNode(head.val)
        self.node=self.node.next
        