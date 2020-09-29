# class Solution:
#     def change(self, amount, coins):
#         self.memo=[]
#         for i in range(len(coins)):
#             self.memo.append([-1]*(amount+1))
#         def subsetsum(amount,coins,i):
#             if amount==0:
#                 return 1
#             if i==-1:
#                 return 0
#             if self.memo[i][amount]==-1:
#                 if coins[i]<=amount:
#                     self.memo[i][amount] = subsetsum(amount-coins[i],coins,i)+subsetsum(amount,coins,i-1)
#                     return self.memo[i][amount]
#                 else:
#                     self.memo[i][amount] = subsetsum(amount,coins,i-1)
#                     return self.memo[i][amount]
#             else:
#                 return self.memo[i][amount]
#         return subsetsum(amount,coins,len(coins)-1)

class Solution:
    def change(self, amount, coins):
        if len(coins)==0 and amount==0:
            return 1
        self.memo=[]
        for i in range(len(coins)+1):
            self.memo.append([-1]*(amount+1))
        def cc(coins,i,sum,target):
            if i==len(coins):
                return 0
            if sum==target:
                return 1
            if self.memo[i][sum]==-1: 
                if sum<=target:
                    self.memo[i][sum]=cc(coins,i,sum+coins[i],target)+cc(coins,i+1,sum,target)
                    return self.memo[i][sum]
                self.memo[i][sum]=0
                return 0
            return self.memo[i][sum]
        return cc(coins,0,0,amount)




sol=Solution()
print(sol.change( amount = 5, coins = [2,5] ))