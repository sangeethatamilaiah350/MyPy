def diagonal(root):
    
    q=[]
    q.append(root)
    q.append("N")
    ans=[]
    while len(q)!=0:
        temp=q[0]
        q.pop(0)
        if temp=="N" and len(q)!=0:
            q.append("N")
            
        else:
            if temp!="N":
                ans.append(temp.data)
            
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    temp2=temp.right
                
                    while temp2:
                        ans.append(temp2.data)
                        if temp2.left:
                            q.append(temp2.left)
                        temp2=temp2.right
                
    return ans
