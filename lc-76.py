from collections import OrderedDict
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def checkdt(d,t):
            if len(d)!=len(t):
                return False
            for i in d:
                if d[i]<t[i]:
                    return False
            return True

        d=collections.defaultdict(int)
        t=collections.Counter(t)
        i=0
        res=999999
        for j in range(len(s)):
            if s[j] in t:
                d[s[j]]+=1
            while(checkdt(d,t)):
                if res==999999:
                    res=(i,j)
                elif (j-i)<(res[1]-res[0]):
                    res=(i,j)
                if s[i] in d:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                i+=1
        if res==999999:
            return ""
        else:
            return s[res[0]:res[1]+1]
                

sol=Solution()
print(sol.minWindow("a",
"aa"))