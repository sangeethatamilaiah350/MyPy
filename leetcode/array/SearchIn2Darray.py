#only row is sorted

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
            
        
