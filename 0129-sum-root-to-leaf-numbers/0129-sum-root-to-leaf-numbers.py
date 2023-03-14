# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        res = []
        def dfs(root,s):
            if not root.left and not root.right:
                s+=str(root.val)
                res.append(int(s))
                return
            if root.left:
                dfs(root.left,s+str(root.val))
            if root.right:    
                dfs(root.right,s+str(root.val))

        dfs(root,"")
        return sum(res)     



        