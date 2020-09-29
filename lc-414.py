class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash=[0]*(len(prices))
        hold=[0]*(len(prices))
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            cash[i]=max(cash[i-1],hold[i-1]+prices[i]-fee)
            hold[i]=max(hold[i-1],cash[i]-prices[i])
        return cash[-1]

sol=Solution()
sol.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)