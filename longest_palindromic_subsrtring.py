class Solution(object):
    def __init__(self):
        self.long=0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestsubstring=0
        longeststring=""
        if len(s)==1:
            return s
        for i in range(0,len(s)):
            for j in range(0,len(s)+1):
                string=s[i:j]
                if string==string[::-1]:
                    if j-i+1>longestsubstring:
                        longestsubstring=j-i+1
                        longeststring=string
        return longeststring-1

sol=Solution()
sol.longestPalindrome("bb")
