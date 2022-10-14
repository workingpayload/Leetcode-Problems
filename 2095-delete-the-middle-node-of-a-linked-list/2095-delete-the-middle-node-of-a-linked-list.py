# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or not head.next:
            return None
        
        
        if not head.next.next:
            head.next=None
            return head
        
        
        slow = fast = head
        
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            
            
        slow.val = slow.next.val
        slow.next = slow.next.next
        
        return head
        