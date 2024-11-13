#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        g_i ,s_i = 0, 0
        len_g, len_s = len(g), len(s)

        while g_i < len_g and s_i < len_s:

            if g[g_i] <= s[s_i]:
                g_i += 1
            s_i += 1
        return g_i

        
# @lc code=end

