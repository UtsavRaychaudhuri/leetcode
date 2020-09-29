import collections
class Solution:
    def maxDistance(self, grid):
        land=[]
        water=[]
        dis=collections.defaultdict(lambda:9999999)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    land.append((i,j))
                else:
                    water.append((i,j))
        if len(land)==0 or len(water)==0:
            return -1
        for i,j in land:
            for k,l in water:
                if abs(k-i)+abs(l-j)<dis[(k,l)]:
                    dis[(k,l)]=abs(k-i)+abs(l-j)
        return max(dis.values())

sol=Solution()
sol.maxDistance([[1,0,0],[0,0,0],[0,0,0]])