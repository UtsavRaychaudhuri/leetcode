class Solution:
    def spiral(self,matrix):
        self.seen=set()
        def dfs(matrix,i,j):
            if (i,j) in self.seen:
                return
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
                return
            print(matrix[i][j])
            self.seen.add((i,j))
            dfs(matrix,i,j+1)
            dfs(matrix,i+1,j)
            dfs(matrix,i,j-1)
            dfs(matrix,i-1,j)
        dfs(matrix,0,0)

sol=Solution()
sol.spiral([[1,2,3],
            [4,5,6],
            [7,8,9]])
