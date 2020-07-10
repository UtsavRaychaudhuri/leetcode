class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        if len(A)==0:
            return 0
        if len(A)==1:
            return min(A[0])
        for i in range(1,len(A)):
            for j in range(len(A)):
                my_array=A[i-1][0:j]
                my_array.extend(A[i-1][j+1:])
                A[i][j]+=min(my_array)
        return min(A[len(A)-1])
                
        