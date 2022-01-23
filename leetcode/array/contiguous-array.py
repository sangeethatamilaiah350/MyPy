class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen=0
        d={}
        n=len(nums)
        tot=0
        d[0]=-1
        for i in range(n):
            if nums[i]==1:
                tot+=1
            else:
                tot-=1
            
            if tot==0:
                maxlen=max(maxlen,i+1)
            elif tot in d:
                maxlen=max(maxlen,i-d[tot])
            else:
                d[tot]=i
        #print(d)
        return maxlen
            
        
