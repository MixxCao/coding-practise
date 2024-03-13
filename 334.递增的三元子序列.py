#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
# [1,6,2,5,1]
# [2,4,-2,-3]
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_from_left, max_from_right = nums[0], nums[-1]
        is_any_less_from_left = 0
        for i in range(1, len(nums)):
            if nums[i] > min_from_left:
                is_any_less_from_left = is_any_less_from_left | ( 1 << i )
            min_from_left = min(min_from_left, nums[i])
            
        print(bin(is_any_less_from_left))
        
        for i in reversed(range(len(nums) - 1)):
            print(i, nums[i], max_from_right)
            if nums[i] < max_from_right:
                if (1 << i) & is_any_less_from_left:
                    return True
            max_from_right = max(max_from_right, nums[i])
                
        return False
            
            
        
        
# @lc code=end

