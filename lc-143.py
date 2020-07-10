# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        my_stack=[]
        while(head!=None):
            my_stack.append(head)
            head=head.next
        i=0
        j=len(my_stack)-1
        node=ListNode(0)
        new_head=node
        while(i<j):
            node.next=my_stack[i]
            node=node.next
            node.next=my_stack[j]
            node=node.next
            i+=1
            j-=1
        if i==j:
            node.next=my_stack[i]
            node=node.next
        node.next=None
        return new_head.next
        
        
        