#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q0, q1 = [root], []
        
        res = []
        
        while q0 or q1:
            q = q0 if len(q0) > 0 else q1
            other_q = q1 if len(q0) > 0 else q0
            this_level_res = []
            while q:
                node = q.pop(0)
                this_level_res.append(node.val)
                if node.left:
                    other_q.append(node.left)
                if node.right:
                    other_q.append(node.right)
            res.append(this_level_res)      
        return res
        
        
        
# @lc code=end

