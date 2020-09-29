class Solution:
    def minCost(self, costs):
        def mc(i,j):
            if j==len(costs):
                return 0
            self.total_cost=costs[j][i]
            if i==0:
                self.total_cost+=min(mc(1,j+1),mc(2,j+1))
            if i==1:
                self.total_cost+=min(mc(0,j+1),mc(2,j+1))
            if i==2:
                self.total_cost+=min(mc(1,j+1),mc(0,j+1))
            return self.total_cost
        self.total_cost=0
        taken=mc(0,0)
        self.total_cost=0
        taken1=mc(1,0)
        self.total_cost=0
        taken2=mc(2,0)
        self.total_cost=0
        return min(taken,taken1,taken2)

            
            
sol=Solution()
print(sol.minCost([[17,2,17],[16,16,5],[14,3,19]]))