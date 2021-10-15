

def absolutePermutation(n, k):
    # Write your code here
    a=[i for i in range(n+1)]
    if k==0:
        return a[1:]
    if n%2!=0:
        return [-1]

    else:
        for i in range(1,n-k+1):
            if abs(a[i]-a[i+k])==k:
                a[i],a[i+k]=a[i+k],a[i]
                
        for i in range(n-k+1,n+1):
            if abs(i-a[i])!=k:
                return [-1]
        return a[1:]

