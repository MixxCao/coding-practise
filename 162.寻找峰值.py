#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid-1]:
                left = mid
            else:
                right = mid
                
        return left
# @lc code=end

