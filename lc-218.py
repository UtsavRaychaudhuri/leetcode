class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        l=[]
        for i in buildings:
            l.append([i[0],i[2]])
            l.append([i[1],i[2]])
        l.sort()
        s=[l[0].copy()]
        for i in range(1,len(l)-1):
            if s[-1][0]==l[i][0]:
                s[-1][1]=max(s[-1][1],l[i][1])
                continue
            if l[i-1][1]>l[i][1]<l[i+1][1]:
                continue
            s.append(l[i])
        if s[-1][0]==l[-1][0] and s[-1][1]<l[-1][1]:
            s[-1][1]=l[-1][1]
        else:
            s.append(l[-1])
        ans=[s[0]]
        for i in range(1,len(s)-1):
            if s[i][1]!=ans[-1][1]:
                ans.append(s[i])
            else:
                ans.append([s[i][0],s[i+1][1]])
                s[i+1][1]=0
        if s[-1][1]==ans[-1][1]:
            ans.append([s[-1][0],0])
        else:
            ans.append(s[-1])
        return ans


sol=Solution()
print(sol.getSkyline([[1,2,1],[2147483646,2147483647,2147483647]]))