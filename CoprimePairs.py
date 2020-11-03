"""
coprime numbers are nothing but numbers whose gcd is 1
"""

def coprime(a,b):
    while a!=0:
        gcd=a
        a=b%a
        b=gcd

    if gcd==1:
        return 1
    else:
        return 0
def coprimepairs(array):
    flag=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(coprime(array[i],array[j])):
                flag=1
                print(array[i],array[j])
    if flag==0:
        print("NO SUCH PAIR")
A=[6,2,4]
coprimepairs(A)
