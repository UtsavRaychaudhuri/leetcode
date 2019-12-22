# float('inf')  -1  0  float('inf')
# float('inf') float('inf') float('inf')  -1
# float('inf')  -1 float('inf')  -1
#   0  -1 float('inf') float('inf')

# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Approach:- Find the 0 value or the gate in the array and then apply dfs from there everywhere

def dfs(i,j,count,a):
    if i<0 or i>=len(a) or j>=len(a[i]) or j<0 or a[i][j]<count or a[i][j]==-1:
        return
    else:
        a[i][j]=count
    dfs(i+1,j,count+1,a)
    dfs(i-1,j,count+1,a)
    dfs(i,j+1,count+1,a)
    dfs(i,j-1,count+1,a)

a=[[float('inf'),-1,0,float('inf')],[float('inf'),float('inf'),float('inf'),-1],[float('inf'),-1,float('inf'),-1],[0,-1,float('inf'),float('inf')]]
for i,k in enumerate(a):
    for j,v in enumerate(k):
        if v==0:
            dfs(i,j,0,a)
print(a)