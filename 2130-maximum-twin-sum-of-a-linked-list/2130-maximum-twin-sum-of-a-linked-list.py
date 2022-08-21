# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        l = []
        while(head):
            l.append(head.val)
            head = head.next
            
        i = 0
        r = len(l)-1
        
        max_sum = 0
        
        while(i<r):
            if l[i]+l[r]>max_sum:
                max_sum = l[i]+l[r]
            i+=1
            r-=1
            
        return max_sum    
                