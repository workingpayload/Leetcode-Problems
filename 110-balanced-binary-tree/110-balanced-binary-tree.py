# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return -1
            
            heightleft = height(root.left)
            if heightleft == float('-inf'):
                return float('-inf')
            
            heightright= height(root.right)
            if heightright == float('inf'):
                return float('-inf')
            
            diff = heightleft - heightright
            
            if abs(diff)>1:
                return float('-inf')
            else:
                return max(heightleft,heightright)+1
        
        return height(root)!=float('-inf')