class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        res=S[::-1]
        ans=""
        def reverse(start,end):
            nonlocal ans
            intermediate=res[start:end]
            #print(intermediate,start)
            ans+=intermediate[::-1]+'.'
                
                
        
        start=0
        for i in range(len(res)):
            if res[i]=='.':
                reverse(start,i)
                start=i+1
                #print("i",i)
        reverse(start,i+1)#last word
        #print(res)
        #print(ans)
        return ans[:-1]#to remove last '.'
            
            
        
