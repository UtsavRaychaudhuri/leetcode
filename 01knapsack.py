class Solution:
    def knapsack(self,val,weight,W):
        def dfs(val,weight,W,i):
            if i==0:
                return 0
            if weight[i]<W:
                return max(val[i]+dfs(val,weight,W-weight[i],i-1),dfs(val,weight,W,i-1))
            else:
                return dfs(val,weight,W,i-1)
        dfs(val,weight,W,len(val)-1)

sol=Solution()
sol.knapsack([100,200,300,100,200],[3,2,1,1,8],5)

