#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    if matrix[i][j] == "1":
                        dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
                    else:
                        matrix[i][j] = 0
                res = max(res, dp[i][j])
        # for d in dp:
        #     print(d) 
        return res ** 2

# @lc code=end

