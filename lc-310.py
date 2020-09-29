import collections
class Solution:
    def findMinHeightTrees(self, n, edges):
        d=collections.defaultdict(set)
        for i,v in edges:
            d[i].add(v)
            d[v].add(i)
        ret=[]
        leaves=[]
        for i in d:
            if len(d[i])==1:
                leaves.append(i)
        while(True):
            next=[]
            for leaf in leaves:
                for neighbour in d[leaf]:
                    d[neighbour].remove(leaf)
                    if len(d[neighbour])==1:
                        next.append(neighbour)
            if len(next)==0:
                return leaves
            leaves=next




sol=Solution()
print(sol.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))