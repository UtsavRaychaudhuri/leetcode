class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(nums)-1
        while(i!=j):
            if nums[i]+nums[j]>target:
                j-=1
                continue
            if nums[i]+nums[j]<target:
                i+=1
            if nums[i]+nums[j]==target:
                return i+1,j+1
        