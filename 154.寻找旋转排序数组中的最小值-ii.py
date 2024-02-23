#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        while nums[0] == nums[-1]:
            if len(nums) == 1:
                return nums[0]
            nums.pop()
        
        if nums[0] <= nums[-1]:
            return nums[0]
            
        
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if left == mid:
                return min(nums[left], nums[right])
            
            if nums[mid] >= nums[0]:
                left = mid + 1
                res = left
            else:
                right = mid
                res = right
                
        return nums[res]
            
                
# @lc code=end

