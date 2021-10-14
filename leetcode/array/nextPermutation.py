class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            #print(nums)
            return nums
    
        else:
            n=len(nums)-1
            index=-1
            i=n
            while i>=1:
                #print("whie",index,i)
                if nums[i]>nums[i-1]:
                    #print(nums[i],nums[i-1])
                    index=i-1
                    break
                i-=1
            #print(index)
            if index==-1:
                #print(nums[::-1])
                i=0
                j=n
                while i<j and i!=j:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1
                return 
            i=n
            while i>0:
        
                if nums[i]>nums[index]:
                    nums[i],nums[index]=nums[index],nums[i]
                    break
                i-=1
            i=index+1
            j=n
            while i<j and i!=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        
            
            
