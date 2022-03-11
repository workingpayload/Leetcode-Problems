# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        zero = ListNode(next=head) # dummy node
        
        count, tail = 0, zero
        while tail.next:
            count, tail = count + 1, tail.next
            
        k = k % count
        if not k: return head

        newTail = zero
        for _ in range(0, count - k):
            newTail = newTail.next

        zero.next, tail.next, newTail.next = newTail.next, head, None
            
        return zero.next
        