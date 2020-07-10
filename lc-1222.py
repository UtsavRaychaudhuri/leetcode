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
    
        
        
            
        
            
        