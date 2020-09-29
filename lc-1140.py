class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        def tp(i,j,M,piles):
            if i==M and j==M:
                return 0
            if i<(2*M):
                M=max(i,M)
                return piles[i]+tp(i+1,j,M,piles)
            if j<(2*M):
                M=max(j,M)
                return piles[i]+tp(j+1,j+1,M,piles)
        tp(0,0,1,piles)
sol=Solution()
sol.stoneGameII([2,7,9,4,4])