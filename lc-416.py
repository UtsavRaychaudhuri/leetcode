class Solution:
    def canPartition(self, nums):
        def subsetsum(nums,sum,n):
            if sum==0:
                return True
            if n<0:
                return False
            if self.memo[n][sum]==-1:
                if nums[n]<=sum:
                    self.memo[n][sum]= subsetsum(nums,sum-nums[n],n-1) or subsetsum(nums,sum,n-1)
                    return self.memo[n][sum]
                else:
                    self.memo[n][sum]= subsetsum(nums,sum,n-1)
                    return self.memo[n][sum]
            return self.memo[n][sum]
        if sum(nums)%2==0:
            self.memo=[]
            for i in range(len(nums)+1):
                self.memo.append([-1]*(sum(nums)//2+1))
            return subsetsum(nums,sum(nums)//2,len(nums)-1)
        return False
        
                
sol=Solution()
print(sol.canPartition([1, 2, 3, 5]))