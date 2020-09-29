class Solution:
    def hasValidPath(self, matrix):
        self.i,self.j=0,0
        def vp(matrix):
            i,j=self.i,self.j
            prev=""
            seen=set()
            d={1:"LR",2:"UD",3:"LD",4:"DR",5:"LU",6:"UR"}
            while(i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0])):
                if (i,j) in seen:
                    return False
                if prev!="":
                    search=matrix[i][j]
                    if d[matrix[i][j]][0]=="U" and prev[1]!="D":
                        return False
                    elif d[matrix[i][j]][0]=="L" and prev[1]!="R":
                        return False
                    if d[matrix[i][j]][0]=="D" and prev[1]!="U":
                        return False
                    if d[matrix[i][j]][0]=="R" and prev[1]!="L":
                        return False
                if i==len(matrix)-1 and j==len(matrix[0])-1:
                    return True
                seen.add((i,j))
                prev=d[matrix[i][j]]
                if matrix[i][j]==1:
                    j+=1
                elif matrix[i][j]==2:
                    i+=1
                elif matrix[i][j]==3:
                    i+=1
                elif matrix[i][j]==4:
                    j+=1
                elif matrix[i][j]==5:
                    i-=1
                elif matrix[i][j]==6:
                    j+=1
            return False
        if matrix[0][0]==4:
            self.i=1
            ret1=vp(matrix)
            self.i,self.j=0,1
            re2=vp(matrix)
            return ret1 or re2
        else:
            return vp(matrix)

        

sol=Solution()
print(sol.hasValidPath(matrix = [[4,1],[6,1]]))

