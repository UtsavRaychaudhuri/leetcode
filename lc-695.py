class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.local_max=self.global_max=0
        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            if grid[i][j]==1:
                grid[i][j]=0
                self.local_max+=1
            else:
                return
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.local_max=0
                    dfs(grid,i,j)
                    self.global_max=max(self.local_max,self.global_max)
        return self.global_max
                    
sol=Solution()
sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])