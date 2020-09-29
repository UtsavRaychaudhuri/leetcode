class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def mcs(word1,word2,i,j):
            if i==len(word1) or j==len(word2):
                return 0
            taken=0
            if word1[i]==word2[j]:
                taken=1+mcs(word1,word2,i+1,j+1)
            notaken=max(mcs(word1,word2,i+1,j),mcs(word1,word2,i,j+1))
            return max(taken,notaken)
        l=mcs(word1,word2,0,0)
        print(l)
        return max(len(word1),len(word2))-mcs(word1,word2,0,0)

sol=Solution()
sol.minDistance("horse","ros")