#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = [h for h in heights]
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] > heights[i]:
                    idx = stack.pop(-1)
                    area[idx] += (i - idx - 1) * heights[idx]
                else:
                    break
            stack.append(i)
        # print(stack, area)
        while stack:
            idx = stack.pop()
            area[idx] += (len(heights) - idx - 1) * heights[idx]
        
        # print(area)
         
        stack = []
        for i in reversed(range(len(heights))):
            while stack:
                if heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    area[idx] += (idx-i-1) * heights[idx]
                else:
                    break
            stack.append(i)
        while stack:
            idx = stack.pop()
            area[idx] += (idx) * heights[idx]
        # print(area)
        return max(area)
            
# @lc code=end

