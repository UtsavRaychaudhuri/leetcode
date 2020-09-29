class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo=[]
        for i in range(len(nums)+1):
            self.memo.append([-1]*2001)
        def subsetsum(nums,n,s):
            if n==len(nums):
                if s==S:
                    return 1
                return 0
            if self.memo[n][s+1001]==-1:
                self.memo[n][s+1001] = subsetsum(nums,n+1,s+nums[n])+subsetsum(nums,n+1,s-nums[n])
                return self.memo[n][s+1001]
            return self.memo[n][s+1001]
        return subsetsum(nums,0,0)
        
sol=Solution()
print(sol.findTargetSumWays([0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39],2))