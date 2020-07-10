class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        a=[1]*(len(nums))
        for j in range(1,len(nums)):
            for i in range(0,j):
                if nums[j]>nums[i] and a[i]+1>a[j]:
                    a[j]+=1
        return max(a)
            
        