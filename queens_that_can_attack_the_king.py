class Solution(object):
    def __init__(self):
        self.outarray=[]
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """ 
        self.checkleft(king,queens)
        self.checkup(king,queens)
        self.checkdown(king,queens)
        self.checkright(king,queens)
        self.checkdiagonal(king,queens)
        return self.outarray
        
    def checkleft(self,king,queens):
        j=king[1]
        for i in range(king[0],-1,-1):
            if [i,j] in queens:
                self.outarray.append([i,j])
                break
    
    def checkright(self,king,queens):
        i=king[0]
        for j in range(king[1],10):
            if [i,j] in queens:
                self.outarray.append([i,j])
                break
    
    def checkup(self,king,queens):
        j=king[1]
        for i in range(king[0],10):
            if [i,j] in queens:
                self.outarray.append([i,j])
                break
    
    def checkdown(self,king,queens):
        i=king[0]
        for j in range(king[1],-1,-1):
            if [i,j] in queens:
                self.outarray.append([i,j])
                break
    
    def checkdiagonal(self,king,queens):
        i=king[0]
        j=king[1]
        while(i>=0 and j>=0):
            if [i,j] in queens and [i,j] not in self.outarray:
                self.outarray.append([i,j])
                break
            i-=1
            j-=1
        i,j=king[0],king[1]
        while(i<=9 and j<=9):
            if [i,j] in queens and [i,j] not in self.outarray:
                self.outarray.append([i,j])
                break
            i+=1
            j+=1
        i,j=king[0],king[1]
        while(j>=0 and i<=9):
            if [i,j] in queens and [i,j] not in self.outarray:
                self.outarray.append([i,j])
                break
            i+=1
            j-=1
        i,j=king[0],king[1]
        while(i>=0 and j<=9):
            if [i,j] in queens and [i,j] not in self.outarray:
                self.outarray.append([i,j])
                break
            j+=1
            i-=1
sol=Solution()
print(sol.queensAttacktheKing([[7,3],[6,6],[3,0],[5,6],[0,2],[7,7],[2,1],[0,7],[1,6],[5,1],[2,5],[0,3],[3,7],[4,0],[6,7],[5,5],[3,3],[7,6],[6,3],[1,5],[3,6],[2,2],[0,4],[3,4],[5,0],[0,0],[7,1],[4,5],[1,4],[7,5],[4,2],[3,1],[7,4],[4,3],[1,7],[5,2]],[2,4]))