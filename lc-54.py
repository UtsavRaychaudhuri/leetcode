class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def dfs(matrix,i,j):
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]):
                return
            print(matrix[i][j])
            dfs(matrix,i,j+1)
            dfs(matrix,i+1,j)
            dfs(matrix,i,j-1)
            dfs(matrix,i-1,j)

        dfs(matrix,0,0)

sol=Solution()
sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])