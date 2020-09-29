class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def lip(i,j,matrix,prev):
            if i<0 or j<0 or i==len(matrix) or j==len(matrix[0]):
                return 0
            if prev is not None:
                if matrix[i][j]<=prev:
                    return 0
            if (i,j) in d:
                return d[(i,j)]
            return 1+max(lip(i,j+1,matrix,matrix[i][j]),lip(i,j-1,matrix,matrix[i][j]),lip(i+1,j,matrix,matrix[i][j]),lip(i-1,j,matrix,matrix[i][j]))
        gans=0
        d=dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = lip(i,j,matrix,None)
                d[(i,j)]=ans
                gans=max(ans,gans)
        return gans
                
sol=Solution()
sol.longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]])