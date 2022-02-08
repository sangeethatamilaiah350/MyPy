class Solution:
    def maxLen(self, n, arr):
        #Code here
        if sum(arr)==0:
            return n
        d={}
        sums=0
        maxlen=0
        for i in range(n):
            sums+=arr[i]
            if sums==0:
                maxlen=i+1
            
            elif sums in d:
                maxlen=max(maxlen,i-d[sums])
            else:
                d[sums]=i
        return maxlen
