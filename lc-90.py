import collections

class Solution(object):
    def subsetsWithDup(self, S):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

sol=Solution()
sol.subsetsWithDup([1,2,2])