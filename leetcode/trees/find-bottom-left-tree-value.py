class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=[]
        leftmost=0
        queue.append(root)
        while len(queue):
            n=len(queue)
            for i in range(n):
                vaal=queue.pop(0)
                if i==0:
                    leftmost=vaal.val
                if vaal.left:
                    queue.append(vaal.left)
                if vaal.right:
                    queue.append(vaal.right)
        return leftmost
        
