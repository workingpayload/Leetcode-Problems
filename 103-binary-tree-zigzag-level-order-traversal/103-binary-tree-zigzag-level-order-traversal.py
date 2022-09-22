# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()
        
        res = []
        
        q.append(root)
        
        while(q):
            
            qlen = len(q)
            level = []
            
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
                
        for i in range(1,len(res),2):
            res[i] = res[i][::-1]            
            
            
        return res        
            
                
                
        