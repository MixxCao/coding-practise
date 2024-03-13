#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, len(matrix[0]) - 1
        
        while i >= 0 and j >= 0:
            # print(i, j)
            if matrix[i][j] == target:
                return True
            
            if matrix[i][0] > target:
                i -= 1
                continue
            
            if matrix[i][j] > target:
                j -= 1
            else:
                i -= 1
                j = len(matrix[0]) - 1
                
        return False
        
# @lc code=end

