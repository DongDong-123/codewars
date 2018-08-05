class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        list_bottom = []
        n = len(grid)
        end_jian = 0
        for i in range(n):
            for v in range(0, len(grid[i])):
                x_zhou = (i, v, grid[i][v])
                print(x_zhou)
                if grid[i][v] == 0:
                    end_jian += 1
                list_bottom.append(x_zhou)
                # print('v:',grid[i][v])
        # 底投影面积
        end = len(list_bottom) - end_jian
        print('end:', end)
        print(list_bottom)
        yy = []
        xx = []
        for t in range(n):
            # y轴投影面积
            y_area1 = []
            for i in range(len(list_bottom)):
                if list_bottom[i][0] == t:
                    y_area1.append(list_bottom[i][-1])

            yy.append(max(y_area1))

            # x轴投影面积
            x_area1 = []
            for i in range(len(list_bottom)):
                if list_bottom[i][1] == t:
                    x_area1.append(list_bottom[i][-1])

            xx.append(max(x_area1))

        y_area = sum(yy)
        x_area = sum(xx)
        print('x_area:', x_area)
        print('y_area:', y_area)
        total = x_area + y_area + end
        print(total)
        return total


Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
Solution().projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
# Solution().projectionArea([[1, 0], [0, 2]])
# Solution().projectionArea([[2]])


"""
在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

示例 1：
输入：[[2]]
输出：5

示例 2：
输入：[[1,2],[3,4]]
输出：17

示例 3：
输入：[[1,0],[0,2]]
输出：8

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：14

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：21

提示：
1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50
"""