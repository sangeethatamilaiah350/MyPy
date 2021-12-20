# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(node):
        
            if node==None or node==p or node==q:
                return node
        
            l=find(node.left)
            r=find(node.right)
            if l==None :
                
                return r
            
            elif r==None:
                return l
            
            else:
                return node
            
        if root==None:
            return 
        else:
            return find(root)
