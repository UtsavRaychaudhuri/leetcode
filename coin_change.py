class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array=[amount+1]*(amount+1)
        array[0]=0
        for i in range(1,amount):
            for j in coins:
                if i-j>=0:
                    array[i]=min(array[i-j]+1,array[i])
        return array[amount-1]+1

sol=Solution()
print(sol.coinChange([1, 2, 5],11))
