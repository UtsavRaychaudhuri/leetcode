class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict,deque
        g=defaultdict(list)
        self.visited=[]
        for i in tickets:
            g[i[0]].append(i[1])
        bitmap={}
        for i in g:
            g[i]=sorted(g[i])
            bitmap[i]=[False]*len(g[i])
        def backtrack(graph,i,start,visited):
            if len(visited)==len(tickets)+1:
                self.visited=visited
                return True
            for i,v in enumerate(graph[start]):
                if not bitmap[start][i]:
                    bitmap[start][i]=True
                    ret = backtrack(graph,i,graph[start][i],visited+[v])
                    bitmap[start][i]=False
                    if ret:
                        return self.visited
        return backtrack(g,0,"JFK",["JFK"])
            


        
sol=Solution()
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))

#jfk:[kul,nrt]
#nrt:[jfk]