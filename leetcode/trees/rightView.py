

if we use a level order traversal then at the last level in least case we need to store atlmost half of the node while leads to space complexity

hence it is better to go with recursion



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        size=0
        res=[]
        level=0
        def find(node,level):
            nonlocal size
            if node==None:
                return 
            if level==size:
            
                size+=1
                res.append(node.val)
            find(node.right,level+1)
            find(node.left,level+1)
        if root==None:
            return
        else:
            find(root,level)
        return res
                
        
