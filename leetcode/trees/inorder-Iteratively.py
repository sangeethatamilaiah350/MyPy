# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        res=[]
        a.append(root)
        while len(a):
            value=a.pop()
            if value!=None:
                a.append(value)
                a.append(value.left)
            else:
                if len(a)!=0:
                    value=a.pop()
                    res.append(value.val)
                    a.append(value.right)
        return res
        
