# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPair(self,head,returnthishead,chainthishead):
        if head is None:
            return returnthishead.next
        prev=head
        head=head.next
        if head is None:
            chainthishead.next=ListNode(prev.val)
            chainthishead=chainthishead.next
            return returnthishead.next
        chainthishead.next=ListNode(head.val)
        chainthishead=chainthishead.next
        chainthishead.next=ListNode(prev.val)
        chainthishead=chainthishead.next
        return self.swapPair(head.next,returnthishead,chainthishead)

    def swapPairs(self,head):
            chainthishead=ListNode(0)
            returnthishead=chainthishead
            return self.swapPair(head,returnthishead,chainthishead)
                
            
            