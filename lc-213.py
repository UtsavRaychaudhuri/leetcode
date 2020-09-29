class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==2:
            return max(nums)
        self.memo=[-1]*(len(nums)+1)
        def rob(nums,i,j):
            if i>j:
                return 0
            if i==j:
                return nums[i]
            if self.memo[i]==-1:
                self.memo[i] = max(nums[i]+rob(nums,i+2,j),nums[i+1]+rob(nums,i+3,j))
                return self.memo[i]
            return self.memo[i]
        return max(rob(nums,0,len(nums)-2),rob(nums,1,len(nums)-1))

sol=Solution()
print(sol.rob([1,3,1]))