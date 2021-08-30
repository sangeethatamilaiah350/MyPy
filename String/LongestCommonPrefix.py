  class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        compare=arr[0]
        def check(string):
            nonlocal compare
            flag=0
            ns=len(string)
            nc=len(compare)
            n=min(ns,nc)
            i=0
            mid=''
            while i<n:
            
                if compare[i]==string[i]:
                    flag=1
                    mid+=compare[i]
                    i=i+1
                else:
                    break
                
            #print("reached")

            if flag==1:
                compare=mid
            else:
                
                compare=-1
                
        for i in range(1,n):
            if compare!=-1:
                check(arr[i])
            else:
                return compare
                
        return compare
