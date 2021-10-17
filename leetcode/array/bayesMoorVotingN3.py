class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        num1=''
        num2=''
        for i in nums:
            if i==num1:
                c1+=1
            
            elif i==num2 :
                c2+=1
            elif c1==0:
                num1=i
                c1=1
                
            elif c2==0:
                
                num2=i
                c2=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for i in nums:
            if i==num1:
                c1+=1
            if i==num2:
                c2+=1
        val=len(nums)//3
        if c1>val and c2>val:
            return [num1,num2]
        if c1>val:
            return [num1]
        if c2>val:
            return [num2]
        
        return []
            
        
