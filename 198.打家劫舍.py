#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        res = 0
        for i in range(2, len(nums)):
            dp[i + 1] = max(dp[i], dp[i-1] + nums[i], dp[i-2]+nums[i])
            res = max(res, dp[i+1])
        return res
# @lc code=end

