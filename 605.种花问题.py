#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flower_len = len(flowerbed)
        index = 0
        flower_place = 0

        while index < flower_len:
            if flowerbed[index] == 1:
                index += 2
            else:
                if index == flower_len-1:
                    flower_place += 1
                    break
                if flowerbed[index+1] == 1:
                    index += 3
                else:
                    flower_place += 1
                    index += 2
        if flower_place >= n:
            return True
        else:
            return False



        
# @lc code=end

