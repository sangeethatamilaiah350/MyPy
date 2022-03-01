def encode(arr):
    # Code here
    res=''
    i=0
    while i<len(arr):
        element=arr[i]
        count=0
        while i!=len(arr) and element==arr[i]  :
            count+=1
            i+=1
        res+=element
        res+=str(count)
    return res
