import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        board_copy=copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                pop=0
                if i+1<len(board):
                    pop+=board[i+1][j]
                    if j+1<len(board[0]):
                        pop+=board[i+1][j+1]
                    if j-1>=0:
                        pop+=board[i+1][j-1]
                if j+1<len(board[0]):
                    pop+=board[i][j+1]
                if i-1>=0:
                    pop+=board[i-1][j]
                    if j-1>=0:
                        pop+=board[i-1][j-1]
                    if j+1<len(board[0]):
                        pop+=board[i-1][j+1]
                if j-1>=0:
                    pop+=board[i][j-1]
                if board[i][j]==0 and pop==3:
                    board_copy[i][j]=1
                if board[i][j]==1:
                    if pop<2:
                        board_copy[i][j]=0
                    if pop>3:
                        board_copy[i][j]=0
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board_copy[i][j]
                
                    
                
        