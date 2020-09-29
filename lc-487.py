class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numzeros=res=i=0
        for j in range(len(nums)):
            if nums[j]==0:
                numzeros+=1
            while(numzeros>1):
                if nums[i]==0:
                    numzeros-=1
                i+=1
            res=max(res,j-i+1)
        return res
        

sol=Solution()
sol.findMaxConsecutiveOnes([1,0,1,1,0])