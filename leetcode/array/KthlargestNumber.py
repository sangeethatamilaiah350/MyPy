class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        def quickselect(l,r):
            pivot=nums[r]
            p=l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            
            if k>p:
                return quickselect(p+1,r)
            elif k<p:
                return quickselect(l,p-1)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)
        
