# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorderl = []
        
        
        def postorder(root):
            
            if root:
                
                postorder(root.left)
                postorder(root.right)
                postorderl.append(root.val)
                
                
                
                
        postorder(root)        
        return postorderl                
        
        