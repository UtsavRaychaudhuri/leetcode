import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l=[[-a,"a"],[-b,"b"],[-c,"c"]]
        heapq.heapify(l)
        str=""
        while(l):
            char=heapq.heappop(l)
            if -char[0]>=2:
                str+=char[1]*2
                if len(l)==0:
                    break
                char1=heapq.heappop()
                str+=char1[1]
                if char1[1]+1<0:
                    char1[0]+=1
                    heapq.heappush(char1)
                if -char[0]-2>2:
                    char[0]+=2
                    heapq.heappush(char)

sol=Solution()
sol.longestDiverseString(a = 7, b = 1, c = 0)