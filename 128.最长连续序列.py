#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        res = 1
        
        while len(nums) > 0:
            n = nums.pop()
            cnt = 0
            nums.add(n)
            if n - 1 in nums:
                continue
            
            while True:
                
                cnt += 1
                nums.remove(n)
                if n+1 not in nums:
                    res = max(cnt, res)
                    break
                else:
                    n = n + 1
                    
        
        return res 
        
        
# @lc code=end

