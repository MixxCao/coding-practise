#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations) == 1:
        #     if citations[0] == 1:
        #         return citations[0]
        #     else:
        #         return 0
        result = 0
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] >= (i + 1):
                result = i + 1
        return result
        
# @lc code=end

