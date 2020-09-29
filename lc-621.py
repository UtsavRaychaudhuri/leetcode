import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import heapq
        if n==0:
            return len(tasks)
        d=collections.defaultdict(int)
        for i in tasks:
            d[i]+=1
        cur=[]
        for i in d:
            cur.append([-d[i],i])
        new=[]
        heapq.heapify(cur)
        heapq.heapify(new)
        res=[]
        while(cur):
            for i in range(n+1):
                if len(new)==0 and len(cur)==0:
                    break
                if len(cur)==0:
                    res.append("")
                    continue
                ele=heapq.heappop(cur)
                if ele[0]<-1:
                    ele[0]+=1
                    heapq.heappush(new,ele)
                res.append(ele[1])
            if len(cur)==0:
                new,cur=cur,new
                continue
            for i in new:
                heapq.heappush(cur,i)
            new=[]
        return len(res)
        
            
sol=Solution()
sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)