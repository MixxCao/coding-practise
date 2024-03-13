#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start

from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        voc = defaultdict(int)
        
        for s in secret:
            voc[s] += 1
            
        bulls, cows = 0, 0
        
        for g in guess:
            if voc[g] > 0:
                cows += 1
                voc[g] -= 1
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls +=1
                cows -= 1
                
        return f'{bulls}A{cows}B'
        
# @lc code=end

