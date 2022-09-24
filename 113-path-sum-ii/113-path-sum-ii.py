# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        def dfs(root,path):
            
            if not root.left and not root.right:
                
                if targetSum==sum(path)+root.val:
                    res.append(path+[root.val])
                    return
            
            if root.left:
                dfs(root.left,path+[root.val])
                
            if root.right:
                dfs(root.right,path+[root.val])
                
        res = []
        dfs(root,[])
        return res
        