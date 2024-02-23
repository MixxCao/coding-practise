#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        height = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0:
                    height[i][j] = 1
                else:
                    height[i][j] = height[i-1][j] + 1        
        print(height)
        
        res = 0
        for i in reversed(range(m)):
            res = max(
                res,
                self.max_area(height=height[i])
            )
        
        return res
    

    def max_area(self, height):
        if not height:
            return 0
        
        stack = []
        area = [h for h in height]

        for i in range(len(height)):
            while stack:
                if height[stack[-1]] > height[i]:
                    idx = stack.pop()
                    area[idx] += height[idx] * (i - idx - 1)
                else:
                    break

            stack.append(i)
            
        # print(stack, area)
        while stack:
            idx = stack.pop()
            area[idx] += height[idx] * (len(height) - idx - 1)
        # print(area)
        
        stack = []   
        for i in reversed(range(len(height))):
            while stack:
                if height[stack[-1]] > height[i]:
                    idx = stack.pop()
                    area[idx] += height[idx] * (idx - i - 1)
                else:
                    break

            stack.append(i)
            
        while stack:
            idx = stack.pop()
            area[idx] += height[idx] * idx
            

        return max(area)
                        

# @lc code=end

