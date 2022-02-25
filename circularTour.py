
kind of kadanes algorithm


class Solution:
    
   
    def tour(self,lis, n):
       
        shortage=0
        fuel=0
        start=0
        #print(lis)
        for i in range(n):
            fuel+=lis[i][0] - lis[i][1]
            if fuel<0:
                start=i+1
                shortage+=fuel
                fuel=0
                
        if fuel+shortage>=0:
            return start
        else:
            return -1
