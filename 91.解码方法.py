#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if i == 0:
                if s[i] == '0':
                    return 0
                else:
                    dp[i + 1] = 1
                continue
                    
                    
            if s[i] != '0':
                x = int(s[i-1:i+1])
                if x <= 26 and x > 10:
                    dp[i+1] = dp[i-1] + dp[i]
                else:
                    dp[i+1] = dp[i]
            else:
                x = int(s[i-1:i+1])
                if x == 10 or x == 20:
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            
        return dp[-1]
        
# @lc code=end

