A
B A
C B A
D C B A
E D C B A

n=5
for i in range(n):
    j=65+i
    while j>=65:
        print(chr(j),end='')
        j-=1
    print()
    
    
    
A
AB
ABC
ABCD
ABCDE    
      
n=5
for i in range(n):
    k=65
    for j in range(i+1):
        print(chr(k+j),end='')
    print()
