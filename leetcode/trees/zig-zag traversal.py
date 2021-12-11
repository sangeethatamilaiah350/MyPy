# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=[]
        queue.append(root)
        lefttoright=1
        if root==None:
            return
        while len(queue):
            n=len(queue)
            temp=[0]*n
            for i in range(n):
                
                vals=queue[0]
                index=i if lefttoright==1 else n-1-i   #nice logic to enter values in reversal order
            
                temp[index]=vals.val
                queue.remove(vals)
                
                if vals.left:
                    queue.append(vals.left)
                if vals.right:
                    queue.append(vals.right)
                    
            lefttoright=(lefttoright+1)%2    #either 1 or 0
            res.append(temp)
        return res
        
