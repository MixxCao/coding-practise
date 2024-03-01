#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # solution 1
        # max_height_l = [h for h in height]
        # for i in range(1, len(height)):
        #     max_height_l[i] = max(max_height_l[i-1], max_height_l[i])
            
        # max_height_r = [h for h in height]
        # for i in reversed(range(0, len(height) - 1)):
        #     max_height_r[i] = max(max_height_r[i+1], max_height_r[i])
        
        # res = 0
        # for i in range(len(height)):
        #     res += min(max_height_l[i], max_height_r[i]) - height[i]
        
        # return res
        
        stack = []
        
                
        
        
        
# @lc code=end

