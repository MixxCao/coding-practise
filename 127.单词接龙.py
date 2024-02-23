#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        round = self.bfs(beginWord, endWord, wordList, 0)
        
        return round
        
        
    def bfs(self, word, endWord, wordList, round):
        if is_one_word_trans(word, endWord):
            return round + 1
        
        flag = False
        for candidate in wordList:
            if 
            
            
        if not flag:
            return 0
            
        
    
    def is_one_word_trans(self, x, y):
        flag = False
        for _x, _y in zip(x, y):
            if _x != _y:
                if flag:
                    return False
                else:
                    flag = True
# @lc code=end

