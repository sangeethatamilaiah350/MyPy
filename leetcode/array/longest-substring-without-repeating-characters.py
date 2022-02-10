class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        n=len(s)
        l=0
        r=0
        maxlen=0
        while r!=n:
            if s[r] not in d:
                d[s[r]]=r
            else:
                if d[s[r]]<l:
                    d[s[r]]=r
                else:
                    l=d[s[r]]+1
                    d[s[r]]=r
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        
