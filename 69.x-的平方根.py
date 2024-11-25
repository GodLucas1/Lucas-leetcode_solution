#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        l = 1
        r = x

        while l <= r:

            mid = (l + r) // 2
            mid_sql = mid**2

            if mid_sql == x:
                return mid
            
            if mid_sql < x:
                l = mid + 1
            else:
                r = mid - 1

        return r
        
# @lc code=end

