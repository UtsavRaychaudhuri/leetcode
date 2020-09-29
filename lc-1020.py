import collections

class Solution:
    def numEnclaves(self, A):
        def dfs(A,i,j):
            q=collections.deque([[i,j]])
            while(q):
                i,j=q.popleft()
                A[i][j]=0
                if i+1<len(A):
                    if A[i+1][j]==1:
                        A[i+1][j]==0
                        q.append([i+1,j])
                if i-1>=0:
                    if A[i-1][j]==1:
                        A[i-1][j]=1
                        q.append([i-1,j])
                if j+1<len(A[0]):
                    if A[i][j+1]==1:
                        A[i][j+1]=0
                        q.append([i,j+1])
                if j-1>=0:
                    if A[i][j-1]==1:
                        A[i][j-1]=0
                        q.append([i,j-1])
        for i in range(len(A)):
            if A[i][0]==1:
                dfs(A,i,0)
            if A[i][len(A[0])-1]==1:
                dfs(A,i,len(A[0])-1)
        for j in range(len(A[0])):
            if A[0][j]==1:
                dfs(A,0,j)
            if A[len(A)-1][j]==1:
                dfs(A,len(A)-1,j)
        res=0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    res+=1
        return res

        
sol=Solution()
sol.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]])