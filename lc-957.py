class Solution:
    def prisonAfterNDays(self, cell, N):
        new_cell=[0]*8
        for _ in range(N-1):
            for i in range(1,6):
                new_cell[i]= 0 if cell[i-1]^cell[i+1]==1 else 1
            new_cell[0],new_cell[-1]=0,0
            new_cell,cell=cell,new_cell
        return cell

sol=Solution()
print(sol.prisonAfterNDays(cell = [0,1,0,1,1,0,0,1], N = 7))