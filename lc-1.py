class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_set={}
        for i,v in enumerate(nums):
            if target-v in my_set:
                return [i,my_set[target-v]]
            my_set[v]=i
        
            
        
        