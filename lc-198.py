class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        my_max=nums[0]
        global_max=my_max
        i=0
        for j in range(2,len(nums)):
            nums[j]+=my_max
            if nums[j]>global_max:
                global_max=nums[j]
            if nums[i+1]>my_max:
                my_max=nums[i+1]
            i+=1
        if len(nums)<4:
            return max(nums)
        return global_max