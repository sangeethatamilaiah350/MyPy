# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return 
        temp=head
        temp2=head.next
        main=temp2
        while temp!=None and temp2!=None and temp.next!=None and temp2.next!=None:
            temp.next=temp2.next
            temp=temp.next
            temp2.next=temp.next
            temp2=temp2.next
        temp.next=main
        return head
            
        
        
