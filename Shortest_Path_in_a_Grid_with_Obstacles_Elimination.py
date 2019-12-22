class Solution(object):
    def __init__(self):
        self.highestcount=9999999999

    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        try:
            self.dfs(grid,k,0,0,0,999999999999)
        except:
            pass
        return self.highestcount

    def dfs(self,grid,actualk,i,j,count,highestcount):
        print(i,j)
        if i<0 or j<0 or j>len(grid[0])-1 or i>len(grid)-1 or actualk<0:
            return
        if grid[i][j]==1:
            actualk-=1
        if j==len(grid[0])-1 and i==len(grid)-1:
            if count<self.highestcount:
                highestcount=count
                self.highestcount=count
                return
        self.dfs(grid,actualk,i,j+1,count+1,highestcount) #Right
        self.dfs(grid,actualk,i+1,j,count+1,highestcount) #Down
        self.dfs(grid,actualk,i,j-1,count+1,highestcount) #Left
        self.dfs(grid,actualk,i-1,j,count+1,highestcount) #Up

sol=Solution()
sol.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]],1)

