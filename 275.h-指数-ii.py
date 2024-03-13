#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        # if len(citations) == 1:
        #     if citations[0] >= 1:
        #         return 1
        #     else:
        #         return 0
        
        while left < right:
            
            mid = (left + right) // 2
            # print(left, mid, right, citations[mid], len(citations) - mid)
            if citations[mid] >= len(citations) - mid:
                right = mid
            else:
                left = mid + 1
                
        return len(citations) - left
# @lc code=end

