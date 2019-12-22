class Solution(object):
    def __init__(self):
        self.low=999999999999
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.minpathsum(grid,0,0,0)
        return self.low
    
    def minpathsum(self,grid,i,j,count,dp=[]):
        if i==len(grid) or j==len(grid[0]) or [i,j] in dp:
            return
        dp.append([i,j])
        count+=grid[i][j]
        if i==len(grid)-1 and j==len(grid[0])-1:
            if count<self.low:
                self.low=count
            return
        self.minpathsum(grid,i,j+1,count,dp)
        self.minpathsum(grid,i+1,j,count,dp)
        
sol=Solution()
print(sol.minPathSum([[0]]))