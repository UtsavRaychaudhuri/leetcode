class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        my_set=[]
        for i,val in enumerate(matrix):
            for j,val1 in enumerate(val):
                if val1==0:
                    my_set.append([i,j])       
        for i,j in my_set:
            for k,_ in enumerate(matrix[i]):
                matrix[i][k]=0
            for i,val in enumerate(matrix):
                matrix[i][j]=0
        return matrix