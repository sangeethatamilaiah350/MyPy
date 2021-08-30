class Solution:
    def romanToInt(self, s: str) -> int:
        def check(c):
            if c=='I':
                return 1
            if c=='V':
                return 5
            if c=='X':
                return 10
            if c=='L':
                return 50
            if c=='C':
                return 100
            if c=='D':
                return 500
            if c=='M':
                return 1000
            
        i=0
        n=len(s)
        res=0
        while i<n:
            if i+1<n:
                if check(s[i])>=check(s[i+1]):
                    res+=check(s[i])
                    i=i+1
                else:
                    res=res+(check(s[i+1])-check(s[i]))
                    i=i+2
            else:
                res +=check(s[i])
                i=i+1
        return res
                
