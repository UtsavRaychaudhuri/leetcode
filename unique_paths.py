class Solution(object):
    def __init__(self):
        self.count=0

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.dfs(m,n,1,1)
        return self.count
        
        
    def dfs(self,m,n,i,j):
        if i>m or j>n:
            return
        else:
            if i==m and j==n:
                self.count+=1
                return
        self.dfs(m,n,i+1,j)
        self.dfs(m,n,i,j+1)

sol=Solution()
print(sol.uniquePaths(7,3))