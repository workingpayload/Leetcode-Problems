# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        def dfs(root,currmax):
            if not root:
                return 
            
            
            if root.val>=currmax:
                count[0]+=1
                currmax = root.val
                
            dfs(root.left,currmax)
            dfs(root.right,currmax)
            
            
        count=[0]
        dfs(root,root.val)
        return count[0]
        