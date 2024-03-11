#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = 2 * k + 1
        
        profit = [-1e31] * size
        profit[0] = 0
        profit[1] = - prices[0]
        result = 0
        for i in range(1, len(prices)):
            print(i, profit)
            for k in range(1, size):
                if k > i + 1:
                    continue
                
                if k % 2 == 1:
                    # buy
                    profit[k] = max(profit[k-1] - prices[i], profit[k])
                else:
                    # sell
                    profit[k] = max(profit[k-1] + prices[i], profit[k])
                    result = max(result, profit[k])
        # print(profit)              
        return result
        
# @lc code=end

