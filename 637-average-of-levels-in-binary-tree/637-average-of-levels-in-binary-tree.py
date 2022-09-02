class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        result = []
        queue = deque([root])
        
        while queue:
            result.append(sum([x.val for x in queue])/len(queue))
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
        return result