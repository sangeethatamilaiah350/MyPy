class Solution:
    def printCousins(self, root, node_to_find):
        node_to_find=node_to_find.data
        def check(val):
            if val==None:
                
                return False
            else:
                return True
        #code here
        if root.data==node_to_find:
            return [-1]
        elif root.left and root.left.data==node_to_find :
            return [-1]
        elif root.right and  root.right.data==node_to_find :
            return [-1]
        else:
            queue=[]
            queue.append(root)
            flag=0
            while len(queue):
                n=len(queue)
                for i in range(n):
                    
                    val=queue.pop(0)
                    if (check(val.left) and val.left.data==node_to_find) or (check(val.right) and val.right.data==node_to_find):
                        flag=1
                       # print("gtot")
                    else:
                        if check(val.left):
                            #print(val.left.data)
                            queue.append(val.left)
                        if check(val.right):
                            #print(val.right.data)
                            queue.append(val.right)
                if flag==1:
                    if len(queue)==0:
                        return [-1]
                        
                    else:
                        ans=[]
                        for i in queue:
                            #print(i.data)
                            ans.append(i.data)
                        return ans
                    
                    
                
                
            return [-1]


