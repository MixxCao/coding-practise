#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(
            [],
            root,
            targetSum,
            result
        )
        
        return result
    
    def dfs(self, path, node, targetSum, result) -> None:
        if node is None:
            return 
        
        if node.left is None and node.right is None:
            if sum(path) + node.val == targetSum:
                result.append([p for p in path] + [node.val])
            return

        path.append(node.val)
        # left 
        self.dfs(path, node.left, targetSum, result)
        # right
        self.dfs(path, node.right, targetSum, result)
        path.pop()
            
# @lc code=end

