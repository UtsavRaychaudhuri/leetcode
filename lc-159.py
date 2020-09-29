import collections

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=collections.defaultdict(int)
        i=res=0
        for j in range(len(s)):
            d[s[j]]+=1
            while(len(d)>2):
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            res= max(res,j-i+1)
        return res

sol=Solution()
sol.lengthOfLongestSubstringTwoDistinct("eceba")