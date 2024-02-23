#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, r1 = 0, len(nums1) - 1
        l2, r2 = 0, len(nums2) - 1
        l, r = l1 + l2, r1 + r2
        
        mid_idx = (len(nums1) + len(nums2)) // 2
        
        while l < r and l1 < r1 and l2 < r2:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            
            
            
        
# @lc code=end

