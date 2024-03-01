#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        roadmap = set()
        
        height, width = len(grid), len(grid[0])
        res = 0
        for i in range(height):
            for j in range(width):
                idx = i * width + j
                if idx in roadmap: 
                    continue
                if grid[i][j] == '1':
                    res += 1
                    self.__dfs(grid, width, height, i, j, roadmap)
                    
                    
        return res
    
    
    def __dfs(self, grid, width, height, i, j, roadmap):

        if i >= height or i < 0 or j >= width or j < 0:
            return
        
        if grid[i][j] == '0':
            return
        
        idx = i * width + j
        if idx in roadmap:
            return
        
        roadmap.add(idx)
        
        self.__dfs(grid, width, height, i + 1, j, roadmap)
        self.__dfs(grid, width, height, i - 1, j, roadmap)
        self.__dfs(grid, width, height, i, j + 1, roadmap)
        self.__dfs(grid, width, height, i, j - 1, roadmap)
        
        
# @lc code=end

