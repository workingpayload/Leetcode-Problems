# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        idx = 0
        res = []
        max_sum = 0
        slow = fast = head
        while fast and fast.next:
            res.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        idx = 1
        while slow:
            res[-idx] += slow.val
            max_sum = max(max_sum, res[-idx])
            slow = slow.next
            idx += 1
        return max_sum