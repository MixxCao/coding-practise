#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {}
        in_order_cnt = [0] * numCourses
        available_flag = [1] * numCourses
        
        for e in prerequisites:
            if e[1] not in edges:
                edges[e[1]] = [e[0]]
            else:
                edges[e[1]].append(e[0])
                
            in_order_cnt[e[0]] += 1
        
        for i in range(numCourses):
            flag = False
            for i in range(numCourses):
                if available_flag[i] < 1:
                    continue
                # flag = True
                if in_order_cnt[i] == 0:
                    flag = True
                    available_flag[i] = 0
                    
                    if i in edges:
                        for n in edges[i]:
                            in_order_cnt[n] -= 1
                    break
                
            if not flag:
                return False
                
                
        return True
                    
                
                
                
                
                
        
# @lc code=end

