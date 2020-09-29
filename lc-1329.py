class Solution:
    def diagonalSort(self, mat):
        def ds(mat,i,j):
            res=[]
            while(i<len(mat) and j<len(mat[0])):
                res.append(mat[i][j])
                i+=1
                j+=1
            return sorted(res)
        def put(matrix,i,j,res):
            for v in res:
                matrix[i][j]=v
                i+=1
                j+=1
        for i in range(len(mat)-1,-1,-1):
            res=ds(mat,i,0)
            put(mat,i,0,res)
        for j in range(1,len(mat[0])):
            res=ds(mat,0,j)
            put(mat,0,j,res)
        return mat

sol=Solution()
print(sol.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))