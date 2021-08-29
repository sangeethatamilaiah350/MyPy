class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        stack=[]
        n=len(nums)
        i=2*n-1
        top=-1
        while i>=0:
            while top!=-1 and stack[top]<=nums[i%n]:
                stack.pop()
                top-=1
            
            if i<n:
                if top==-1:
                    res.append(-1)
                else:
                    res.append(stack[top])
            stack.append(nums[i%n]) 
            top=top+1
            i=i-1
        return res[::-1]
            
        
