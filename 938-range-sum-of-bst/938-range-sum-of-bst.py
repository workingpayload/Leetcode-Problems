# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.l = []
        self.inorder(root)
        
        s = 0
        
        for i in range(low,high+1):
            if i in self.l:
                s+=i
                
        return s        
            
        
        
        
        
        
        
        
        
        
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)
        