# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        
        return self.solve(root,target,0)
    
    
    
    def solve(self,root,target,sumt):
        
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val+sumt==target
        
        
        return self.solve(root.left,target,root.val+sumt) or self.solve(root.right,target,root.val+sumt)
        