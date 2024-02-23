#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        if n == 1:
            return "1"
        idx = []
        ns = list(map(str, range(1, n+1)))
        res = []
        
        size = 1
        
        for i in range(1, n+1):
            size *= i
            
        while n > 0:
            if n == 2:
                if k == 1:
                    idx.extend([0, 0])
                else:
                    idx.extend([1, 0])
                    
                break

            size = int(size / n)
            idx.append((k-1) // size)
            k = k % size
            n = n - 1
        
        # print(idx)    
        
        while idx:
            res.append(
                ns.pop(
                    idx.pop(0)
                )
            )
        # print(res)
        return ''.join(res)
            
        
            
            
# @lc code=end

