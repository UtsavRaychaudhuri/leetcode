class Solution:
    def pivotIndex(self, nums):
        j=len(nums)-1
        i=0
        sumi=nums[0]
        sumj=nums[-1]
        while(j-i!=2):
            if sumi>sumj:
                j-=1
                sumj+=nums[j]
            else:
                i+=1
                sumi+=nums[i]
        if sumi==sumj:
            return i+1
        else:
            return -1

sol=Solution()
sol.pivotIndex([-1,-1,-1,-1,-1,0])