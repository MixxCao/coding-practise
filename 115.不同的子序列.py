#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if s[0] == t[0] else 0 
        for i in range(m):
            for j in range(n):
                if j > i: continue
                if i == 0 and j == 0: continue
                
                if j == 0:
                    if s[i] == t[j]:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = dp[i-1][j]
                    
                    continue
                
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                
                    
                
        
        
        
        return dp[-1][-1]
# @lc code=end

