# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.curr = 0
        
        def traverse(root):
            
            if not root:
                return
            
            traverse(root.right)
            temp= root.val
            self.curr+=root.val
            root.val=self.curr
            traverse(root.left)
        
        traverse(root)
        return root
            
        
       
        