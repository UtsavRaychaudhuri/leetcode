class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_sum=-9999999
        local_sum=0
        for i in nums:
            local_sum+=i
            if i>local_sum:
                local_sum=i
            if local_sum>global_sum:
                global_sum=local_sum
        return global_sum

sol=Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
            