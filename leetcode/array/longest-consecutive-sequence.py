class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table=set()
        for i in nums:
            table.add(i)
        print(table)
        
        maxlen=0
        for i in nums:
            if i-1 not in table:
                count=0
                j=i
                while i in table:
                    i=i+1
                    count+=1
                maxlen=max(maxlen,count)
        return maxlen
