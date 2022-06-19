# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.l = []
        self.inorder(root)
        s = []
        
        for i in range(1,len(self.l)):
            s.append(self.l[i]-self.l[i-1])
            
        return min(s)    
            
        
        
        
        
        
        
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)
            
        