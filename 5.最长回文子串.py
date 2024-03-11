#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in s]
        
        for i in range(len(s)):
            dp[i][i] = True
        result = s[0]
        
        for length in range(len(s)):
            for i in range(len(s)):
                j = i + length + 1
                if j >= len(s):
                    break
                
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = True
                        result = s[i:j+1]
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        result = s[i:j+1] if dp[i][j] else result
                else:
                    dp[i][j] = False
                    
        return result 

        
# @lc code=end

