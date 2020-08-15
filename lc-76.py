from collections import OrderedDict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a=OrderedDict()
        v=dict()
        for i in t:
            if i in v:
                v[i]+=1
            else:
                v[i]=1
        u=dict(v)

        self.best=(0,0,99999999999999999)
        for i in range(len(s)):
            if s[i] in u:
                if u[s[i]]==1:
                    del(u[s[i]])
                else:
                    u[s[i]]-=1
                if s[i] in a:
                    a.pop(s[i])
                a[s[i]]=i
                if len(u)==0:
                    val=a[next(iter(a))]
                    val2=a[next(reversed(a))]
                    if (val2-val)<self.best[2]:
                        self.best=(val,val2,val2-val)
                    u=dict(v)
                    del(u[next(iter(a))])
                    a.pop(next(iter(a)))
            elif s[i] in a:
                a.pop(s[i])
                a[s[i]]=i
        if self.best[2]==99999999999999999:
            return ""
        return s[self.best[0]:self.best[1]+1]
                

sol=Solution()
print(sol.minWindow(s = "aa", t = "aa"))