#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        m1 = m - 1
        n1 = n - 1

        while n1 >= 0 and m1 >= 0:

            if nums1[m1] > nums2[n1]:
                nums1[pos] = nums1[m1]
                m1 -= 1
            else:
                nums1[pos] = nums2[n1]
                n1 -= 1
            pos -= 1

        nums1[:n1+1] = nums2[:n1+1]

        
# @lc code=end

