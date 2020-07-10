class Solution(object):
    def dfs(self,i,j,count,a):
        if i<0 or i>=len(a) or j>=len(a[i]) or j<0 or a[i][j]<count or a[i][j]==-1:
            return
        else:
            a[i][j]=count
        self.dfs(i+1,j,count+1,a)
        self.dfs(i-1,j,count+1,a)
        self.dfs(i,j+1,count+1,a)
        self.dfs(i,j-1,count+1,a)
        
    def wallsAndGates(self, a):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        for i,k in enumerate(a):
            for j,v in enumerate(k):
                if v==0:
                    self.dfs(i,j,0,a)
        return a
        
    
        