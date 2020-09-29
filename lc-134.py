class Solution:
    def canCompleteCircuit(self, gas, cost):
        l=[]
        for i in range(len(gas)):
            l.append(gas[i]-cost[i])
        for i in range(len(l)):
            if l[i]>=0:
                sum=0
                for j in list(range(i,len(l)))+ list(range(i)):
                    ret=True
                    sum+=l[j]
                    if sum<0:
                        ret=False
                        break
                if ret:
                    return i
        return -1

sol=Solution()
print(sol.canCompleteCircuit([2],[2]))