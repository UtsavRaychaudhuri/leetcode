class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        def mp(prices,i,cp,buy,sell):
            if i>=len(prices):
                return 0
            if sell:
                return max(prices[i]-cp-fee,mp(prices,i+1,cp,buy=False,sell=True))
            if buy:
                return max(mp(prices,i+1,prices[i],buy=False,sell=True),mp(prices,i+1,cp,buy=True,sell=False))
        return mp(prices,0,0,buy=True,sell=False)

sol=Solution()
print(sol.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))