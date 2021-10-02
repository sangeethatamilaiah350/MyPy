# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=[]
        temp=head
        c=0
        while temp!=None:
            a.append(temp)
            c+=1
            temp=temp.next
        print(c)
        if n==c:
            head=head.next
        else:
            add=a[-(n+1)]
            if n==1 and c==1:
                head=None
            elif n==1:
                add.next=None
            else:
                add.next=add.next.next
        return head
        
        
        
        
