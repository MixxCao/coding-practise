#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        l, r = dummy, dummy
        for i in range(1, left):
            l = l.next
            r = r.next
            
        for i in range(right - left):
            if i == 0:
                r = r.next
                
            x = r.next
            r.next = r.next.next
            
            x.next = l.next
            l.next = x
            
        return dummy.next
            
            
            
            
# @lc code=end

