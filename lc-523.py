class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(0,len(nums)):
            local_sum=nums[i]
            for j in range(i+1,len(nums)):
                local_sum=local_sum+nums[j]
                if k==0 and local_sum==0:
                    return True
                elif k!=0 and (local_sum%k==0 or local_sum==0):
                    return True
        return False