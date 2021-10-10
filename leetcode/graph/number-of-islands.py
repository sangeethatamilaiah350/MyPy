class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        c=0
        def dfs(i,j):
            
            if   i>=n or j<0 or i<0 or j>=m or grid[i][j] !="1" :
                return
        
            grid[i][j]="2" # mark current as 2
            dfs(i-1,j)#up
            dfs(i,j+1)#right
            dfs(i,j-1)#left
            dfs(i+1,j)#down
                
        
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(i,j)
                    c+=1
        return c
