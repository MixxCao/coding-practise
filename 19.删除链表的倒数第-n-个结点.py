#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        dummy = ListNode(next = head)
        low, high = dummy, head
        
        for i in range(n):
            high = high.next
            if high is None and i == n-1:
                return head.next
            
        while high:
            low = low.next
            high = high.next
        
        x = low.next
        low.next = low.next.next
        del x
        
        return dummy.next
            
# @lc code=end

