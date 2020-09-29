class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        res=float("inf")
        sum=0
        for j in range(len(nums)):
            sum+=nums[j]
            while(sum>=s):
                if sum-nums[i]>=s:
                    sum-=nums[i]
                    i+=1
                else:
                    res=min(res,j-i+1)
                    break
        if res==float("inf"):
            return 0
        return res
                
sol=Solution()
sol.minSubArrayLen(s = 6, nums = [10,2,3])