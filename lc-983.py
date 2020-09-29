class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        def mct(days,i):
            if i>=len(days):
                return 0
            ondp=costs[0]+mct(days,i+1)
            self.si=i
            for j in range(i,len(days)):
                if days[i]<days[self.si]+7:
                    pass
                else:
                    break
            wdp=costs[1]+mct(days,i)
            self.si=i
            for j in range(i,len(days)):
                if days[i]<days[self.si]+30:
                    pass
                else:
                    break
            mdp=costs[2]+mct(days,i)
            return min(ondp,wdp,mdp)

        def findindex(days,indextostart,day):
            for i in range(indextostart,len(days)):
                if days[i]>=day:
                    return i-1
            return i

        return mct(days,0)

sol=Solution()
print(sol.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))