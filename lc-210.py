import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        d=collections.defaultdict(list)
        for i in prerequisites:
            d[i[1]].append(i[0])
        self.seen=set()
        self.topo=collections.deque()
        def dfs(i,d,seen):
            if i in seen:
                return True
            seen.add(i)
            for j in range(len(d[i])):
                if d[i][j] in d and d[i][j] not in self.seen:
                    ret = dfs(d[i][j],d,seen)
                    if ret is not None:
                        return True
                if d[i][j] not in self.seen:
                    self.seen.add(d[i][j])
                    self.topo.appendleft(d[i][j])
        for i in d:
            if i not in self.seen:
                if dfs(i,d,set()) is not None:
                    return []
                self.topo.appendleft(i)
                self.seen.add(i)
        return self.topo

    

sol=Solution()
sol.canFinish(6, [[2,1],[3,2],[1,4],[5,4],[4,6],[5,6]])