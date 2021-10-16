#only row is sorted


#leetcode
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        col=len(matrix[0])
        high=(len(matrix)*col)-1
        
        
        while low<=high:
            mid=(low+high)//2
            midval=matrix[mid//col][mid%col]
            if midval==target:
                return True
            elif target>midval:
                low=mid+1
            else:
                high=mid-1
                
        return False
    
    
#both row and col is sorted
class Solution:
	def matSearch(self,mat, N, M, X):
		# Complete this function
		i=0
		j=M-1
		while j!=-1   and  i!=N:
		    val=mat[i][j]
		   # print(val)
		    if val==X:
		        return 1
		    elif X<val:
		        j-=1
		    else:
		        i+=1
		return 0
