#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        count = 0
        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.v_func(s, left, right-1) or self.v_func(s, left+1, right)

        return True
    
    def v_func(self, s: str, left: int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True






# @lc code=end

