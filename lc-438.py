import collections

class Solution:
    def findAnagrams(self, s, p):
        if len(s)<len(p):
            return []
        ps=collections.defaultdict(int)
        for i in p:
            ps[i]+=1
        i=0
        j=0
        res=[]
        ss=collections.defaultdict(int)
        while(j<len(s)):
            if j-i<len(p):
                ss[s[j]]+=1
            if j-i>=len(p):
                ss[s[i]]-=1
                if ss[s[i]]==0:
                    del ss[s[i]]
                ss[s[j]]+=1
                i+=1
            if ss==ps:
                res.append(i)
            j+=1
        return res
                

sol=Solution()
sol.findAnagrams(s="cbaebabacd", p="abc")