class Solution:
    def minSubArrayLen(self, s, nums):
        i=0
        j=0
        sum=0
        length=99999999
        while(j!=len(nums)):
            if sum<s:
                sum+=nums[j]
                j+=1
            else:
                length=min(length,j-i)
                sum-=nums[i]
                i+=1
        if j-i<length:
            return j-i-1
        return length-1

sol=Solution()
print(sol.minSubArrayLen(7,[2,3,1,2,4,3]))