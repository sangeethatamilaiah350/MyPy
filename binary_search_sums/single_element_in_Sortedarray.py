class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-2
        while (l<=h):
            mid=(l+h)//2
            if nums[mid]==nums[mid^1]:
                l=mid+1
            else:
                h=mid-1
        #print(nums[l])
        return nums[l]
        
