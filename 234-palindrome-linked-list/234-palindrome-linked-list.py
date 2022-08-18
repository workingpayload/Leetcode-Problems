# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = []
        
        while(head):
            prev.append(head.val)
            head = head.next
            
        if prev == prev[::-1]:
            return True
        return False
