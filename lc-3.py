class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=res=0
        ms=set()
        for j in range(len(s)):
            while(s[j] in ms):
                ms.remove(s[i])
                i+=1
            ms.add(s[j])
            res=max(res,j-i+1)
        return res

sol=Solution()
print(sol.lengthOfLongestSubstring("c"))