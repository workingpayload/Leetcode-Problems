# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        
        def dfs(root,s):
            
            if not root.left and not root.right:
                s = s + str(root.val)
                res.append(s)
                
            s = s+ str(root.val)+"->"    
            
            if root.left:
                left = dfs(root.left,s)
            
            if root.right:
                right = dfs(root.right,s)
            
            
        dfs(root,"")
        
        return res