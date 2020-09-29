class Solution:
    def coinChange(self, coins, amount):
        def subsetsum(coins,n,amt):
            if amt==amount:
                return 0
            if n==len(coins):
                if amt==amount:
                    return 0
                return 99999999
            if coins[n]<=amount-amt:
                return min(subsetsum(coins,n,amt+coins[n])+1,subsetsum(coins,n+1,amt))
            else:
                return subsetsum(coins,n+1,amt)
        val = subsetsum(coins,0,0)
        if val==99999999:
            return -1
        return val

sol=Solution()
print(sol.coinChange(coins = [2,5,10,1], amount = 27))