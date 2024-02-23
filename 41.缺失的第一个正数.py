#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 0
        size = len(nums)
        for n in nums:
            if n > 0 and n <= size:
                res = res | (1 << (n))
        
        for i in range(1, size + 1):
            if (res & 1 << i) == 0:
                return i
        return size + 1
                
                
                
# @lc code=end

