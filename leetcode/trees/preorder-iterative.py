# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        res=[]
        if root==None:
            return res
        a.append(root)
        while len(a):
            value=a.pop()
            res.append(value.val)
            if value.right:
                a.append(value.right)
            if value.left:
                a.append(value.left)
        return res
        
