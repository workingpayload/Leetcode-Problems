# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,s):
            
            if not root.left and not root.right:
                res.append(int(s+str(root.val)))
                
            if root.left:
                helper(root.left,s+str(root.val))
                
            if root.right:
                helper(root.right,s+str(root.val))
                
        res = []
        
        helper(root,"")
        
        return sum(res)
            
            
        