#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in prices]
        
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(
                dp[i-1][0],
                dp[i-1][1] + prices[i]
            )
            dp[i][1] = max(
                dp[i-1][1],
                dp[i-1][0] - prices[i]
            )
            
        return dp[-1][0]
# @lc code=end

