def diagonalSum(root):
    #:param root: root of the given tree.
    
    #code here
    queue=[]
    result=[]
    queue.append(root)
    while len(queue):
        total=0
        for i in range(len(queue)):
            element=queue.pop(0)
            total+=element.data
            while element.right:
                total+=element.right.data
                
                if element.left:
                    queue.append(element.left)
                
                element=element.right
            if element.left:
                queue.append(element.left)
        result.append(total)
        #print(total)
    return result
        
