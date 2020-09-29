import collections

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        from itertools import combinations
        matches=sorted(zip(timestamp,username,website))
        d=collections.defaultdict(list)
        e=collections.defaultdict(int)
        for t,u,w in matches:
            d[u].append(w)
        for i in d.values():
            for s in set(combinations(i,3)):
                e[s]+=1
        a= sorted(e.items(),key=lambda kv: [-kv[1],kv[0]])[0][0]
        return list(a)

        

            
sol=Solution()
print(sol.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]))