#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.

from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = self.bfs(root, 0, 0)
        return res
    
    
    def bfs(self, node, current_number, res):
        current_number = current_number * 10 + node.val
        
        if node.left is None and node.right is None:
            return res + current_number 
        
        
        if node.left:
            res = self.bfs(node.left, current_number, res)
        if node.right:
            res = self.bfs(node.right, current_number, res)
            
        return res
        
# @lc code=end

