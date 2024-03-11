#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        dp = [1e5] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = min(prices[i-1], dp[i-1])
            # print(dp)
            res = max(prices[i] - dp[i], res)
        # print(dp)
        
        return res            
        

# @lc code=end

