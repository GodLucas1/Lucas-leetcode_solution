#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq = Counter(t)

        l = 0
        count = 0
        min_l = None
        min_length = None

        for r in range(len(s)):

            if s[r] not in freq:
                continue

            freq[s[r]] -= 1
            if freq[s[r]] >= 0:
                count += 1

            while count == len(t):

                if min_length is None or r - l + 1 < min_length:
                    min_l = l
                    min_length = r - l + 1
                
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        count -= 1

                l += 1

        return "" if min_length is None else s[min_l: min_l + min_length]



# @lc code=end

