#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import *
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])
        path = []
        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(i, 0, m, n, board, path)
            if board[i][n-1] == 'O':
                self.bfs(i, n-1, m, n, board, path)
        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(0, j, m, n, board, path)
            if board[m-1][j] == 'O':
                self.bfs(m-1, j, m, n, board, path)
        
        print(path)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i * n + j in path:
                        continue
                    
                    # print(i * n + j, i, j)
                    board[i][j] = 'X'
                    
                
                
    def bfs(self, i, j, m, n, board, path) -> bool:
        if board[i][j] == 'X':
            return
        
        path.append(i * n + j)

        for direction in range(4):
            if direction == 0:
                new_i, new_j = i - 1, j
            elif direction == 1:
                new_i, new_j = i + 1, j
            elif direction == 2:
                new_i, new_j = i, j - 1
            else:
                new_i, new_j = i, j + 1
            
            if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
               continue 
            if new_i * n + new_j in path:
                continue
            self.bfs(new_i, new_j, m, n, board, path)

   
        
# @lc code=end

