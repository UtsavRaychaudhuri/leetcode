class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.d=[]
        for i in range(len(s1)+1):
            self.d.append([-1]*len(s2))
        def mds(s1,s2,i,j):
            if i==len(s1) or j==len(s2):
                return 0
            taken=0
            if self.d[i][j]==-1:
                if s1[i]==s2[j]:
                    taken=ord(s1[i])+mds(s1,s2,i+1,j+1)
                notaken=max(mds(s1,s2,i+1,j),mds(s1,s2,i,j+1))
                self.d[i][j] = max(taken,notaken)
                return self.d[i][j]
            return self.d[i][j]
        s=sum(ord(i) for i in s1)+sum(ord(i) for i in s2)
        return s-(mds(s1,s2,0,0)*2)

sol=Solution()
print(sol.minimumDeleteSum(s1 = "delete", s2 = "leet"))