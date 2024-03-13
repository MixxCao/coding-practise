#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        b = 0 # int32
        
        for x in nums:
            xb = 1 << x
            if xb & b > 0:
                return x
            
            b = b | xb
            
    
# @lc code=end

