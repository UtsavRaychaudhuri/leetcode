class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        return self.climbstairs(n,dp)
        
    def climbstairs(self,n,dp):
        if n<0:
            return 0
        if n==0:
            return 1
        if dp[n]>0:
            return dp[n]
        dp[n]=self.climbstairs(n-1,dp) + self.climbstairs(n-2,dp)
        return dp[n]
        