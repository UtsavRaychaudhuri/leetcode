import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d=collections.defaultdict(set)
        letters=set()
        for i in words:
            for j in i:
                letters.add(j)
        for i in range(1,len(words)):
            for j in range(len(words[i])):
                if words[i-1][j]==words[i][j]:
                           continue
                d[words[i-1][j]]=words[i][j]
                break
        for i in words[0]:
            if i in d:
                start=i
                break
        q=collections.deque([start])
        res=""
        seen=set()
        while(q):
            ele=q.popleft()
            if ele in seen:
                return ""
            res+=ele
            seen.add(ele)
            for i in d[ele]:
                q.append(i)
        for i in letters:
            if i not in seen:
                res+=i
        return res
            
sol=Solution()
sol.alienOrder(
  [
  "z",
  "x",
  "z"
]
)