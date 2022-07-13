# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def order(l):
            
            if len(l)==0:
                return 
            
            m,n = [],[]
            
            for i in l:    
                n.append(i.val)
                
                if i.left:
                    m.append(i.left)
                    
                if i.right:
                    m.append(i.right)
                    
            res.append(n)
            
            order(m)
            return
        
        res = []
        if root:
            order([root])
        return res
            