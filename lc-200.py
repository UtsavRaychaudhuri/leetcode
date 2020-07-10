class Solution(object):
    def numIslands(self, a):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numofislands=0
        for i,k in enumerate(a):
            for j,v in enumerate(k):
                if v=="1":
                    numofislands+=self.dfs(i,j,a)
        return numofislands
    def dfs(self,i,j,a):
        if i<0 or i>=len(a) or j>=len(a[i]) or j<0 or a[i][j]=="0":
            return
        else:
            a[i][j]="0"
        self.dfs(i+1,j,a)
        self.dfs(i-1,j,a)
        self.dfs(i,j+1,a)
        self.dfs(i,j-1,a)
        return 1
        