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
