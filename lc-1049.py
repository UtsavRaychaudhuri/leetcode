class Solution:
    def lastStoneWeightII(self, stones):
        self.dp=[]
        for i in range(len(stones)+1):
            self.dp.append([-1]*(sum(stones)//2+1))
        def ls(stones,sum,target,i):
            if i==len(stones):
                return 0
            if sum==target:
                return 0
            taken=0
            if self.dp[i][sum]==-1:
                if stones[i]+sum<=target:
                    taken = stones[i]+ls(stones,sum+stones[i],target,i+1)
                nottaken = ls(stones,sum,target,i+1)
                self.dp[i][sum] = max(taken,nottaken)
                return self.dp[i][sum]
            return self.dp[i][sum]

        return int((sum(stones)/2-ls(stones,0,sum(stones)//2,0))*2)
            
sol=Solution()
print(sol.lastStoneWeightII([8,2,4,4,8]))
            
