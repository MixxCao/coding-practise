#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        hp = [[1] * n for _ in range(m)]
        
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m-1 and j == n-1:continue
                if i == m - 1:
                    hp[i][j] = max(hp[i][j+1] - dungeon[i][j+1], 1)
                    continue
                if j == n - 1:
                    hp[i][j] = max(hp[i+1][j] - dungeon[i+1][j], 1)
                    continue
                hp[i][j] = min(hp[i+1][j] - dungeon[i+1][j], hp[i][j+1] - dungeon[i][j+1])
                hp[i][j] = max(hp[i][j], 1)
        # print(hp)    
        return max(hp[0][0] - dungeon[0][0], 1)
# @lc code=end

