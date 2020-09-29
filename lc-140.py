import collections

class Solution:
    def wordBreak(self, s, worddict):
        d=collections.defaultdict(list)
        start=set()
        self.l=[]
        def dfs(d,i,str,strsp):
            if str not in s:
                return
            if str==s:
                self.l.append(" ".join(strsp))
                return 
            if i not in d:
                return
            for j in d[i]:
                dfs(d,j,str+j,strsp+[j])          
        for i in worddict:
            try:
                d[i].append(i)
                if s.index(i)==0:
                    start.add(i)
                for j in worddict:
                    if i!=j and i+j in s:
                        d[i].append(j)
            except:
                pass
        for i in start:
            dfs(d,i,i,[i])
        return self.l
        
        
sol=Solution()
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
