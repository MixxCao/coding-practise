#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    cache = {}
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        
        res = 0
        
        for i in range(n):
            left, right = self.numTrees(i), self.numTrees(n-i-1)
            add_to_res = max(left, 1) * max(right, 1)
            res += add_to_res

        self.cache[n] = res      
            
        return res
        
# @lc code=end

