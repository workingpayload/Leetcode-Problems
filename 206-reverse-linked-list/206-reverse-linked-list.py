# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currH = head
        while currH and currH.next:
            curr = currH.next
            currH.next = currH.next.next
            curr.next = head
            head = curr
        return head
        