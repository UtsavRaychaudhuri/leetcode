class Solution:
    def frequencySort(self, s: str) -> str:
        d=dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=""
        for i,_ in sorted(d.items(),key=lambda k: k[1],reverse=True):
            ans+=i*d[i]
        return ans

sol=Solution()
print(sol.frequencySort("Aabb"))