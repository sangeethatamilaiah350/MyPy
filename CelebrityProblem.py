#without using extra space


class Solution:
    
   
    def celebrity(self, M, n):
      
        top=n-1
        i=n-2
        while i>=0:
            if M[top][i]==1:  #based on stack idea
                top=i
            i-=1
        #print(top)
        for i in range(n):
            if M[top][i]==1:
                #print(M[top][i],top,i,"row check")
                return -1
        for i in range(n):
            if i!=top and  M[i][top]==0:
                #print(M[i][top],top,i,"column check")
                return -1
        return top

