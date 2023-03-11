class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = self.getValues(head)
        return self.buildBST(values, 0, len(values)-1)
    
    def getValues(self, head):
        values = deque()
        while head:
            values.append(head.val)
            head = head.next
        return values
    
    def buildBST(self, values, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(values[mid])
        node.left = self.buildBST(values, start, mid-1)
        node.right = self.buildBST(values, mid+1, end)
        return node
