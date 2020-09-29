class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        self.memo=[-1]*len(nums)
        if len(nums)<=2:
            return max(nums)
        def rob(nums,i):
            if i==len(nums)-1:
                return nums[i]
            if i>=len(nums)-1:
                return 0
            if self.memo[i]==-1:
                self.memo[i] = max(nums[i]+rob(nums,i+2),nums[i+1]+rob(nums,i+3))
                return self.memo[i]
            return self.memo[i]
        return rob(nums,0)

sol=Solution()
print(sol.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))