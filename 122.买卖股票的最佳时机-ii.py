#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = [0]
        dp1 = [-prices[0]]
        
        for i in range(1, len(prices)):
            dp0.append(
                max(dp0[-1], dp1[-1] + prices[i])
            )
            dp1.append(
                max(dp0[-1] - prices[i], dp1[-1])
            )
            
        return dp0[-1]
# @lc code=end

