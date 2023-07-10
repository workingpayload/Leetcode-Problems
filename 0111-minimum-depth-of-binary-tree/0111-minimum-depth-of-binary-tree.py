# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,depth):
            if not root:
                return depth
            else:
                if(root.left==None):
                    return dfs(root.right,depth+1)
                elif(root.right==None):
                    return dfs(root.left,depth+1)
                return min(dfs(root.left,depth+1),dfs(root.right,depth+1))
            
        return dfs(root,0)   
        