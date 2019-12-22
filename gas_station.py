class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cango=False
        if sum(gas)-sum(cost)==0:
            cango=True
        if cango==False:
            return -1
        my_gas_cost=[]
        for j in range(len(gas)):
            my_gas_cost.append(gas[j]-cost[j])
        sums=0
        i=0
        foundit=True
        for i,v in enumerate(my_gas_cost):
            k=i
            if v>0:
                sums+=v
                j=k
                k+=1
                while(k!=j):
                    if j==len(my_gas_cost):
                        j=0
                    sums+=my_gas_cost[j]
                    if sums<0:
                        foundit=False
                        break
                if foundit:
                    return k
        return i

sol=Solution()
sol.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1])