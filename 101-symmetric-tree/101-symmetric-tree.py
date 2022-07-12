# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(l,r):
            if l and r:
                if l.val==r.val:
                    return check(l.left,r.right) and check(l.right,r.left)
                else:
                    return False
                
            else:
                if l:
                    return False
                elif r:
                    return False
                else:
                    return True
                
                
        return check(root.left,root.right)       
                