class Solution(object):
    def __init__(self):
        self.count=0
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid[0])
        n=len(obstacleGrid)
        self.dfs(m,n,1,1,obstacleGrid)
        return self.count
        
        
    def dfs(self,m,n,i,j,obstacleGrid):
        if i>m or j>n:
            return
        elif obstacleGrid[i-1][j-1]==1:
            return
        else:
            if i==m and j==n:
                self.count+=1
                return
        self.dfs(m,n,i+1,j,obstacleGrid)
        self.dfs(m,n,i,j+1,obstacleGrid)

sol=Solution()
print(sol.uniquePathsWithObstacles([[0],[0]]))