class Solution(object):
    def longestSubsequence(self, arr, diff):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        res = {}
        for num in arr:
            res[num] = res[num - diff] + 1 if (num - diff) in res else 1
        return max(res.values())


sol=Solution()
print(sol.longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8],0))