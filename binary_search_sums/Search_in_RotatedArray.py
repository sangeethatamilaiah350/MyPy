class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            
            if nums[l]<=nums[mid]:#left is sorted
                if target>=nums[l] and target<=nums[mid]:#checking range
                    h=mid-1
                else:
                    l=mid+1
            else:#right must be sorted
                if nums[mid]<=target and target<=nums[h]:#checking range
                    l=mid+1
                else:
                    h=mid-1
        return -1
        
