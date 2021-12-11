# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=float('-inf')
        
        def sums(node):
            nonlocal res 
            if node==None:
                return 0
            l=max(0,sums(node.left))
            r=max(0,sums(node.right))
            res=max(res,l+r+node.val)
            return node.val+max(l,r)
        sums(root)
        
        return res
            
