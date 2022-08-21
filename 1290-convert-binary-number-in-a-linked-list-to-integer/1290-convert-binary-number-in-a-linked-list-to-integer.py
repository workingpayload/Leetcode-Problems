# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        l = []
        
        while(head):
            l.append(head.val)
            head = head.next
            
            
        count = 0
        
        num = 0
        
        for i in range(len(l)-1,-1,-1):
            num+=l[i]*(2**count)
            count+=1
            
        return num    
            
            
        