# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = [] # store all root TreeNodes
        dic = {} # memo: map serialized data to root TreeNode
        
        self.find(root, dic, res)
        return res
    
    
    def find(self, root, dic, res):
        if not root:
            return
        
        # find left and right duplicate subtrees
        self.find(root.left, dic, res)
        self.find(root.right, dic, res)
        # serialize a new subtree for every TreeNode
        data = []
        self.serialize(root, data)
        data = ''.join(data)
        # only add one TreeNode for each duplication
        if dic.get(data, 0) == 1:
            res.append(root)
        # update memo dictionary
        dic[data] = dic.get(data, 0) + 1
            

    def serialize(self, root, data):
        if not root:
            data.append('#,')
            return
        # preorder serialization
        data.append(str(root.val))
        data.append(',')
        self.serialize(root.left, data)
        self.serialize(root.right, data)
        