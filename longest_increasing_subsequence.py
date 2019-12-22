class Solution(object):

    def lengthOfLIS(self,nums):
        a=[1]*(len(nums))
        for j in range(1,len(nums)):
            for i in range(0,j):
                if nums[j]>nums[i] and a[i]+1>a[j]:
                    a[j]+=1
        return max(a)



sol=Solution()
sol.lengthOfLIS([-2,-1])

# 10  9   2   5   3   7   101     18
# 1   1   1   2   2   3   4       4 
