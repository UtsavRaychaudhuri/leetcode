class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_set=set()
        i=0
        while(i<len(nums)):
            if nums[i] not in my_set:
                my_set.add(nums[i])
                nums.pop(i)
            else:
                i+=1
        return nums