try:
    n=int(input())
    for i in range(n):
        x=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        #print(a,b)
        c=0
        if a[0]>=b[0]:
            c+=1
        for i in range(1,x):
            if a[i]-a[i-1]>=b[i]:
                c+=1
        
        print(c)        
                
except:
    pass
        
