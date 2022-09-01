# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetsum: int) -> bool:
        
        if not root:
            return False
        
        def dfs(root,curr):
            
            if not root:
                return False
            
            if not root.left and not root.right:
                return curr+root.val==targetsum
            
            return dfs(root.left,curr+root.val) or dfs(root.right,curr+root.val)
        
        
        return dfs(root,0)
        