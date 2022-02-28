class Solution:
    def crossPattern (ob,S):
        # code here
        n=len(S)
        a=[]
        for i in range(n):
            k=[]
            for j in range(n):
                s=' '
                k.append(s)
            a.append(k)
        j=0
        k=0
        kk=n-1
        p=n-1
        for i in range(n):
            if i==j:
                a[i][j]=S[k]
            a[i][p]=S[kk]
            p-=1
            k+=1
            j+=1
            kk-=1
        
        res=''   
        for i in range(n):
            for j in range(n):
                res+=a[i][j]
        
        return res
        
        
        
        '''   
        for i in range(n):
            for j in range(n):
                print(a[i][j],end="")
            print()
        '''
        
               
