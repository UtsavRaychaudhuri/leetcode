class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumn=sum(nums)
        i,j=0,len(nums)-1
        while(sumn)!=k:
            if i>j:
                break
            if sumn>k:
                if nums[i]>nums[j]:
                    sumn-=nums[i]
                    i+=1
                else:
                    sumn-=nums[j]
                    j-=1
            elif sumn<k:
                if nums[i]<nums[j]:
                    sumn-=nums[i]
                    i+=1
                else:
                    sumn-=nums[j]
                    j-=1

        if i>j:
            return 0
        return j-i+1
            
sol=Solution()
sol.maxSubArrayLen([-2,1,-3,4,-1,2,1,-5,4],
0)