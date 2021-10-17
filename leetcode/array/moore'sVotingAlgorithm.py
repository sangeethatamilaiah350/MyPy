#assuming that there is always a majority element in the array
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=0
        c=0
        for i in nums:
            if c==0:
                maj=i
            if i==maj:
                c+=1
            else:
                c-=1
        return maj
