import collections

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
        record = {}
        for a,b in zip(cumsum[:-1],cumsum[1:]):
            b = b%k if k else b
            a = a%k if k else a
            if b in record:
                return True
            record[a] = 1 
        return False
        


sol=Solution()
sol.checkSubarraySum([23, 2, 4, 6, 7],  k=6)