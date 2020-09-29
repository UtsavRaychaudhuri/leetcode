class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=len(nums):
                tmp=nums[i]
                nums[i]=-1
                nums.append(tmp)
            else:
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
        for i in range(len(nums)):
            if nums[i]==-1 or nums[i]!=i:
                return i


                
sol=Solution()
sol.missingNumber([9,6,4,2,3,5,7,0,1])