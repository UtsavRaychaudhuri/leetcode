class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        i=len(nums)-2
        valueneeded=1
        canreach=False
        while(i>=0):
            if nums[i]>=valueneeded:
                canreach=True
                valueneeded=1
            else:
                valueneeded+=1
                canreach=False
            i-=1
        return canreach

sol=Solution()
sol.canJump([1,2,0,1])