#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        left, right = head, head.next
        left.next = None
        while left is not None and right is not None:
            x = right.next
            right.next = left
            left = right
            right = x
        
        return left
            
# @lc code=end

