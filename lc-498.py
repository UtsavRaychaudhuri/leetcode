class Solution:
    def findDiagonalOrder(self, matrix):
        def dt(matrix,i,j):
            res=[]
            while(i>=0 and j>=0 and j<len(matrix[0]) and i<len(matrix)):
                res.append(matrix[i][j])
                i+=1
                j-=1
            return res
        gofw=True
        fres=[]
        for j in range(len(matrix[0])):
            if gofw:
                gofw=False
                fres+=dt(matrix,0,j)[::-1]
            else:
                gofw=True
                fres+=dt(matrix,0,j)
        for i in range(1,len(matrix)):
            if gofw:
                gofw=False
                j=len(matrix[0])-1
                fres+=dt(matrix,i,j)[::-1]
            else:
                gofw=True
                j=len(matrix[0])-1
                fres+=dt(matrix,i,j)
        return fres
            
sol=Solution()
print(sol.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))