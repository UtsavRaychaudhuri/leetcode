class Solution:
    def ldps(self,nums):
        def ldps(nums,i,arr):
            if len(arr)>1:
                if arr[-1]%arr[-2]!=0 and arr[-2]%arr[-1]!=0:
                    return 0
            if i>=len(nums):
                return 0
            return max(1+ldps(nums,i+1,arr+[nums[i]]),ldps(nums,i+1,arr))
        return ldps(nums,0,[])-1

sol=Solution()
print(sol.ldps([1,2,3,6] ))