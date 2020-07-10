class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        count=1
        maxcount=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
                if count>maxcount:
                    maxcount=count
            else:
                count=1
        return maxcount