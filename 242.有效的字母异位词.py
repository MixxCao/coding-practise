#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        voc = defaultdict(int)
        
        for s1, s2 in zip(s, t):
            voc[s1] +=1
            voc[s2] -=1
        
        for _, v in voc.items():
            if v != 0:
                return False
            
        return True 
        
# @lc code=end

