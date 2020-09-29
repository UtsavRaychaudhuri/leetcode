class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        d=defaultdict(dict)
        def dfs(d,i,j,sum,seen):
            seen.add(i)
            if i!=self.start:
                if i not in d[self.start]:
                    d[self.start][i]=sum
                    d[i][self.start]=1/sum
            if j in d[i]:
                self.sum=sum*d[i][j]
                return True
            for k in list(d[i]):
                if k not in seen:
                    ret = dfs(d,k,j,sum*d[i][k],seen)
                    if ret is not None:
                        return True
        k=0
        for i in equations:
            a,b=i[0],i[1]
            d[a][b]=values[k]
            d[b][a]=1/values[k]
            k+=1
        self.ret=[]
        for i in queries:
            if i[0] not in d or i[1] not in d:
                self.ret.append(-1)
            else:
                self.start=i[0]
                if dfs(d,i[0],i[1],1,set()) is not None:
                    self.ret.append(self.sum)
                else:
                    self.ret.append(-1)
        return self.ret
sol=Solution()
sol.calcEquation(
[["a","b"],["e","f"],["b","e"],["g","h"]],
[3.4,1.4,2.3,1.5],
[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"],["a","g"]]
)
