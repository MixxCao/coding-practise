#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        
        for i in range(len(nums) * 2):
            # real_i = i % len(nums)   
            while stack:
                if nums[stack[-1] % len(nums)] < nums[i % len(nums)]:
                    idx = stack.pop()
                    
                    if idx < len(nums):
                        result[idx] = nums[i % len(nums)]
                else:
                    break
            stack.append(i)
            
        return result
         
# @lc code=end

