import collections
import heapq

class Solution:
    def isNStraightHand(self, hand, W):
        d=collections.defaultdict(int)
        for i in hand:
            d[i]+=1
        arr=[]
        l=sorted(d)
        i=0
        j=1
        for _ in range(W-1):
            if d[l]






            


        
sol=Solution()
sol.isNStraightHand([1,2,3,6,2,3,4,7,8],
3)
