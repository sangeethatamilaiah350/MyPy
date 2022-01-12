
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            head.val=''
        slow=head
        fast=head
        while slow.next!=None and fast.next!=None and fast.next.next!=None:
            
            slow=slow.next
            fast=fast.next.next
        while slow.next!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next
        if slow.next==None:
            head.next=None
            return head
        else:
            slow.val=slow.next.val
            slow.next=slow.next.next
            return head
            
        
