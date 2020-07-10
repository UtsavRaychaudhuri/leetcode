# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    m=0
    a=0
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return
        else:
            self.a+=1
            self.removeNthFromEnd(head.next,n)
            self.m+=1
            if self.m==n+1:
                head.next=head.next.next
        if self.a==self.m:
            if self.a==n:
                head=head.next
                return head
            return head
            
        