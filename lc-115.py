class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def ds(s,t,i,j):
            if i==len(s) or j==len(t):
                return 0
            taken=0
            if s[i]==t[j]:
                taken = ds(s,t,i+1,j+1)+ds(s,t,i+1,j)
                if j==len(t)-1:
                    return 1
            nottaken = ds(s,t,i+1,j)
            return max(taken,nottaken)
                
        return ds(s,t,0,0)
sol=Solution()
print(sol.numDistinct(s = "babgbag", t = "bag"))