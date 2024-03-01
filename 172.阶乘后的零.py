#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        res = 0
        for i in range(5, n + 1, 5):
            to_be_added = 0
            while i > 0 and i % 5 == 0:
                i = i // 5
                to_be_added += 1
                
            res += to_be_added
        return res
        
# @lc code=end

