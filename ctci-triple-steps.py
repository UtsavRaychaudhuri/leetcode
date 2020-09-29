from collections import defaultdict
class Solution:
    def numways(self,n):
        memo=defaultdict(lambda:-1)
        self.ways=0
        return self.numWays(n,memo)

    def numWays(self,n,memo):
        if memo[n]!=-1:
            return memo[n]
        if n<0:
            return 0
        if n==0:
            return 1
        if memo[n]==-1:
            memo[n]=self.numWays(n-1,memo)+self.numWays(n-2,memo)+self.numWays(n-3,memo)
            return memo[n]
    
sol=Solution()
print(sol.numways(7))