# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root,left):
            
            if not root.left and not root.right and left:
                res.append(root.val)
            
            if root.left:
                traverse(root.left,True)
            if root.right:
                traverse(root.right,False)
            
            
        res = []
        
        traverse(root,False)
        
        return sum(res)
        