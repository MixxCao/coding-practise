#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0
        m, n = len(board), len(board[0])
        color = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[idx]:
                    color[i][j] = 1
                    
                    for d in range(4):
                        if self.dfs(board, word, m, n, i, j, d, idx + 1, color):
                            return True
                    
                    color[i][j] = 0
        else:
            return False
                    
                    
    def dfs(self, board, word, m, n, i, j, direction, idx, color):
        if idx >= len(word):
            return True
        # print(i,j)
        if direction == 0:
            i, j = i, j + 1
        elif direction == 1:
            i, j = i + 1, j
        elif direction == 2:
            i, j = i, j - 1
        else:
            i, j = i - 1, j
            
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        if color[i][j] == 1:
            return False
        
        if word[idx] != board[i][j]:
            return False
        
        color[i][j] = 1
        for d in range(4):
            if self.dfs(board, word, m, n, i, j, d, idx + 1, color):
                return True
            
        color[i][j] = 0
        
        return False
# @lc code=end

