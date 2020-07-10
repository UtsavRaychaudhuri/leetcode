# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        stack=[]
        mhead=head
        i=0
        while(i<n):
            stack.append(mhead)
            mhead=mhead.next
            i+=1
        i=m-1
        j=len(stack)-1
        while(i<j):
            stack[i].val,stack[j].val=stack[j].val,stack[i].val
            i+=1
            j-=1
        return head
        
            
            
            
        