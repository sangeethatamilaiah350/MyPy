#assuming that there is always a majority element in the array  {leetcode}
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

#assuming that may or may not be  a majority element in the array  {geek for geek}    
    class Solution:
    def majorityElement(self, A, N):
        #Your code here
        c=0
        maj=-1
        for i in A:
            if c==0:
                maj=i
            if i==maj:
                c+=1
            else:
                c-=1
        c=0
        for i in A:
            if i==maj:
                c+=1
        if c>(N//2):#important important
            return maj
        else:
            return -1
        
