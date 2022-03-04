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
    
    
    
    
    
    
    
    
    
    
    
    
    
#spiral matrix    
    
    class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        down=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        direction=0
        res=[]
        
        
        while top<=down and left<=left:
            
            if direction==0:
                #print("0",top,down,left,right)
                for i in range(left,right+1):
                   
                    res.append(matrix[top][i])
                    print(matrix[top][i],'00',left,right)
                top+=1
            elif direction==1:
                print('1')
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                    print(matrix[i][right],"11")
                right-=1
            elif direction==2:
                #print('2')
                i=right
                while i>=left:
                    res.append(matrix[down][i])
                    
                    i-=1
                down-=1
            elif direction==3:
                #print('3')
                i=down
                while i>=top:
                    res.append(matrix[i][left])
                    i-=1
                left+=1
            direction=(direction +1)%4
        return res
                    
                    
                    
        
