class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        while head:
            if head.next:
                head.val, head.next.val = head.next.val, head.val
                head = head.next.next
            else:
                break
        
        return h