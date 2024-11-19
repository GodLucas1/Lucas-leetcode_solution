#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        first_circle = True

        while slow != fast or first_circle:

            if fast is None or fast.next is None:
                return None
            
            fast = fast.next.next

            slow = slow.next

            first_circle = False


        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
        
# @lc code=end

