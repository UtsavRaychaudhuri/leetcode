class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lis(nums,prev,i): 
            if i>=len(nums):
                return 0
            if nums[i]<=prev:
                return 0
            print(prev,nums[i])
            taken=0
            taken=1+lis(nums,nums[i],i+1)
            nottaken=lis(nums,prev,i+1)
            return max(taken,nottaken)
            
        return lis(nums,-999999999999,0)

sol=Solution()
print(sol.lengthOfLIS([-2,-1]))

# [1,3,6,7,9,4,10,5,6]
# [-2,-1]
# [4,10,4,3,8,9]
# [2,2]
# [18,55,66,2,3,54]