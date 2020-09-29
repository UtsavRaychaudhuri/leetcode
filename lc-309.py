class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def mp(prices,i,cp,sell):
            if i>=len(prices):
                return 0
            if sell:
                return max(cp-prices[i],mp(prices,i+1,cp,sell))
            return max(prices[i]+mp(prices,i+1,prices[i],sell=True),mp(prices,i+1,cp,sell=False))
        return mp(prices,0,0,False)
        
        

sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))