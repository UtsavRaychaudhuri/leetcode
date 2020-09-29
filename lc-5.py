class Solution:
    def longestPalindrome(self, s):
        s1=s[::-1]
        def lp(s,s1,i,j):
            if i==len(s) or j==len(s1):
                return ""
            if s[i]==s1[j]:
                return s[i]+lp(s,s1,i+1,j+1)
            return max(lp(s,s1,i+1,j),lp(s,s1,i,j+1))
        return lp(s,s1,0,0)

sol=Solution()
print(sol.longestPalindrome("babad"))
        