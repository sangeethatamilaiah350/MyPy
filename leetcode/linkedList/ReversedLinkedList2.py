# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head.next==None:
        
            return head
        
        start=head
        count=1
        
        
        while left!=1 and start.next and count!=left:
            temp=start
            start=start.next
            count+=1
            
            
        temp1=start
        pre=None
        while start.next and count!=right:
            nexts=start.next
            start.next=pre
            pre=start
            start=nexts
            count+=1
        temp2=start.next
        start.next=pre
        
        if left!=1:
            temp.next=start
        
        temp1.next=temp2
        
        if left==1:
            return start
        
        return head
        
            
            
        
