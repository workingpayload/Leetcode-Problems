# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def helper(root,left):
            
            if not root.left and not root.right and left:
                self.res+=root.val
                
            if root.left:
                helper(root.left,True)
                
            if root.right:
                helper(root.right,False)
                
        helper(root,False)        
        return self.res
        
        
        