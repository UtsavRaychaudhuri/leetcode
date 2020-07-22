from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.root={}
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(board_copy,i,j,current):
            if i==len(board_copy) or j==len(board_copy[0]) or i<0 or j<0:
                self.word=self.word[:-1]
                return
            if board_copy[i][j]=="":
                self.word=self.word[:-1]
                return
            if board_copy[i][j] not in current:
                self.word=self.word[:-1]
                return
            current=current[board_copy[i][j]]
            self.word+=board[i][j]
            board_copy[i][j]=""
            if self.word in self.my_set:
                self.words.add(self.word)
            dfs(board_copy,i+1,j,current)
            dfs(board_copy,i,j+1,current)
            dfs(board_copy,i-1,j,current)
            dfs(board_copy,i,j-1,current)
        current=self.root
        for i in words:
            current=self.root
            for j in i:
                if j not in current:
                    current[j]={}
                current=current[j]
        board_copy=deepcopy(board)
        self.word=""
        self.words=set()
        self.my_set=set(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board_copy[i][j] in self.root:
                    self.word=""
                    dfs(board_copy,i,j,self.root)
                    board_copy=deepcopy(board)
        return list(self.words)

sol=Solution()
sol.findWords([["a","b"],["c","d"]],
["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"])





        
        