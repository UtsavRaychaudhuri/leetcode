class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_set=set()
        sum=0
        count=0
        for i in nums:
            if i==k or sum+i-k in my_set:
                count+=1
            sum+=i
            my_set.add(sum)
        if sum-k in my_set:
            return count+1
        return count

sol=Solution()
sol.subarraySum([1,1,1], k = 2)