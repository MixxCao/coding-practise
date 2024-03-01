#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        p = res = ListNode()
        h = [(l.val, i) for i, l in enumerate(lists) if l is not None]
        heapq.heapify(h)
                
        while len(h) > 0:
            _, idx = heapq.heappop(h)
            node = lists[idx]
            lists[idx] = lists[idx].next
            
            p.next = node
            p = p.next
            
            if lists[idx] is None:
                continue
            else:
                heapq.heappush(h, (lists[idx].val, idx))
        
        
        return res.next
# @lc code=end

