import collections
from functools import lru_cache
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def bb(nums,i):
            if i>=len(nums):
                return 0
            if len(nums)==1:
                return nums[0]
            a,b=1 if i==0 else nums[i-1],1 if i==len(nums)-1 else nums[i+1]
            return max(a*nums[i]*b + bb(nums[:i]+nums[i+1:],0),bb(nums,i+1))
        ans = bb(tuple(nums),0)
        return ans
                
sol=Solution()
print(sol.maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2,5,5]))