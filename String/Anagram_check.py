class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d={}#hash
        lena=len(a)
        lenb=len(b)
        
        if lena!=lenb:
            return False
        else:
            
            for i in a:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1#incrementing count
            
            for i in b:
                
                if i not in d:
                    
                    return False
                else:
                    d[i]-=1#decrementing count
            
            val=d.values()
            for i in val:
                
                if i!=0:#if all are zero then its anagram
                    return False
            return True      
                    
        
