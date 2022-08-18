# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        fast = slow = head

        while(fast and fast.next):
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while(slow):
            top = stack[-1]
            stack.pop(-1)
            if top!=slow.val:
                return False
            slow = slow.next

        return True