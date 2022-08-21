# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev = None
        
        while(head):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
            
        value = 0
        count = 0
        
        
        while(prev):
            if prev.val==1:
                value += 2**count
            count+=1
            prev = prev.next
            
        return value    
            
            
        