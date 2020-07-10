
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode temp = head;
        int prevcarry=0;
        int x=0;
        int y=0;
        while(l1!=null || l2!=null){
            x=(l1!=null)? l1.val:0;
            y=(l2!=null)? l2.val:0;
            int data= x+y + prevcarry;
            prevcarry= data/10;
            data=data%10;
            ListNode ln= new ListNode(data);
            temp.next=ln;
            temp=temp.next;
            if (l1!=null){
                l1=l1.next;
            }
            if (l2!=null){
                l2=l2.next;
            }
        }
        if (prevcarry>0){
            temp.next=new ListNode(prevcarry);
        }
        return head.next;
        
    }
}
