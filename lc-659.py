from collections import _heapq as heapq
class Solution:
    def isPossible(self, nums):
        l=[[-nums[0]]]
        unbalanced=set([0])
        for i in nums[1:]:
            pushub,pushb=False,False
            for j in unbalanced:
                if l[j][0]!=-i and l[j][0]==-i+1:
                    heapq.heappush(l[j],-i)
                    pushub=True
                    if len(l[j])==3:
                        unbalanced.remove(j)
                    break
            if not pushub:
                for j in l:
                    if j[0]!=-i and j[0]==-i+1:
                        pushb=True
                        heapq.heappush(j,-i)
                        if len(j)==3:
                            unbalanced.remove(j)
                        break
            if not (pushb or pushub):
                l.append([-i])
                unbalanced.add(len(l)-1)
        return True if len(unbalanced)==0 else False
                    
sol=Solution()
print(sol.isPossible([1,2,5,5,6,6,7,8,8,9]))