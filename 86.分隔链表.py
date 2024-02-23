#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = s = ListNode()
        large = l = ListNode()
        
        while head:
            next_head = head.next
            
            if head.val < x:
                s.next = head
                s = s.next
                s.next = None
            else:
                l.next = head
                l = l.next
                l.next = None
            
            head = next_head
            
        s.next = large.next
        
        return small.next
# @lc code=end

