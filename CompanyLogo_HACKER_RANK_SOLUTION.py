s="aabbbccde"
h=list(s)
s=list(set(s))
a=sorted(s,reverse=False)
#print(a)
b=[]
for i in a:
    b.append(i)
    b.append(h.count(i))
print(b)
    
x=[]

for j in range(1,len(b),2):
    for k in range(j+2,len(b),2):
        if b[j]<b[k]:
            b[j],b[k]=b[k],b[j]
            b[j-1],b[k-1]=b[k-1],b[j-1]
        if b[j]==b[k]:
            if b[j-1]>b[k-1]:
                b[j-1],b[k-1]=b[k-1],b[j-1]
    
print(b)
for i in range(0,6,2):
    print(b[i],b[i+1])
