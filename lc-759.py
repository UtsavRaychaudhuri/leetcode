class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        l=[]
        for j in schedule:
            for i in j:
                l.append([i[0],i[1]])
        l.sort()
        cur=l[0]
        ans=[]
        for i in range(1,len(l)):
            if l[i][0]<=cur[1]:
                cur[1]=max(cur[1],l[i][1])
            else:
                ans.append([cur[1],l[i][0]])
                cur=l[i]
        print(ans)

sol=Solution()
sol.employeeFreeTime([[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]])