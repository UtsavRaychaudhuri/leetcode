import collections

class Solution:
    def findRedundantConnection(self, edges):
        d=collections.defaultdict(set)
        for i,v in edges:
            d[i].add(v)
            d[v].add(i)
        for i,v in edges[::-1]:
            if len(d[i])>1 and len(d[v])>1:
                return [i,v]

sol=Solution()
sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])