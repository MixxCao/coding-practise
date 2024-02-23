#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
def comparing(x : str, y : str):
    return int(x+y) -  int(y+x)

import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        x = [str(n) for n in nums]
        x.sort(key = functools.cmp_to_key(comparing), reverse=True)
        res = ''.join(x)
        while res[0] == '0' and len(res) > 1:
            res = res[1:]
        
        return res

# @lc code=end

