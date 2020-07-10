class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A)==0:
            return 0
        if len(A)==1:
            return min(A[0])
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                if j-1>=0 and j+1<len(A[0]):
                    A[i][j]+=min(A[i-1][j-1],A[i-1][j],A[i-1][j+1])
                elif j-1>=0:
                    A[i][j]+=min(A[i-1][j-1],A[i-1][j])
                elif j+1<len(A[0]):
                    A[i][j]+=min(A[i-1][j],A[i-1][j+1])
                else:
                    A[i][j]+=A[i-1][j]
        return min(A[len(A)-1])
        
        