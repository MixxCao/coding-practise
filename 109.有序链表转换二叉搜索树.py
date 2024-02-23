#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(val = head.val)
        
        dummy = ListNode(next = head)
        slow, quick = dummy, dummy
        
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        
        x = slow.next
        slow.next = None
        return TreeNode(
            val = x.val,
            left = self.sortedListToBST(dummy.next),
            right = self.sortedListToBST(x.next)
        )    
        
# @lc code=end

