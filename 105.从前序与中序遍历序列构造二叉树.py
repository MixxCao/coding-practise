#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val = preorder[0])
        
        idx = inorder.index(preorder[0])
        return TreeNode(
            val = preorder[0], 
            left = self.buildTree(preorder[1:idx+1], inorder[0:idx]),
            right = self.buildTree(preorder[idx+1:], inorder[idx+1:]), 
        )
        
# @lc code=end

