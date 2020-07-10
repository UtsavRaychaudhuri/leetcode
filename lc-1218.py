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