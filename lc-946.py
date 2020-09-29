import collections
class Solution:
    def validateStackSequences(self, pushed, popped):
        popped=collections.deque(popped)
        pu=collections.deque([])
        i=0
        l=len(pushed)
        while(i<l and popped):
            if len(pu)>0:
                if popped[0]==pu[-1]:
                    popped.popleft()
                    pu.pop()
                    continue
            if pushed[i]!=popped[0]:
                pu.append(pushed[i])
                i+=1
                continue
            if pushed[i]==popped[0]:
                popped.popleft()
                pushed.pop(i)
        return len(popped)==0

sol=Solution()
print(sol.validateStackSequences([0,2,1],
[0,1,2]))