class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        return_sum=0
        for i in range(0,len(nums),2):
            return_sum+=nums[i]
        return return_sum
        