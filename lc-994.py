from collections import deque
class Solution:
    def orangesRotting(self, grid):
        que=deque()
        fresh_oranges=0
        minutes=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    que.append((i,j))
                elif grid[i][j]==1:
                    fresh_oranges+=1
        que.append((-1,-1))
        if fresh_oranges==0:
            return 0
        while(que):
            if que[0][0]==-1:
                minutes+=1
                que.popleft()
                que.append((-1,-1))
                if len(que)==1:
                    break
            i,j=que[0][0],que[0][1]
            if i+1<len(grid):
                if grid[i+1][j]==1:
                    grid[i+1][j]=2
                    fresh_oranges-=1
                    que.append((i+1,j))
            if i-1>=0:
                if grid[i-1][j]==1:
                    grid[i-1][j]=2
                    fresh_oranges-=1
                    que.append((i-1,j))
            if j+1<len(grid[0]):
                if grid[i][j+1]==1:
                    grid[i][j+1]=2
                    fresh_oranges-=1
                    que.append((i,j+1))
            if j-1>=0:
                if grid[i][j-1]==1:
                    grid[i][j-1]=2
                    fresh_oranges-=1
                    que.append((i,j-1))
            que.popleft()
            if fresh_oranges<=0:
                return minutes+1
        return minutes if fresh_oranges<=0 else -1




            
sol=Solution()
sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
        
        