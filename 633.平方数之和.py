#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(math.sqrt(c))

        while left <= right:

            sum = left ** 2 + right ** 2

            if sum == c:
                return True
            elif sum > c:
                right -= 1
            else:
                left += 1

        return False

            
            
        
# @lc code=end

