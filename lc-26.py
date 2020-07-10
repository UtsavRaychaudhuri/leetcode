class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.removeDuplicate(nums,0,1)
    
    def removeDuplicate(self,nums,i,j):
        if j==len(nums):
            return i+1
        if nums[i]==nums[j]:
            return self.removeDuplicate(nums,i,j+1)
        elif i+1!=j:
            nums[i+1]=nums[j]
            return self.removeDuplicate(nums,i+1,j+1)
        return self.removeDuplicate(nums,i+1,j+1)
        