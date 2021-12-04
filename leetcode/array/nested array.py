class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        maxx=1
        
        for i in range(n):
            d[i]=0
            
            
        def check(start):
            nonlocal maxx
            i=nums[start]
            d[start]=1
            count=1
            while nums[i]!=nums[start]:
                d[i]=1
                count+=1
                i=nums[i]
            if count>maxx:
                maxx=count
                
                
                
        for i in range(n):
            if d[i]!=1:
                check(i)
        return maxx
        
