# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        self.reverseList(head.next)
        head.next=head.val
        head=head.next

ListNode1=ListNode(1)
ListNode1.next=ListNode(2)
ListNode1.next.next=ListNode(3)
ListNode1.next.next.next=ListNode(4)
ListNode1.next.next.next.next=ListNode(5)
sol=Solution()
sol.reverseList(ListNode1)
        