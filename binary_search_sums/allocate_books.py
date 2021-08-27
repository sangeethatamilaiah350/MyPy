class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        def possible(val):
            #print("possible",val)
            student=1
            pages=0
            for i in A:
                #print(i)
                if i>val:
                    return False
                if pages+i>val:
                    
                    student+=1
                    pages=i
                    if pages>val:
                        return False
                else:
                    pages+=i
                #print(student)
            if student==M:
                return True
            else:
                return False
        l=min(A)
        h=sum(A)
        res=-1
        while l<=h:
            #print("loop")
            mid=(l+h)//2
            if possible(mid):
                #print(mid,"mid")
                res=mid
                h=mid-1
            else:
                l=mid+1
             
        return res   

