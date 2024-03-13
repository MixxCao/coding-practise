#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums) - i - 1] = right[len(nums) - i] * nums[len(nums) - i]
            
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
            
        return result
# @lc code=end

