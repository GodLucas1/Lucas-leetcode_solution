#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 先用lambda函数对列表进行排序

        shoot = len(points)
        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        for i in range(1, len(points)):

            if prev_end >= points[i][0]:
                shoot -= 1
            else:
                prev_end = points[i][1]
        
        return shoot


[[1,2], [2,3], [3, 4], [4, 5]]

        
# @lc code=end

