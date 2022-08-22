# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return -1
            
            return max(height(root.left),height(root.right))+1
        
        
        if not root:
            return True
        
        dif = height(root.left) - height(root.right)
        
        if abs(dif)>1:
            return False
        
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        