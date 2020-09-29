import collections

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        d=collections.defaultdict(int)
        i=res=0
        for j in range(len(tree)):
            d[tree[j]]+=1
            while(len(d)>2):
                d[tree[i]]-=1
                if d[tree[i]]==0:
                    del d[tree[i]]
                i+=1
            res=max(res,j-i+1)
        return res

sol=Solution()
sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])