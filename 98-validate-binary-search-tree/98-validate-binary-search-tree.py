# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.newroot = []
        
        self.inorder(root)
        
        for i in range(1,len(self.newroot)):
            if self.newroot[i]<=self.newroot[i-1]:
                return False
        return True
    
    
    
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            self.newroot.append(node.val)
            self.inorder(node.right)