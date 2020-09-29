import sys


class Solution:
    def maxProfit(self, prices):
        def mp(i):
            return max(prices[i]-mp(i+1),mp(i+1))
        return mp(len(prices)-1)

sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
        