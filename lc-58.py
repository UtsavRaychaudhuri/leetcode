class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for v in s[::-1]:
            if v.isspace():
                if cnt: break
            else: cnt += 1
        return cnt

        