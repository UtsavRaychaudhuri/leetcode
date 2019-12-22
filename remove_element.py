class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return len(nums)
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                i-=1
                if i<0:
                    i=0
            else:
                i+=1
        return len(nums)

sol=Solution()
print(sol.removeElement([],3))