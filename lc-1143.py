class Solution:
    def longestCommonSubsequence(self, text1, text2):
        self.memo=[]
        for i in range(len(text1)):
            self.memo.append([-1]*len(text2))
        def lcs(text1,text2,n,m):
            if n==-1 or m==-1:
                return 0
            if self.memo[n][m]==-1:
                if text1[n]==text2[m]:
                    self.memo[n][m] = 1+lcs(text1,text2,n-1,m-1)
                    return self.memo[n][m]
                self.memo[n][m] = max(lcs(text1,text2,n-1,m),lcs(text1,text2,n,m-1))
                return self.memo[n][m]
            return self.memo[n][m]
        return lcs(text1,text2,len(text1)-1,len(text2)-1)

sol=Solution()
print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))