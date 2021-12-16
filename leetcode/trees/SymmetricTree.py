# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def find(Ltree,Rtree):
            
            if Ltree==None or Rtree==None:
                return Ltree==Rtree
            if Ltree.val!=Rtree.val:
                return False
            return find(Ltree.left,Rtree.right) and find (Ltree.right,Rtree.left)
        
        
        if root==None:
            return False
        return find(root.left,root.right)
    
            
        
