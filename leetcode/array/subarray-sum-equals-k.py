class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        count=0
        tot=0
        for i in nums:
            tot+=i
            if tot==k:
                count+=1
            if tot-k in d:
                count+=d[tot-k]
            if tot in d:
                d[tot]+=1
            else:
                d[tot]=1
        return count
        
