class Solution:
    def longestSubarray(self, nums, limit):
        i=0
        j=0
        mini=99999999999999
        maxi=-9999999999999
        res=0
        while(j<len(nums)):
            maxi=max(maxi,nums[j])
            mini=min(mini,nums[j])
            if maxi-mini>limit:
                maxi=nums[j]
                mini=nums[j]
                res=max(res,j-i)
                i+=1
            j+=1
        return max(res,j-i)

sol=Solution()
sol.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 1)