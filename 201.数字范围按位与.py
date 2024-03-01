#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0

        for i in range(32):
            _l = left >> i
            _r = right >> i
            
            if _l == _r: 
                return _l << i
            elif _l == 0 or _r == 0:
                return 0
                
        return 0
        
        
# @lc code=end

