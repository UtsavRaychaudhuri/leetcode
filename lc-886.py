import collections
class Solution:
    def possibleBipartition(self, N, dislikes):
        d=collections.defaultdict(list)
        for i in dislikes:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        seen=set()
        q=collections.deque()
        for i in d:
            if i not in seen:
                col={i:'r'}
                q.append(i)
                seen.add(i)
                while(q):
                    ele=q.popleft()
                    for i in d[ele]:
                        if i in col:
                            if col[ele]==col[i]:
                                return False
                        col[i]='r' if col[ele]=='b' else 'b'
                        if i not in seen:
                            q.append(i)
                            seen.add(i)
        return True

sol=Solution()
sol.possibleBipartition(5,
[[1,2],[3,4],[4,5],[3,5]])