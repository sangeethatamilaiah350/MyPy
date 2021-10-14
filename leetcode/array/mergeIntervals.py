class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        first=intervals[0]
        for i in intervals:
            if i[0]<=first[1]:
                first=(min(first[0],i[0]),max(first[1],i[1]))
            else:
                ans.append(first)
                first=i
        ans.append(first)
        
        return ans
        
