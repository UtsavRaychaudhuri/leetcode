class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.count=0
        def dfs(grid,i,j,stack):
            while(stack):
                i,j = stack.pop()
                if grid[i][j]=="0" or grid[i][j]==-1:
                    continue
                grid[i][j]=-1
                if i+1<len(grid):
                    stack.append([i+1,j])
                if i-1>=0:
                    stack.append([i-1,j])
                if j-1>=0:
                    stack.append([i,j-1])
                if j+1<len(grid[0]):
                    stack.append([i,j+1])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j,[[i,j]])
                    self.count+=1
        return self.count
        

sol=Solution()
sol.numIslands( [["1","1","1"],["0","1","0"],["1","1","1"]])