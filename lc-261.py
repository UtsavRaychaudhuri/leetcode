import collections
class Solution:
    def validTree(self, n, edges):
        d=collections.defaultdict(list)
        for i in edges:
            start=i[0]
            d[i[0]].append(i[1])
        self.seen=set()
        def dfs(i,d):
            if i in self.seen:
                return True
            self.seen.add(i)
            for j in range(len(d[i])):
                if d[i][j] in d:
                    ret = dfs(d[i][j],d)
                    if ret is not None:
                        return True
                elif d[i][j] in self.seen:
                    return True
                else:
                    self.seen.add(d[i][j])
        if dfs(0,d) is None:
            return len(self.seen)==n
        return False
            
sol=Solution()
sol.validTree(n = 2, edges = [[,0]])