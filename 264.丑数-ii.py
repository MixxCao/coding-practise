#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * (n)
        
        pointer = [0, 0, 0]
        i = 1
        while i < n:
            # print(dp)
            c2, c3, c5 = dp[pointer[0]] * 2, dp[pointer[1]] * 3, dp[pointer[2]] * 5
            dp[i] = min(c2, c3, c5)
            
            if dp[i] == c2:
                pointer[0] += 1
            elif dp[i] == c3: 
                pointer[1] += 1
            else:
                pointer[2] += 1
                
            if dp[i] not in dp[:i]:
                i += 1
            else:
                continue
                
            
        
        # print(dp) 
        return dp[-1]
            
# @lc code=end

