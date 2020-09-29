class Solution:
    def isBipartite(self, graph):
        color={0:'R'}
        stack=[0]
        seen=set()
        unseen=set()
        for i in graph:
            unseen = unseen.union(i)
        while(stack):
            ele=stack.pop()
            seen.add(ele)
            for i in graph[ele]:
                if i not in seen:
                    if i in color:
                        if color[ele]==color[i]:
                            return False
                    color[i]='R' if color[ele]=='B' else 'B'
                    stack.append(i)
        return len(seen)==len(unseen)
sol=Solution()
print(sol.isBipartite([[4],[],[4],[4],[0,2,3]]))