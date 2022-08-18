# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        count=0
        temp = head
        
        while(head):
            new = ListNode(head.val)
            new.next = prev
            prev = new
            head = head.next    
            count+=1
            
        while(count > count//2):
            if prev.val!=temp.val:
                return False
            prev = prev.next
            temp = temp.next
            count-=1
            
        return True    
            
            