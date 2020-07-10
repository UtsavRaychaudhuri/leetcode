class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.exist=False
        for i,v  in enumerate(board):
            for j,k in enumerate(v):
                if k==word[0]:
                    if self.checkifexists(board,word,i,j):
                        return True
        return False
        
    def checkifexists(self,board,word,i,j,count=0):
        if count==len(word):
            self.exist=True
            return True
        if i==len(board) or j==len(board[0]) or i<0 or j<0 or word[count]!=board[i][j]:
            return False
        temp=board[i][j]
        board[i][j]= " "
        found= self.checkifexists(board,word,i,j+1,count+1) or self.checkifexists(board,word,i+1,j,count+1) or self.checkifexists(board,word,i,j-1,count+1) or self.checkifexists(board,word,i-1,j,count+1)
        board[i][j]=temp
        return found
        
        