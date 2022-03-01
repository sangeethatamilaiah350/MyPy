class Solution:
    def romanToDecimal(self, S): 
        # code here
        d={'I': 1,'V': 5,'X': 10,'L': 50,'C':100,'D': 500,'M' :1000}
        n=len(S)
        res=d[S[n-1]]
        i=n-1
        while i>0:
            if d[S[i-1]]<d[S[i]]:
                res-=d[S[i-1]]
            else:
                res+=d[S[i-1]]
                
                
            i-=1
        return res
        
