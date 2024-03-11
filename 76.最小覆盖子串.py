#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        
        dictionary = defaultdict(int)
        count = defaultdict(int)
        
        for x in t:
            dictionary[x] += 1
            
        min_length = len(s) + 1
        res = ''
        
        while left < len(s):
            while s[left] not in t:
                left += 1
                if left >= len(s):
                    return res
            right = max(left, right)
                
            for key, cnt in dictionary.items():
                while count[key] < cnt and right < len(s):
                    count[s[right]] +=1
                    right += 1

                if right >= len(s) and count[key] < cnt:
                    return res
            
            if right - left < min_length:
                res = s[left:right]
                min_length = right - left

            count[s[left]] -= 1  
            left += 1
        return res
            
        
               
                
# @lc code=end

