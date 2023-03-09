# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        count = 0
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            count +=1
            
            if slow == fast:
                
                slow = head
                
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return fast
            
        return None   
            
            
        