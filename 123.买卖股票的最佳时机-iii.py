#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# doing
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1e31] * 5 for _ in prices]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], -prices[i])
            
            if i <= 0: 
                continue
            
            dp[i][2] = max(dp[i - 1][2],  dp[i-1][1] + prices[i])
            
            if i <= 1:
                continue  
            
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            
            if i <= 2:
                continue
            
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        
        # for d in dp:  
        #     print(d)
        return max(dp[-1][4], dp[-1][2], 0)
            
        
# @lc code=end

