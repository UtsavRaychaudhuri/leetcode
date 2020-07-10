class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            nums[lastNonZeroFoundAt] = nums[i]
            lastNonZeroFoundAt+=1
        for i in range(lastNonZeroFoundAt,len(nums)):
            nums[i]=0

            
            
        