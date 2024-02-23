#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        min_gas = 1e31
        idx = -1
        left = 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if min_gas > left:
                idx = i
                min_gas = left

        if idx < 0:
            return -1
        else:
            return (idx + 1)  % len(gas)

        
            
        
# @lc code=end

