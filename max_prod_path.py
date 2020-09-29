def matricproduct(matrix):
    def mp(matrix,i,j):
        print(i,j)
        if i==len(matrix) or j==len(matrix[0]):
            return 1
        down=matrix[i][j]*mp(matrix,i+1,j)
        # right=matrix[i][j]*mp(matrix,i,j+1)
        return max(down,matrix[i][j]*mp(matrix,i,j+1))
    return mp(matrix,0,0)

print(matricproduct([[1,2,3],[4,5,6],[7,8,9]]))
