import collections
import heapq
class Solution:
    def networkDelayTime(self, times, N, K): 
        g=collections.defaultdict(dict)
        for i,v,w in times:
            g[i][v]=w
        s=set()
        s.add(K)
        d=[]
        heapq.heappush(d,(0,K))
        total=[]
        while(d):
            weight,node=heapq.heappop(d)
            s.add(node)
            for key,val in g[node].items():
                if key not in s:
                    total.append(weight)
                    heapq.heappush(d,(weight+val,key))
        if len(s)==N:
            return max(total)
        return -1
        
                
sol=Solution()
sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2)